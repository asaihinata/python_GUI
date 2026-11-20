from tkinter import Variable
from tkinter.ttk import Entry as ttkentry

from sgg.models import _setDefaultValues2, _setDefaultValues3

__all__ = ("TEntry",)


class TEntry(ttkentry):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "background": None,
            "cursor": None,
            "exportselection": True,
            "font": None,
            "foreground": "",
            "invalidcommand": "",
            "justify": "left",
            "name": None,
            "show": "",
            "state": "normal",
            "takefocus": None,
            "value": None,
            "validate": "none",
            "validatecommand": "",
            "width": 20,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._variable = Variable(value=self._default_dict["value"])
        super().__init__(
            master,
            textvariable=self._variable,
            class_="TEntry",
            style="TEntry",
            **_setDefaultValues3(self._default_dict, {"value", "textvariable"}),
        )

    def set(self, value):
        self._default_dict["value"] = value
        self._variable.set(value=value)
