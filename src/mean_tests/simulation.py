from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    import numpy as np

    import mean_tests.config


def generate_simulation_report(
    rng: int | np.random.Generator,
    n_simulations: int,
    alpha: float,
    power: float,
    pp_diff: float,
    buckets: tuple[int, ...],
    control: mean_tests.config.ControlConfig,
    treatments: tuple[mean_tests.config.TreatmentConfig, ...],
) -> str:  # ty:ignore[empty-body]
    ...
