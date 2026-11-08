from numpy import asanyarray

from sgg._constant import _TWODIMENSIONAL_PROPERTY_DICT
from sgg._graph.base.twodimensional import TwoDimensional
from sgg.models import _setDefaultValues2, _update_dict

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
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        self._values = self._exclusive_dict.pop("values", None)
        super().__init__(self._default_dict)
        self._graph_draw(self._values, self._exclusive_dict)

    def _graph_draw(self, values, kw):
        label = self._default_dict.get("label", None)
        if values is not None:
            self._values = asanyarray(values).T
        else:
            raise TypeError
        self._graph = self._ax.boxplot(self._values, **kw)
        if label is not None:
            self._ax.legend()
        self._set_style()

    def update(self, values=None, **kw):
        self._clear()
        if values is None:
            values = self._values
        self._update(kw)
        self._exclusive_dict = _update_dict(self._exclusive_dict, kw)
        self._graph_draw(values, self._exclusive_dict)
        self._redraw()
