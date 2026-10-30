from sgg._graph.base.twodimensional import TwoDimensional

__all__ = ("Plot",)


class Plot(TwoDimensional):
    def __init__(self, cnf={}, **kw):
        _default_dict = cnf | kw
        x = _default_dict.pop("x", None)
        y = _default_dict.pop("y", None)
        super().__init__(_default_dict)
        self._ax.plot(x, y)
