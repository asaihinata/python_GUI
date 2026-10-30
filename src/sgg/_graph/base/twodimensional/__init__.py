from matplotlib.axes._axes import Axes
from matplotlib.figure import Figure

from sgg._graph._base import _Base_Graph, _Top_Graph
from sgg.models import _setDefaultValues2

__all__ = ("TwoDimensional",)


class TwoDimensional(_Top_Graph):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "dpi": 100,
            "facecolor": None,
            "edgecolor": None,
            "linewidth": 0.0,
            "title": None,
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
        self._ax = self.fig.add_subplot(111)
        self._ax.set_title(self._default_dict["title"])

    @property
    def ax(self) -> Axes:
        return self._ax

    def widget(self, master=None):
        return _Base_Graph.__new__(self, master=master, figure=self.fig)
