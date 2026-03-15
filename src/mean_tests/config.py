from __future__ import annotations

from typing import Annotated

import pydantic


PositiveFloat = Annotated[pydantic.StrictFloat, pydantic.Field(gt=0)]
Proportion = Annotated[pydantic.StrictFloat, pydantic.Field(gt=0, lt=1)]
NSimulations = Annotated[pydantic.StrictInt, pydantic.Field(gt=0)]
NBuckets = Annotated[pydantic.StrictInt, pydantic.Field(ge=10)]


class ControlConfig(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")

    mean: PositiveFloat
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
    n_simulations: NSimulations
    alpha: Proportion
    power: Proportion
    pp_diff: PositiveFloat
    buckets: tuple[NBuckets, ...]
    output: pydantic.StrictStr
    control: ControlConfig
    treatments: tuple[TreatmentConfig, ...]
