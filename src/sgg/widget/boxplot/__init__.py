from numpy import asarray

from sgg._constant import _TWODIMENSIONAL_PROPERTY_DICT
from sgg._graph.base.twodimensional import TwoDimensional
from sgg.models import _setDefaultValues1, _setDefaultValues2, _update_dict

__all__ = ("Boxplot",)


class Boxplot(TwoDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "autorange": False,
            "bootstrap": None,
            "boxprops": None,
            "capprops": None,
            "capwidths": None,
            "conf_intervals": None,
            "flierprops": None,
            "label": None,
            "manage_ticks": True,
            "meanline": None,
            "meanprops": None,
            "medianprops": None,
            "notch": None,
            "orientation": "vertical",
            "patch_artist": None,
            "positions": None,
            "showbox": None,
            "showcaps": None,
            "showfliers": None,
            "showmeans": None,
            "sym": None,
            "tick_labels": None,
            "usermedians": None,
            "values": None,
            "vert": None,
            "whis": None,
            "whiskerprops": None,
            "widths": None,
            "zorder": None,
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
        values = kw["values"]
        if values is None:
            raise TypeError
        else:
            values = asarray(values).T
        self._graph = self._ax.boxplot(values, **_setDefaultValues2(kw, {"values"}))
        if kw["label"] is not None:
            self._ax.legend()

    def update(self, values=None, **kw):
        self._clear()
        if values is not None:
            self._default_dict["values"] = self._exclusive_dict["values"] = values
        self._update(kw)
        self._exclusive_dict = _update_dict(self._exclusive_dict, kw)
        self._graph_draw(self._exclusive_dict)
        self._redraw()
