from sgg._constant import _TWODIMENSIONAL_PROPERTY_DICT
from sgg._graph.base.twodimensional import TwoDimensional
from sgg.models import _setDefaultValues1, _setDefaultValues2, _update_dict

__all__ = ("Eventplot",)


class Eventplot(TwoDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "alpha": None,
            "colors": None,
            "label": None,
            "linelengths": 1,
            "lineoffsets": 1,
            "linestyles": "solid",
            "linewidths": None,
            "orientation": "vertical",
            "values": None,
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
        self._graph = self._ax.eventplot(
            kw["values"], **_setDefaultValues2(kw, {"values"})
        )
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
