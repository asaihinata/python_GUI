import numpy as np

from sgg._constant import _TWODIMENSIONAL_PROPERTY_DICT
from sgg._graph.base.twodimensional import TwoDimensional
from sgg.models import _setDefaultValues2, _setDefaultValues3

__all__ = ("Waterfall",)


class Waterfall(TwoDimensional):
    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "align": "center",
            "bottom": None,
            "colorline": "#47a",
            "dcolor": "#e97132",
            "linestyle": "-",
            "sums": False,
            "sumstext": "sum",
            "ucolor": "#156082",
            "width": 1,
            "x": None,
            "y": None,
        }
        cls._default_dict = cls._exclusive_dict | _TWODIMENSIONAL_PROPERTY_DICT
        cls._exclusion_key = {
            "bottom",
            "color",
            "colorline",
            "dcolor",
            "linestyle",
            "sums",
            "sumstext",
            "ucolor",
            "x",
            "y",
        }
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        super().__init__(self._default_dict)
        self._graph_draw(self._exclusive_dict)

    def _graph_draw(self, kw):
        x = np.asanyarray(kw["x"])
        y = np.asanyarray(kw["y"])
        bottom = np.cumsum(np.append(0, y)[0 : y.size])
        if kw["sums"]:
            x = np.append(x, kw["sumstext"])
            y = np.append(y, np.sum(y))
            bottom = np.append(bottom, 0)
        color = np.where(y < 0, kw["dcolor"], kw["ucolor"])
        self._graph = self._ax.bar(
            x,
            y,
            bottom=bottom,
            color=color,
            **_setDefaultValues3(kw, self._exclusion_key),
        )
        width = kw["width"]
        if width != 1:
            self._horiline(np.cumsum(y), width, kw["colorline"], kw["linestyle"])
        self._set_style()

    def _horiline(self, lin, width=1, color=None, linestyle="-"):
        lens, width, xmaxs, xmins = len(lin) - 1, width / 2, [], []
        for i in range(lens):
            if lin[i] == lin[i + 1]:
                ma, mi = i + width, i + 1.5
            else:
                ma, mi = i + 1 - width, i + width
            xmaxs.append(ma)
            xmins.append(mi)
        self._ax.hlines(
            y=lin,
            xmin=xmins + [0],
            xmax=xmaxs + [0],
            colors=color,
            linestyles=linestyle,
        )
