from tkinter import BooleanVar
from tkinter.ttk import Radiobutton as ttkradiobutton

from sgg.models import _setDefaultValues2

__all__ = ("TRadiobutton",)


class TRadiobutton(ttkradiobutton):
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
            "group": "default",
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._group = self._default_dict.pop("group", "default")
        if not isinstance(self._group, str):
            self._group = "default"
        if self._group in self._group_setting:
            var = self._group_setting[self._group]
        else:
            var = BooleanVar(value=True, name=self._group)
            self._group_setting[self._group] = var
        super().__init__(
            master,
            variable=var,
            value=self,
            class_="TRadiobutton",
            style="TRadiobutton",
            **self._default_dict,
        )
