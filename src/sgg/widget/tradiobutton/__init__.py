from tkinter import BooleanVar
from tkinter.ttk import Radiobutton as ttkradiobutton

from sgg.models import (_do_func, _setDefaultValues2, _setDefaultValues3,
                        _update_dict)

__all__ = ("TRadiobutton",)


class TRadiobutton(ttkradiobutton):
    _group_setting = {}
    _default_dict = {}

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
        if groupname in self._group_setting:
            var = self._group_setting[groupname]
        else:
            var = BooleanVar(value=True, name=f"TRadio_{groupname}")
            self._group_setting[groupname] = var
        super().__init__(
            master,
            variable=var,
            value=self,
            command=lambda x=self._default_dict["command"]: _do_func(x),
            class_="TRadiobutton",
            style="TRadiobutton",
            **_setDefaultValues3(
                self._default_dict, {"command", "group", "value", "variable"}
            ),
        )

    def configure(self, cnf={}, **kw):
        if not cnf and not kw:
            return super().configure()
        self._default_dict = _update_dict(self._default_dict, cnf | kw)
        return super().configure(
            command=lambda x=self._default_dict["command"]: _do_func(x),
            **_setDefaultValues3(
                self._default_dict, {"command", "group", "value", "variable"}
            ),
        )

    config = configure
