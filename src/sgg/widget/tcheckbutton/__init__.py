from tkinter import BooleanVar
from tkinter.ttk import Checkbutton as ttkcheckbutton

from sgg.models import _setDefaultValues2

__all__ = ("TCheckbutton",)


class TCheckbutton(ttkcheckbutton):
    _group_setting = {}
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "command": "",
            "compound": "",
            "cursor": "",
            "image": "",
            "name": None,
            "padding": None,
            "state": "normal",
            "takefocus": None,
            "text": "",
            "textvariable": None,
            "underline": -1,
            "width": "",
            "check": False,
            "group": "default",
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._group = self._default_dict.pop("group", "default")
        variable = BooleanVar(value=False, name=self._group)
        on, off = (0, 1) if self._default_dict.pop("check", False) else (1, 0)
        super().__init__(
            master,
            offvalue=off,
            onvalue=on,
            variable=variable,
            class_="TCheckbutton",
            style="TCheckbutton",
            **self._default_dict,
        )
        if not isinstance(self._group, str):
            self._group = "default"
        if self._group in self._group_setting:
            self._group_setting[self._group].append(self)
        else:
            self._group_setting[self._group] = [self]
