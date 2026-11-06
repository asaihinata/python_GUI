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
                "bw_method": None,
                "facecolor": None,
                "linecolor": None,
                "orientation": "vertical",
                "points": 100,
                "positions": None,
                "quantiles": None,
                "showextrema": True,
                "showmeans": False,
                "showmedians": False,
                "side": "both",
                "values": None,
                "widths": 0.5,
            }
        elif __matplotlib_version_info__ >= (3, 10):
            cls._exclusive_dict = {
                "bw_method": None,
                "orientation": "vertical",
                "points": 100,
                "positions": None,
                "quantiles": None,
                "showextrema": True,
                "showmeans": False,
                "showmedians": False,
                "side": "both",
                "values": None,
                "widths": 0.5,
            }
        else:
            cls._exclusive_dict = {
                "bw_method": None,
                "points": 100,
                "positions": None,
                "quantiles": None,
                "showextrema": True,
                "showmeans": False,
                "showmedians": False,
                "side": "both",
                "values": None,
                "vert": True,
                "widths": 0.5,
            }
        cls._default_dict = cls._exclusive_dict | _top_def_dict
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        values = self._exclusive_dict.pop("values", None)
        super().__init__(self._default_dict)
        self._graph = self._ax.violinplot(values, **self._exclusive_dict)
