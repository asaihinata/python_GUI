from tkinter.ttk import Scale as ttkscale

from sgg.models import _setDefaultValues2

__all__ = ("TScale",)


class TScale(ttkscale):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "command": "",
            "cursor": "",
            "from_": 0.0,
            "length": 100,
            "name": None,
            "orient": "horizontal",
            "state": None,
            "takefocus": None,
            "to": 100.0,
            "value": 0.0,
            "variable": None,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        orient = self._default_dict["orient"]
        if orient not in ("horizontal", "vertical"):
            orient = "horizontal"
        stylename = "Horizontal.TScale" if orient == "horizontal" else "Vertical.TScale"
        super().__init__(master, class_="TScale", style=stylename, **self._default_dict)
