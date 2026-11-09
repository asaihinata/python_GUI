import numpy as np
from matplotlib.figure import Figure

from sgg._graph._base import _Top_Graph
from sgg._graph.base.radar.custom import radar_factory
from sgg.models import _setDefaultValues2

__all__ = ("Radar",)


class Radar(_Top_Graph):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "value": None,
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
            "title": None,
            "xlabel": None,
            "ylabel": None,
        }
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._default_dict["value"] = np.asarray(self._default_dict["value"])
        self._set_theta()
        self.fig = Figure(
            figsize=(5, 4),
            dpi=self._default_dict["dpi"],
            facecolor=self._default_dict["facecolor"],
            edgecolor=self._default_dict["edgecolor"],
        )
        self._ax = self.fig.add_subplot(111, projection="radar")

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
        self._set_theta()
        self._ax.set_title(dicts["title"])
        self._ax.set_xlabel(dicts["xlabel"])
        self._ax.set_ylabel(dicts["ylabel"])
        self._ax.set_xticks(self._theta)
        self._ax.set_theta_zero_location("N")  # 方向の決定
        self._ax.set_theta_direction(-1)  # 時計回り

    def _set_theta(self):
        self._theta = radar_factory(self._default_dict["value"].shape[-1])
        return self._theta

    def _update(self, kw):
        for k, v in kw.items():
            if k != "value":
                self._default_dict[k] = v
