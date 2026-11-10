from matplotlib.figure import Figure
from matplotlib.projections.polar import PolarAxes

from sgg._graph._base import _Top_Graph
from sgg.models import _setDefaultValues2

__all__ = ("Polar",)


class Polar(_Top_Graph):
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
            "theta_direction": True,
            "theta_offset": 0,
            "theta_zero_location_loc": "E",
            "theta_zero_location_offset": 0.0,
            "title": None,
            "title_fontdict": None,
            "title_loc": "center",
            "title_pad": 6.0,
        }
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        dicts = self._default_dict
        self.fig = Figure(
            figsize=(5, 4),
            dpi=dicts["dpi"],
            facecolor=dicts["facecolor"],
            edgecolor=dicts["edgecolor"],
        )
        self._ax: PolarAxes = self.fig.add_subplot(111, projection="polar")
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
        if not isinstance(dicts["theta_direction"], bool):
            dicts["theta_direction"] = True
        self._ax.set_theta_direction(1 if dicts["theta_direction"] else -1)
        self._ax.set_theta_offset(dicts["theta_offset"])
        self._ax.set_theta_zero_location(
            dicts["theta_zero_location_loc"], dicts["theta_zero_location_offset"]
        )
        self._ax.set_thetagrids((0, 45, 90, 135, 180, 225, 270, 315))
