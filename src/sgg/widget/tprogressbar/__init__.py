from tkinter.ttk import Progressbar as ttkprogressbar

from sgg.models import _setDefaultValues2

__all__ = ("TProgressbar",)


class TProgressbar(ttkprogressbar):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "cursor": "",
            "length": 100,
            "maximum": 100,
            "mode": "determinate",
            "name": None,
            "orient": "horizontal",
            "phase": 0,
            "takefocus": "",
            "value": 0.0,
            "variable": None,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        orient = self._default_dict["orient"]
        if orient not in ("horizontal", "vertical"):
            orient = "horizontal"
        stylename = (
            "Horizontal.TProgressbar"
            if orient == "horizontal"
            else "Vertical.TProgressbar"
        )
        super().__init__(
            master, class_="TProgressbar", style=stylename, **self._default_dict
        )
