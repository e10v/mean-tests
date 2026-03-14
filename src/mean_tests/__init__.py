from __future__ import annotations

import tqdm

import mean_tests.config


def main() -> None:
    config = mean_tests.config.load_config()
    tqdm.tqdm.write(str(config))
