from sgg._constant import _THREEDIMENSIONAL_PROPERTY_DICT
from sgg._graph.base.threedimensional import ThreeDimensional
from sgg.models import _setDefaultValues2, _update_dict

__all__ = ("DScatter",)


class DScatter(ThreeDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "alpha": None,
            "c": None,
            "cmap": None,
            "colorizer": None,
            "edgecolors": None,
            "label": None,
            "linestyle": "-",
            "linewidths": None,
            "marker": None,
            "norm": None,
            "plotnonfinite": False,
            "s": 20,
            "vmax": None,
            "vmin": None,
            "x": None,
            "y": None,
            "z": None,
        }
        cls._default_dict = cls._exclusive_dict | _THREEDIMENSIONAL_PROPERTY_DICT
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        self._x = self._exclusive_dict.pop("x", None)
        self._y = self._exclusive_dict.pop("y", None)
        self._z = self._exclusive_dict.pop("z", None)
        super().__init__(self._default_dict)
        self._graph_draw(self._x, self._y, self._z, self._exclusive_dict)

    def _graph_draw(self, x, y, z, kw):
        label = self._default_dict.get("label", None)
        self._graph = self._ax.scatter(x, y, z, **kw)
        if label is not None:
            self._ax.legend()
        self._set_style()

    def update(self, x=None, y=None, z=None, **kw):
        self._clear()
        if x is not None:
            self._x = x
        if y is not None:
            self._y = y
        if z is not None:
            self._z = z
        self._update(kw)
        self._exclusive_dict = _update_dict(self._exclusive_dict, kw)
        self._graph_draw(self._x, self._y, self._z, self._exclusive_dict)
        self._redraw()
