from sgg._constant import _TWODIMENSIONAL_PROPERTY_DICT
from sgg._graph.base.twodimensional import TwoDimensional
from sgg.models import _setDefaultValues2, _update_dict

__all__ = ("Pie",)


class Pie(TwoDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "autopct": None,
            "center": (0, 0),
            "colors": None,
            "counterclock": True,
            "explode": None,
            "frame": False,
            "hatch": None,
            "labels": None,
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
        cls._default_dict = cls._exclusive_dict | _TWODIMENSIONAL_PROPERTY_DICT
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        self._value = self._exclusive_dict.pop("value", None)
        super().__init__(self._default_dict)
        self._graph_draw(self._value, self._exclusive_dict)

    def _graph_draw(self, value, kw):
        label = self._default_dict.get("labels", None)
        self._graph = self._ax.pie(value, **kw)
        if label is not None:
            self._ax.legend()
        self._set_style()

    def update(self, value=None, **kw):
        self._clear()
        if value is not None:
            self._value = value
        self._update(kw)
        self._exclusive_dict = _update_dict(self._exclusive_dict, kw)
        self._graph_draw(self._value, self._exclusive_dict)
        self._redraw()
