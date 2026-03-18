from __future__ import annotations

import argparse
import pathlib
import tomllib

import mean_tests.config
import mean_tests.simulation


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        dest="config",
        type=str,
        default="configs/default.toml",
        help="Config file",
        required=False,
    )

    config_path = pathlib.Path(parser.parse_args().config)
    raw_config = tomllib.loads(config_path.read_text(encoding="utf-8"))
    config = mean_tests.config.MeanTestsConfig.model_validate(raw_config)

    report = mean_tests.simulation.generate_simulation_report(
        rng=config.rng,
        n_simulations=config.n_simulations,
        user_tests=config.user_tests,
        bucket_tests=config.bucket_tests,
        buckets=config.buckets,
        sample=config.sample,
        control=config.control,
        treatments=config.treatments,
    )

    output_path = pathlib.Path(config.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(report + "\n", encoding="utf-8")
