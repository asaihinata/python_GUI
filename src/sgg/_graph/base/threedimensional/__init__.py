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
            "grid": True,
            "grid_alpha": 0.5,
            "grid_axis": "both",
            "grid_color": "gray",
            "grid_linestyle": "--",
            "grid_linewidth": 0.7,
            "grid_which": "major",
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
        self._set_style()

    def _set_style(self):
        dicts = self._default_dict
        if dicts["grid"]:
            self._ax.grid(
                alpha=dicts["grid_alpha"],
                axis=dicts["grid_axis"],
                color=dicts["grid_color"],
                linestyle=dicts["grid_linestyle"],
                linewidth=dicts["grid_linewidth"],
                which=dicts["grid_which"],
            )
        self._ax.set_title(dicts["title"])
        self._ax.set_xlabel(dicts["xlabel"])
        self._ax.set_ylabel(dicts["ylabel"])
        self._ax.set_zlabel(dicts["zlabel"])
