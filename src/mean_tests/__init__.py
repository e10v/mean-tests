from __future__ import annotations

import argparse
import tomllib

import tqdm

import mean_tests.config


def main() -> None:
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
        raw_config = tomllib.load(f)
    config = mean_tests.config.MeanTestsConfig.model_validate(raw_config)
    tqdm.tqdm.write(str(config))
