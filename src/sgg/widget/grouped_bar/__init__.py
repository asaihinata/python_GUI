"""
グループ棒グラフのオブジェクトが入ったモジュール

References:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grouped_bar.html
"""

from sgg._constant import _TWODIMENSIONAL_PROPERTY_DICT
from sgg._graph.base.twodimensional import TwoDimensional
from sgg.models import _setDefaultValues2, _update_dict
from sgg.version import __matplotlib_version_info__

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
        if __matplotlib_version_info__ < (3, 11):
            raise ImportError("matplotlibのバージョンを3.11以上にしてください")
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        self._x = self._exclusive_dict.pop("x", None)
        self._y = self._exclusive_dict.pop("y", None)
        super().__init__(self._default_dict)
        self._graph_draw(self._x, self._y, self._exclusive_dict)

    def _graph_draw(self, x, y, kw):
        label = self._default_dict.get("label", None)
        self._graph = self._ax.grouped_bar(y, tick_labels=x, **kw)
        if label is not None:
            self._ax.legend()
        self._set_style()

    def update(self, x=None, y=None, **kw):
        self._clear()
        if x is not None:
            self._x = x
        if y is not None:
            self._y = y
        self._update(kw)
        self._exclusive_dict = _update_dict(self._exclusive_dict, kw)
        self._graph_draw(self._x, self._y, self._exclusive_dict)
        self._redraw()
