from sgg._graph.base.twodimensional import TwoDimensional
from sgg.models import _setDefaultValues2, _update_dict

__all__ = ("Eventplot",)


class Eventplot(TwoDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        _top_def_dict = TwoDimensional.__new__(cls)._default_dict
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
        cls._default_dict = cls._exclusive_dict | _top_def_dict
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        self._values = self._exclusive_dict.pop("values", None)
        label = self._default_dict.get("label", None)
        super().__init__(self._default_dict)
        self._graph = self._ax.eventplot(self._values, **self._exclusive_dict)
        if label is not None:
            self._ax.legend()

    def update(self, values=None, **kw):
        self._clear()
        if values is not None:
            self._values = values
        self._update(kw)
        self._set_style()
        self._exclusive_dict = _update_dict(self._exclusive_dict, kw)
        self._graph = self._ax.eventplot(self._values, **self._exclusive_dict)
        self._redraw()
