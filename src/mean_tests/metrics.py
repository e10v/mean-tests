# ruff: noqa: RUF001
from __future__ import annotations

import tea_tasting as tt


def get_user_metrics() -> dict[str, tt.metrics.MetricBase]:
    return {
        "Welch's t-test (users)": tt.Mean("value", equal_var=False),
        "Student's t-test (users)": tt.Mean("value", equal_var=True),
        "Mann–Whitney U test (users)": tt.MannWhitneyU("value", correction=False),
        "Mann–Whitney U test (users, cc)": tt.MannWhitneyU("value", correction=True),
    }


def get_bucket_metrics(b: int) -> dict[str, tt.metrics.MetricBase]:
    return {
        f"Welch's t-test ({b} buckets, ratio)":
            tt.RatioOfMeans("value", "users", equal_var=False),
        f"Student's t-test ({b} buckets, ratio)":
            tt.RatioOfMeans("value", "users", equal_var=True),
        f"Welch's t-test ({b} buckets, avg)":
            tt.Mean("value_per_user", equal_var=False),
        f"Student's t-test ({b} buckets, avg)":
            tt.Mean("value_per_user", equal_var=True),
        f"Mann–Whitney U test ({b} buckets)":
            tt.MannWhitneyU("value_per_user", correction=False),
        f"Mann–Whitney U test ({b} buckets, cc)":
            tt.MannWhitneyU("value_per_user", correction=True),
    }
