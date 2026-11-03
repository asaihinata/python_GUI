from tkinter import DoubleVar, IntVar
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
            "maximum": None,
            "mode": "determinate",
            "name": None,
            "orient": "horizontal",
            "phase": 0,
            "takefocus": "",
            "value": 0.0,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        value = self._default_dict["value"]
        self.set_value(value)
        maximum = self._default_dict.pop("maximum", None)
        if maximum is None or not isinstance(maximum, int | float):
            maximum = self._maximum(100)
        else:
            maximum = self._maximum(maximum)
        orient = self._default_dict["orient"]
        if orient not in ("horizontal", "vertical"):
            orient = "horizontal"
        stylename = (
            "Horizontal.TProgressbar"
            if orient == "horizontal"
            else "Vertical.TProgressbar"
        )
        super().__init__(
            master,
            variable=self._variable,
            maximum=maximum,
            class_="TProgressbar",
            style=stylename,
            **self._default_dict,
        )

    def get_value(self):
        return self._variable.get()

    def set_value(self, value):
        if isinstance(value, int):
            self._variable = IntVar(value=value)
        elif isinstance(value, float):
            self._variable = DoubleVar(value=value)
        else:
            raise TypeError
        return self._variable

    def _maximum(self, val):
        vals = self._variable.get()
        return vals if val < vals else val
