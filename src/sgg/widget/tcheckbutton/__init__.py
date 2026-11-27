from tkinter import BooleanVar
from tkinter.ttk import Checkbutton as ttkcheckbutton

from sgg.models import (_do_func, _setDefaultValues2, _setDefaultValues3,
                        _update_dict)

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
        groupname = self._default_dict["group"]
        if not isinstance(groupname, str):
            groupname = "default"
        self._variable = BooleanVar(
            value=False, name=f"TCheckbutton_{groupname}_{TCheckbutton._count}"
        )
        TCheckbutton._count = TCheckbutton._count + 1
        super().__init__(
            master,
            class_="TCheckbutton",
            style="TCheckbutton",
            variable=self._variable,
            command=lambda x=self._default_dict["command"]: _do_func(x),
            onvalue=True,
            offvalue=False,
            **_setDefaultValues3(self._default_dict, {"variable", "command", "group"}),
        )
        if groupname in self._group_setting:
            self._group_setting[groupname].append(self)
        else:
            self._group_setting[groupname] = [self]

    def __bool__(self):
        return self._variable.get()

    def configure(self, cnf={}, **kw):
        if not cnf and not kw:
            return super().configure()
        self._default_dict = _update_dict(self._default_dict, cnf | kw)
        return super().configure(
            command=lambda x=self._default_dict["command"]: _do_func(x),
            **_setDefaultValues3(self._default_dict, {"variable", "command", "group"}),
        )

    config = configure

    def get(self):
        return self._variable.get()

    def set(self, value):
        if not isinstance(value, bool):
            raise TypeError("値の型が不正です")
        self._variable.set(value=value)
