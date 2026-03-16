from __future__ import annotations

from typing import Annotated, Any

import pydantic


PositiveFloat = Annotated[pydantic.StrictFloat, pydantic.Field(gt=0)]
Proportion = Annotated[pydantic.StrictFloat, pydantic.Field(gt=0, lt=1)]
IntGE10 = Annotated[pydantic.StrictInt, pydantic.Field(ge=10)]


class ControlConfig(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")

    mean: PositiveFloat
    top_users: Proportion
    top_value: Proportion


class TreatmentConfig(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")

    name: pydantic.StrictStr
    pp_diff_top: pydantic.StrictFloat
    pp_diff_bottom: pydantic.StrictFloat


class TestConfig(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")

    name: pydantic.StrictStr
    path: pydantic.StrictStr
    args: tuple[pydantic.StrictStr, ...]
    kwargs: dict[pydantic.StrictStr, Any]


class MeanTestsConfig(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")

    output: pydantic.StrictStr
    rng: pydantic.StrictInt
    n_simulations: IntGE10
    buckets: tuple[IntGE10, ...]
    alpha: Proportion
    power: Proportion
    pp_diff_default: PositiveFloat
    control: ControlConfig
    treatments: tuple[TreatmentConfig, ...]
    user_tests: tuple[TestConfig, ...]
    bucket_tests: tuple[TestConfig, ...]
