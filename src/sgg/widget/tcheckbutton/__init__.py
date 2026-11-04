from tkinter import BooleanVar
from tkinter.ttk import Checkbutton as ttkcheckbutton

from sgg.models import _do_func, _setDefaultValues2

__all__ = ("TCheckbutton",)


class TCheckbutton(ttkcheckbutton):
    _group_setting = {}
    _default_dict = {}
    _count = 0

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "command": None,
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
        variable = BooleanVar(
            value=False, name=f"TCheckbutton_{self._group}_{self._count}"
        )
        TCheckbutton._count = TCheckbutton._count + 1
        command = self._default_dict.pop("command", None)
        super().__init__(
            master,
            onvalue=0,
            offvalue=1,
            variable=variable,
            command=lambda: _do_func(command),
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
