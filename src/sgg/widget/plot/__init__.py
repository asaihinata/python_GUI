from sgg._constant import _TWODIMENSIONAL_PROPERTY_DICT
from sgg._graph.base.twodimensional import TwoDimensional
from sgg.models import _setDefaultValues2, _update_dict

__all__ = ("Plot",)


class Plot(TwoDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "label": None,
            "linestyle": "-",
            "marker": None,
            "x": None,
            "y": None,
        }
        cls._default_dict = cls._exclusive_dict | _TWODIMENSIONAL_PROPERTY_DICT
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        self._x = self._exclusive_dict.pop("x", None)
        self._y = self._exclusive_dict.pop("y", None)
        label = self._default_dict.get("label", None)
        super().__init__(self._default_dict)
        self._graph = self._ax.plot(self._x, self._y, **self._exclusive_dict)
        if label is not None:
            self._ax.legend()

    def update(self, x=None, y=None, **kw):
        self._clear()
        if x is not None:
            self._x = x
        if y is not None:
            self._y = y
        self._update(kw)
        self._set_style()
        self._exclusive_dict = _update_dict(self._exclusive_dict, kw)
        self._graph = self._ax.plot(self._x, self._y, **self._exclusive_dict)
        self._redraw()
