"""
塗りつぶしグラフのオブジェクトが入ったモジュール

References:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.fill.html
    https://matplotlib.org/stable/api/_as_gen/matplotlib.patches.Polygon.html
"""

from sgg._constant import _TWODIMENSIONAL_PROPERTY_DICT
from sgg._graph.base.twodimensional import TwoDimensional
from sgg.models import _setDefaultValues2, _setDefaultValues3, _update_dict

__all__ = ("Fill",)


class Fill(TwoDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "alpha": 1,
            "color": None,
            "fill": True,
            "label": None,
            "linestyle": "-",
            "linewidth": 1.0,
            "x": None,
            "y": None,
        }
        cls._default_dict = cls._exclusive_dict | _TWODIMENSIONAL_PROPERTY_DICT
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        super().__init__(self._default_dict)
        self._graph_draw(self._exclusive_dict)

    def _graph_draw(self, kw):
        self._set_style()
        self._graph = self._ax.fill(
            kw["x"], kw["y"], **_setDefaultValues3(kw, {"x", "y"})
        )
        if kw["label"] is not None:
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
