from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.axes3d import Axes3D

from sgg._graph._base import _Top_Graph
from sgg.models import _setDefaultValues2

__all__ = ("ThreeDimensional",)


class ThreeDimensional(_Top_Graph):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "dpi": 100,
            "edgecolor": None,
            "facecolor": None,
            "linewidth": 0.0,
            "title": None,
            "xlabel": None,
            "ylabel": None,
            "zlabel": None,
        }
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self.fig = Figure(
            figsize=(5, 4),
            dpi=self._default_dict["dpi"],
            facecolor=self._default_dict["facecolor"],
            edgecolor=self._default_dict["edgecolor"],
        )
        self._ax = self.fig.add_subplot(111, projection="3d")
        self._ax.set_title(self._default_dict["title"])
        self._ax.set_xlabel(self._default_dict["xlabel"])
        self._ax.set_ylabel(self._default_dict["ylabel"])
        self._ax.set_zlabel(self._default_dict["zlabel"])

    @property
    def ax(self) -> Axes3D:
        return self._ax
