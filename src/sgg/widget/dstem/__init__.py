"""
References:
    https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.stem.html
"""

from sgg._constant import _THREEDIMENSIONAL_PROPERTY_DICT
from sgg._graph.base.threedimensional import ThreeDimensional
from sgg.models import _setDefaultValues1, _update_dict
from sgg.version import __matplotlib_version_info__

__all__ = ("DStem",)


class DStem(ThreeDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "basefmt": "C3-",
            "bottom": 0,
            "label": None,
            "linefmt": "C0-",
            "markerfmt": "C0o",
            "orientation": "z",
            "x": None,
            "y": None,
            "z": None,
        }
        cls._default_dict = cls._exclusive_dict | _THREEDIMENSIONAL_PROPERTY_DICT
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
        if kw["orientation"] not in ("x", "y", "z"):
            kw["orientation"] = "z"
        label = kw["label"]
        if __matplotlib_version_info__ >= (3, 10):
            self._graph = self._ax.stem(
                kw["x"],
                kw["y"],
                kw["z"],
                linefmt=kw["linefmt"],
                markerfmt=kw["markerfmt"],
                basefmt=kw["basefmt"],
                bottom=kw["bottom"],
                label=label,
                orientation=kw["orientation"],
                axlim_clip=kw["axlim_clip"],
            )
        else:
            self._graph = self._ax.stem(
                kw["x"],
                kw["y"],
                kw["z"],
                linefmt=kw["linefmt"],
                markerfmt=kw["markerfmt"],
                basefmt=kw["basefmt"],
                bottom=kw["bottom"],
                label=label,
                orientation=kw["orientation"],
            )
        if label is not None:
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
