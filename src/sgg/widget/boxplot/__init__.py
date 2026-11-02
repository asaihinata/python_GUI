from numpy import asanyarray

from sgg._graph.base.twodimensional import TwoDimensional
from sgg.models import _setDefaultValues2

__all__ = ("Boxplot",)


class Boxplot(TwoDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        _top_def_dict = TwoDimensional.__new__(cls)._default_dict
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
            "vert": None,
            "whis": None,
            "whiskerprops": None,
            "widths": None,
            "x": None,
            "zorder": None,
        }
        cls._default_dict = cls._exclusive_dict | _top_def_dict
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        x = self._exclusive_dict.pop("x", None)
        if x is not None:
            x = asanyarray(x).T
        else:
            raise TypeError
        label = self._default_dict.get("label", None)
        super().__init__(self._default_dict)
        self._graph = self._ax.boxplot(x, **self._exclusive_dict)
        if label is not None:
            self._ax.legend()
