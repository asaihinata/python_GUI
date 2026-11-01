from sgg._graph.base.twodimensional import TwoDimensional
from sgg.models import _setDefaultValues2
from sgg.version import __matplotlib_version_info__

__all__ = ("Violinplot",)


class Violinplot(TwoDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        _top_def_dict = TwoDimensional.__new__(cls)._default_dict
        cls = super().__new__(cls)
        if __matplotlib_version_info__ >= (3, 11):
            cls._exclusive_dict = {
                "data": None,
                "positions": None,
                "orientation": "vertical",
                "widths": 0.5,
                "showmeans": False,
                "showextrema": True,
                "showmedians": False,
                "quantiles": None,
                "points": 100,
                "bw_method": None,
                "side": "both",
                "facecolor": None,
                "linecolor": None,
            }
        elif __matplotlib_version_info__ >= (3, 10):
            cls._exclusive_dict = {
                "data": None,
                "positions": None,
                "orientation": "vertical",
                "widths": 0.5,
                "showmeans": False,
                "showextrema": True,
                "showmedians": False,
                "quantiles": None,
                "points": 100,
                "bw_method": None,
                "side": "both",
            }
        else:
            cls._exclusive_dict = {
                "data": None,
                "positions": None,
                "vert": True,
                "widths": 0.5,
                "showmeans": False,
                "showextrema": True,
                "showmedians": False,
                "quantiles": None,
                "points": 100,
                "bw_method": None,
                "side": "both",
            }
        cls._default_dict = cls._exclusive_dict | _top_def_dict
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        data = self._exclusive_dict.pop("data", None)
        super().__init__(self._default_dict)
        self._graph = self._ax.violinplot(data, **self._exclusive_dict)
