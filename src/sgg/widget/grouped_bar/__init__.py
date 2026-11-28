"""
グループ棒グラフのオブジェクトが入ったモジュール

References:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grouped_bar.html
"""

from sgg.version import __matplotlib_version_info__

if __matplotlib_version_info__ < (3, 11):
    raise VersionError("matplotlibのバージョンを3.11以上にしてください")
import numpy as np

from sgg._constant import _TWODIMENSIONAL_PROPERTY_DICT
from sgg._graph.base.twodimensional import TwoDimensional
from sgg.exceptions import FraudAxis, VersionError
from sgg.models import _setDefaultValues1, _setDefaultValues2, _update_dict

__all__ = ("Grouped_bar",)


class Grouped_bar(TwoDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "bar_spacing": 0,
            "colors": None,
            "group_spacing": 1.5,
            "labels": None,
            "orientation": "vertical",
            "positions": None,
            "x": None,
            "y": None,
        }
        cls._default_dict = cls._exclusive_dict | _TWODIMENSIONAL_PROPERTY_DICT
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues1(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues1(
            self._exclusive_dict, self._default_dict
        )
        super().__init__(self._default_dict)
        self._graph_draw(self._exclusive_dict)

    def _graph_draw(self, kw):
        self._set_style()
        y = np.asarray(kw["y"])
        if y.ndim == 1:
            y = y[:, np.newaxis]
        elif 2 < y.ndim | y.ndim < 1:
            raise FraudAxis("配列の次元数が不正です")
        x = kw["x"]
        if x is None:
            x = np.arange(y.shape[len(y.shape) - 1] - 1)
        self._graph = self._ax.grouped_bar(
            y, tick_labels=x, **_setDefaultValues2(kw, {"x", "y"})
        )
        if kw["labels"] is not None:
            self._ax.legend()

    def update(self, x=None, y=None, **kw):
        self._clear()
        if x is not None:
            self._default_dict["x"] = self._exclusive_dict["x"] = x
        if y is not None:
            self._default_dict["y"] = self._exclusive_dict["y"] = y
        self._update(kw)
        self._exclusive_dict = _update_dict(self._exclusive_dict, kw)
        self._graph_draw(self._exclusive_dict)
        self._redraw()
