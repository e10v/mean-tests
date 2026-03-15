# ruff: noqa: RUF001
from __future__ import annotations

import tea_tasting as tt


def get_user_experiment() -> tt.Experiment:
    return tt.Experiment({
        "Welch's t-test (users)": tt.Mean("value", equal_var=False),
        "Student's t-test (users)": tt.Mean("value", equal_var=True),
        "Mann–Whitney U test (users)": tt.MannWhitneyU("value"),
    })


def get_bucket_experiments(
    buckets: tuple[int, ...],
) -> dict[int, tt.Experiment]:
    return {
        b: tt.Experiment({
            f"Welch's t-test ({b} buckets)":
                tt.RatioOfMeans("value", "users", equal_var=False),
            f"Student's t-test ({b} buckets)":
                tt.RatioOfMeans("value", "users", equal_var=True),
            f"Mann–Whitney U test ({b} buckets)":
                tt.MannWhitneyU("value_per_user"),
        })
        for b in buckets
    }
