from __future__ import annotations

from typing import Annotated, Any

import pydantic


PositiveFloat = Annotated[pydantic.StrictFloat, pydantic.Field(gt=0)]
Proportion = Annotated[pydantic.StrictFloat, pydantic.Field(gt=0, lt=1)]
IntGE10 = Annotated[pydantic.StrictInt, pydantic.Field(ge=10)]


class SampleConfig(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")

    alpha: Proportion
    power: Proportion
    ratio: PositiveFloat
    rel_diff_default: PositiveFloat
    top_users: Proportion
    top_value: Proportion


class TreatmentConfig(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(extra="forbid")

    name: pydantic.StrictStr
    rel_diff_top: pydantic.StrictFloat
    rel_diff_bottom: pydantic.StrictFloat


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
    sample: SampleConfig
    treatments: tuple[TreatmentConfig, ...]
    user_tests: tuple[TestConfig, ...]
    bucket_tests: tuple[TestConfig, ...]

    @pydantic.model_validator(mode="after")
    def validate_config(self) -> MeanTestsConfig:
        validate_unique_names(self.treatments, "treatments")
        validate_unique_names(self.user_tests, "user_tests")
        validate_unique_names(self.bucket_tests, "bucket_tests")

        top_value = self.sample.top_value
        for treatment in self.treatments:
            name = treatment.name
            rel_diff_top = treatment.rel_diff_top
            rel_diff_bottom = treatment.rel_diff_bottom
            if rel_diff_top + top_value <= 0:
                raise ValueError(
                    "treatment.rel_diff_top + sample.top_value == "
                    f"{rel_diff_top + top_value} for treatment {name}, "
                    "should be greater than 0",
                )
            if rel_diff_bottom + 1 - top_value <= 0:
                raise ValueError(
                    "treatment.rel_diff_bottom + 1 - sample.top_value == "
                    f"{rel_diff_bottom + 1 - top_value} for treatment {name}, "
                    "should be greater than 0",
                )

        return self


def validate_unique_names(
    configs: tuple[TreatmentConfig, ...] | tuple[TestConfig, ...],
    config_name: str,
) -> None:
    seen = set()
    duplicates = set()
    for config in configs:
        if config.name in seen and config.name not in duplicates:
            duplicates.add(config.name)
        seen.add(config.name)

    if duplicates:
        raise ValueError(
            f"{config_name} names must be unique; duplicates: "
            + ", ".join(sorted(duplicates)),
        )
