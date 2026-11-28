from matplotlib.figure import Figure

from sgg._graph._axes import _AXESPOLAR
from sgg._graph._base import _Top_Graph
from sgg.models import _setDefaultValues1

__all__ = ("Polar",)


class Polar(_Top_Graph, _AXESPOLAR):
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
        }
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues1(self._default_dict, cnf, **kw)
        dicts = self._default_dict
        self._fig = Figure(
            figsize=(5, 4),
            dpi=dicts["dpi"],
            facecolor=dicts["facecolor"],
            edgecolor=dicts["edgecolor"],
        )
        self._ax = self._fig.add_subplot(111, projection="polar")
        self._set_style()

    def _set_style(self):
        dicts = self._default_dict
        ax = self._ax
        if dicts["grid"]:
            ax.grid(
                alpha=dicts["grid_alpha"],
                axis=dicts["grid_axis"],
                color=dicts["grid_color"],
                linestyle=dicts["grid_linestyle"],
                linewidth=dicts["grid_linewidth"],
                which=dicts["grid_which"],
            )
        ax.set_title(dicts["title"])
        if not isinstance(dicts["theta_direction"], bool):
            dicts["theta_direction"] = True
        ax.set_theta_direction(1 if dicts["theta_direction"] else -1)
        ax.set_theta_offset(dicts["theta_offset"])
        ax.set_theta_zero_location(
            dicts["theta_zero_location_loc"], dicts["theta_zero_location_offset"]
        )
