from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

import scipy.stats
import tea_tasting as tt
import tea_tasting.utils


if TYPE_CHECKING:
    from collections.abc import Sequence
    from typing import Any

    import mean_tests.config


def create_experiment(tests: tuple[mean_tests.config.TestConfig, ...]) -> tt.Experiment:
    return tt.Experiment({
        test.name: create_metric(test.path, *test.args, **test.kwargs)
        for test in tests
    })


def create_metric(
    path: str,
    *args: str,
    **kwargs: Any,
) -> tea_tasting.metrics.MetricBase:
    mod_name, attr_name = path.rsplit(".", 1)
    module = importlib.import_module(mod_name)
    metric = getattr(module, attr_name)
    return metric(*args, **kwargs)


def format_binom_ci(k_n: list[int]) -> str:
    k, n = k_n
    ci = scipy.stats.binomtest(k, n).proportion_ci(method="wilsoncc")
    low = tea_tasting.utils.format_num(ci[0])
    upp = tea_tasting.utils.format_num(ci[1])
    return f"[{low}, {upp}]"


def render_dict(
    dict_: dict[str, Any],
    keys: tuple[str, str] = ("parameter", "value"),
    text_keys: Sequence[str] | None = None,
) -> str:
    return render_dicts(
        tuple({keys[0]: par, keys[1]: str(val)} for par, val in dict_.items()),
        keys,
        text_keys,
    )


def render_dicts(
    dicts: Sequence[dict[str, Any]],
    keys: Sequence[str] | None = None,
    text_keys: Sequence[str] | None = None,
) -> str:
    if keys is None:
        keys = tuple(dicts[0].keys())
    if text_keys is None:
        text_keys = (keys[0],)
    return PrettyDicts(dicts, keys, text_keys).to_markdown()


class PrettyDicts(tea_tasting.utils.DictsReprMixin):
    def __init__(
        self,
        dicts: Sequence[dict[str, Any]],
        keys: Sequence[str],
        text_keys: Sequence[str],
    ) -> None:
        self.default_keys = keys
        self.default_text_keys = text_keys
        self.dicts = dicts

    def to_dicts(self) -> Sequence[dict[str, Any]]:
        return self.dicts
