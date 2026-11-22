"""
References:
    https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.bar.html
"""

from sgg._constant import _THREEDIMENSIONAL_PROPERTY_DICT
from sgg._graph.base.threedimensional import ThreeDimensional
from sgg.models import _setDefaultValues2, _setDefaultValues3, _update_dict

__all__ = ("DBar",)


class DBar(ThreeDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "align": "center",
            "bottom": None,
            "label": None,
            "width": 0.8,
            "x": None,
            "y": None,
            "z": 0,
            "zdir": "z",
        }
        cls._default_dict = cls._exclusive_dict | _THREEDIMENSIONAL_PROPERTY_DICT
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
        if kw["zdir"] not in ("x", "y", "z"):
            kw["zdir"] = "z"
        self._graph = self._ax.bar(
            kw["x"], kw["y"], kw["z"], **_setDefaultValues3(kw, {"x", "y", "z"})
        )
        if kw["label"] is not None:
            self._ax.legend()

    def update(self, x=None, y=None, z=None, **kw):
        self._clear()
        if x is not None:
            self._default_dict["x"] = self._exclusive_dict["x"] = x
        if y is not None:
            self._default_dict["y"] = self._exclusive_dict["y"] = y
        if z is not None:
            self._default_dict["z"] = self._exclusive_dict["z"] = z
        self._update(kw)
        self._exclusive_dict = _update_dict(self._exclusive_dict, kw)
        self._graph_draw(self._exclusive_dict)
        self._redraw()
