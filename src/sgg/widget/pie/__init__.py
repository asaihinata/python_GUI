from matplotlib.figure import Figure
import numpy as np
from sgg._graph._base import _Top_Graph
from sgg.models import _setDefaultValues2, _setDefaultValues3, _update_dict

__all__ = ("Pie",)


class Pie(_Top_Graph):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "autopct": None,
            "center": (0, 0),
            "colors": None,
            "counterclock": True,
            "explode": None,
            "frame": False,
            "hatch": None,
            "labels": None,
            "labeldistance": 1.1,
            "normalize": True,
            "pctdistance": 0.6,
            "radius": 1,
            "rotatelabels": False,
            "shadow": False,
            "startangle": 0,
            "textprops": None,
            "value": None,
            "wedgeprops": None,
        }
        cls._default_dict = cls._exclusive_dict | {
            "dpi": 100,
            "edgecolor": None,
            "facecolor": None,
            "title": None,
        }
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        self._fig = Figure(
            figsize=(5, 4),
            dpi=self._default_dict["dpi"],
            facecolor=self._default_dict["facecolor"],
            edgecolor=self._default_dict["edgecolor"],
        )
        self._ax = self._fig.add_subplot(111)
        self._graph_draw(self._exclusive_dict)

    def _graph_draw(self, kw):
        value=np.asarray(kw["value"])
        if not value.ndim==1:
            raise ValueError("valueの次元数が不正です")
        elif value.dtype.kind not in ("i","u","f"):
            raise TypeError("配列内の要素の型が不正です")
        elif np.any(value<0):
            raise ValueError("配列内の要素に負の数が含まれています")
        self._graph = self._ax.pie(value, **_setDefaultValues3(kw, {"value"}))
        self._ax.set_title(self._default_dict["title"])
        if kw["labels"] is not None:
            self._ax.legend()

    def update(self, value=None, **kw):
        self._clear()
        if value is not None:
            self._default_dict["value"] = self._exclusive_dict["value"] = value
        self._update(kw)
        self._exclusive_dict = _update_dict(self._exclusive_dict, kw)
        self._graph_draw(self._exclusive_dict)
        self._redraw()
