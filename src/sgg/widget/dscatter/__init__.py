from sgg._graph.base.threedimensional import ThreeDimensional
from sgg.models import _setDefaultValues2, _update_dict

__all__ = ("DScatter",)


class DScatter(ThreeDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        _top_def_dict = ThreeDimensional.__new__(cls)._default_dict
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
        cls._default_dict = cls._exclusive_dict | _top_def_dict
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        self._x = self._exclusive_dict.pop("x", None)
        self._y = self._exclusive_dict.pop("y", None)
        self._z = self._exclusive_dict.pop("z", None)
        label = self._default_dict.get("label", None)
        super().__init__(self._default_dict)
        self._graph = self._ax.scatter(
            self._x, self._y, self._z, **self._exclusive_dict
        )
        if label is not None:
            self._ax.legend()

    def update(self, x=None, y=None, z=None, **kw):
        self._clear()
        if x is not None:
            self._x = x
        if y is not None:
            self._y = y
        if z is not None:
            self._z = z
        self._update(kw)
        self._set_style()
        self._exclusive_dict = _update_dict(self._exclusive_dict, kw)
        self._graph = self._ax.scatter(
            self._x, self._y, self._z, **self._exclusive_dict
        )
        self._redraw()
