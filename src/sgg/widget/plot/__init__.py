from sgg._graph.base.twodimensional import TwoDimensional

from sgg.models import _setDefaultValues2

__all__ = ("Plot",)


class Plot(TwoDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        _top_def_dict = TwoDimensional.__new__(cls)._default_dict
        cls = super().__new__(cls)
        cls._exclusive_dict = {
            "label": None,
            "linestyle": "-",
            "marker": None,
            "x": None,
            "y": None,
        }
        cls._default_dict = cls._exclusive_dict | _top_def_dict
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        x = self._exclusive_dict.pop("x", None)
        y = self._exclusive_dict.pop("y", None)
        label = self._default_dict.get("label", None)
        super().__init__(self._default_dict)
        self._graph = self._ax.plot(x, y, **self._exclusive_dict)
        if label is not None:
            self._ax.legend()
