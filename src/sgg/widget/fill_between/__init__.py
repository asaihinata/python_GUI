from sgg._constant import _TWODIMENSIONAL_PROPERTY_DICT
from sgg._graph.base.twodimensional import TwoDimensional
from sgg.models import _setDefaultValues2, _setDefaultValues3, _update_dict

__all__ = ("Fill_Between",)


class Fill_Between(TwoDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "alpha": 1,
            "interpolate": False,
            "label": None,
            "step": None,
            "where": None,
            "x": None,
            "y1": None,
            "y2": 0,
        }
        cls._default_dict = cls._exclusive_dict | _TWODIMENSIONAL_PROPERTY_DICT
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
        self._graph = self._ax.fill_between(
            kw["x"], kw["y1"], kw["y2"], **_setDefaultValues3(kw, {"x", "y1", "y2"})
        )
        if kw["label"] is not None:
            self._ax.legend()

    def update(self, x=None, y1=None, y2=None, **kw):
        self._clear()
        if x is not None:
            self._default_dict["x"] = self._exclusive_dict["x"] = x
        if y1 is not None:
            self._default_dict["y1"] = self._exclusive_dict["y1"] = y1
        if y2 is not None:
            self._default_dict["y2"] = self._exclusive_dict["y2"] = y2
        self._update(kw)
        self._exclusive_dict = _update_dict(self._exclusive_dict, kw)
        self._graph_draw(self._exclusive_dict)
        self._redraw()
