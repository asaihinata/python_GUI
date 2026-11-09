"""
塗りつぶしレーダーグラフのオブジェクトが入ったモジュール

References:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.fill.html
"""

import numpy as np

from sgg._constant import _RADAR_PROPERTY_DICT
from sgg._graph.base.radar import Radar
from sgg.models import _setDefaultValues2, _update_dict

__all__ = ("Radarfill",)


class Radarfill(Radar):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "alpha": 1,
            "fill": True,
            "label": None,
            "linestyle": None,
            "linewidth": None,
        }
        cls._default_dict = cls._exclusive_dict | _RADAR_PROPERTY_DICT
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        super().__init__(self._default_dict)
        self._graph_draw(self._default_dict["value"], self._exclusive_dict)

    def _graph_draw(self, value, kw):
        self._set_style()
        label = self._default_dict.get("label", None)
        self._graph = self._ax.fill(self.theta, value, **kw)
        if label is not None:
            self._ax.legend()

    def update(self, value=None, **kw):
        self._clear()
        self._update(kw)
        if value is not None:
            self._default_dict["value"] = np.asarray(value)
        self._exclusive_dict = _update_dict(self._exclusive_dict, kw)
        self._graph_draw(self._default_dict["value"], self._exclusive_dict)
        self._redraw()
