from sgg._graph.base.twodimensional import TwoDimensional
from sgg._graph.style.solid import _check_linestyle
from sgg.models import _setDefaultValues2

__all__ = ("Plot",)


class Plot(TwoDimensional):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        _top_def_dict = TwoDimensional.__new__(cls)._default_dict
        cls = super().__new__(cls)
        _default_dict = {
            "x": None,
            "y": None,
            "label": None,
            "linestyle": "-",
            "marker": None,
        }
        cls._default_dict = _default_dict | _top_def_dict
        return cls

    def __init__(self, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        x = self._default_dict.get("x", None)
        y = self._default_dict.get("y", None)
        label = self._default_dict.get("label", None)
        marker = self._default_dict.get("marker", "o")
        linestyle = _check_linestyle(self._default_dict.get("linestyle", "-"))
        super().__init__(self._default_dict)
        self._graph = self._ax.plot(
            x, y, linestyle=linestyle, label=label, marker=marker
        )
        if label is not None:
            self._ax.legend()
