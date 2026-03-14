from __future__ import annotations

import argparse
import tomllib
from typing import TYPE_CHECKING

import tea_tasting.utils


if TYPE_CHECKING:
    from typing import Any


def load_config() -> dict[str, Any]:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        dest="config",
        type=str,
        default="mean-tests.toml",
        help="Config file",
        required=False,
    )
    with open(parser.parse_args().config, "rb") as f:
        config = tomllib.load(f)

    tea_tasting.utils.check_scalar(config["rng"], "rng", typ=int)
    tea_tasting.utils.check_scalar(
        config["n_simulations"], "n_simulations", typ=int, gt=0)
    tea_tasting.utils.check_scalar(config["alpha"], "alpha", typ=float, gt=0, lt=1)
    tea_tasting.utils.check_scalar(config["power"], "power", typ=float, gt=0, lt=1)

    buckets = config["buckets"]
    tea_tasting.utils.check_scalar(buckets, "buckets", typ=list)
    for i, bucket in enumerate(buckets):
        tea_tasting.utils.check_scalar(bucket, f"buckets[{i}]", typ=int, gt=0)

    tea_tasting.utils.check_scalar(config["output"], "output", typ=str)

    control = config["control"]
    tea_tasting.utils.check_scalar(control, "control", typ=dict)
    tea_tasting.utils.check_scalar(control["mean"], "control.mean", typ=float, gt=0)
    tea_tasting.utils.check_scalar(
        control["pareto_users"], "control.pareto_users", typ=float, gt=0, lt=1)
    tea_tasting.utils.check_scalar(
        control["pareto_value"], "control.pareto_value", typ=float, gt=0, lt=1)

    treatments = config["treatments"]
    tea_tasting.utils.check_scalar(treatments, "treatments", typ=list)
    for i, treatment in enumerate(treatments):
        tea_tasting.utils.check_scalar(treatment, f"treatments[{i}]", typ=dict)
        tea_tasting.utils.check_scalar(
            treatment["name"], f"treatments[{i}].name", typ=str)
        tea_tasting.utils.check_scalar(
            treatment["pp_diff_top"], f"treatments[{i}].pp_diff_top", typ=float)
        tea_tasting.utils.check_scalar(
            treatment["pp_diff_bottom"], f"treatments[{i}].pp_diff_bottom", typ=float)

    return config
