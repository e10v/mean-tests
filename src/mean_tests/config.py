from __future__ import annotations

import argparse
import tomllib
from typing import Annotated

import pydantic


Proportion = Annotated[pydantic.StrictFloat, pydantic.Field(gt=0, lt=1)]
PositiveInt = Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]


class ControlConfig(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")

    mean: Annotated[pydantic.StrictFloat, pydantic.Field(gt=0)]
    pareto_users: Proportion
    pareto_value: Proportion


class TreatmentConfig(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")

    name: pydantic.StrictStr
    pp_diff_top: pydantic.StrictFloat
    pp_diff_bottom: pydantic.StrictFloat


class MeanTestsConfig(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")

    rng: pydantic.StrictInt
    n_simulations: PositiveInt
    alpha: Proportion
    power: Proportion
    buckets: tuple[PositiveInt, ...]
    output: pydantic.StrictStr
    control: ControlConfig
    treatments: tuple[TreatmentConfig, ...]


def load_config() -> MeanTestsConfig:
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

    return MeanTestsConfig.model_validate(raw_config)
