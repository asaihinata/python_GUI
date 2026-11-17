from sgg._constant import _POLAR_PROPERTY_DICT
from sgg._graph.base.polar import Polar
from sgg.models import _setDefaultValues2, _setDefaultValues3, _update_dict

__all__ = ("Polarstem",)


class Polarstem(Polar):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "basefmt": None,
            "bottom": 0,
            "label": None,
            "linefmt": None,
            "markerfmt": None,
            "x": None,
            "y": None,
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
        self._graph = self._ax.stem(
            kw["x"],
            kw["y"],
            orientation="vertical",
            **_setDefaultValues3(kw, {"x", "y"}),
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
