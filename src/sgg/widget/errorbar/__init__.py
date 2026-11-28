from sgg._constant import _TWODIMENSIONAL_PROPERTY_DICT
from sgg._graph.base.twodimensional import TwoDimensional
from sgg.models import _setDefaultValues1, _setDefaultValues2, _update_dict

__all__ = ("Errorbar",)


class Errorbar(TwoDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "barsabove": False,
            "capsize": None,
            "capthick": None,
            "ecolor": None,
            "elinestyle": None,
            "elinewidth": None,
            "errorevery": 1,
            "fmt": "o",
            "label": None,
            "linestyle": "none",
            "lolims": False,
            "uplims": False,
            "x": None,
            "xerr": None,
            "xlolims": False,
            "xuplims": False,
            "y": None,
            "yerr": None,
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
        self._graph = self._ax.errorbar(
            kw["x"], kw["y"], **_setDefaultValues2(kw, {"x", "y"})
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
