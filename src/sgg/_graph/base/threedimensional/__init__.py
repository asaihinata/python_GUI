from matplotlib.figure import Figure

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
            "grid": True,
            "grid_alpha": 0.5,
            "grid_axis": "both",
            "grid_color": "gray",
            "grid_linestyle": "--",
            "grid_linewidth": 0.7,
            "grid_which": "major",
            "linewidth": 0.0,
            "title": None,
            "title_fontdict": None,
            "title_pad": 6.0,
            "title_loc": "center",
            "xlabel": None,
            "xlabel_fontdict": None,
            "xlabel_labelpad": 4.0,
            "xlabel_loc": "center",
            "ylabel": None,
            "ylabel_fontdict": None,
            "ylabel_labelpad": 4.0,
            "ylabel_loc": "center",
            "zlabel": None,
            "zlabel_fontdict": None,
            "zlabel_labelpad": 4.0,
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
        self._ax.set_title(
            dicts["title"],
            fontdict=dicts["title_fontdict"],
            loc=dicts["title_loc"],
            pad=dicts["title_pad"],
        )
        self._ax.set_xlabel(
            dicts["xlabel"],
            fontdict=dicts["xlabel_fontdict"],
            loc=dicts["xlabel_loc"],
            labelpad=dicts["xlabel_labelpad"],
        )
        self._ax.set_ylabel(
            dicts["ylabel"],
            fontdict=dicts["ylabel_fontdict"],
            loc=dicts["ylabel_loc"],
            labelpad=dicts["ylabel_labelpad"],
        )
        self._ax.set_zlabel(
            dicts["zlabel"],
            fontdict=dicts["zlabel_fontdict"],
            labelpad=dicts["zlabel_labelpad"],
        )
