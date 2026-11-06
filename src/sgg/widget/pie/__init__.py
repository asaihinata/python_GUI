from sgg._graph.base.twodimensional import TwoDimensional
from sgg.models import _setDefaultValues2

__all__ = ("Pie",)


class Pie(TwoDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        _top_def_dict = TwoDimensional.__new__(cls)._default_dict
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "autopct": None,
            "center": (0, 0),
            "colors": None,
            "counterclock": True,
            "explode": None,
            "frame": False,
            "hatch": None,
            "label": None,
            "labeldistance": 1.1,
            "normalize": True,
            "pctdistance": 0.6,
            "radius": 1,
            "rotatelabels": False,
            "shadow": False,
            "startangle": 0,
            "textprops": None,
            "value": None,
            "wedgeprops": None,
        }
        cls._default_dict = cls._exclusive_dict | _top_def_dict
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        value = self._exclusive_dict.pop("value", None)
        label = self._exclusive_dict.pop("label", None)
        super().__init__(self._default_dict)
        self._graph = self._ax.pie(value, labels=label, **self._exclusive_dict)
        if label is not None:
            self._ax.legend()
