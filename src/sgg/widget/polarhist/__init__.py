from sgg._constant import _POLAR_PROPERTY_DICT
from sgg._graph.base.polar import Polar
from sgg.models import _setDefaultValues2, _setDefaultValues3, _update_dict

__all__ = ("Polarhist",)


class Polarhist(Polar):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "align": "mid",
            "bins": 10,
            "bottom": 0,
            "color": None,
            "cumulative": False,
            "density": False,
            "histtype": "bar",
            "label": None,
            "log": False,
            "range": None,
            "rwidth": None,
            "stacked": False,
            "values": None,
            "weights": None,
        }
        cls._default_dict = cls._exclusive_dict | _POLAR_PROPERTY_DICT
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
        self._graph = self._ax.hist(
            kw["values"], orientation="vertical", **_setDefaultValues3(kw, {"values"})
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
