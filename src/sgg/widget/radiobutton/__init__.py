from tkinter import BooleanVar
from tkinter import Radiobutton as tkradiobutton

from sgg.models import (_do_func, _setDefaultValues2, _setDefaultValues3,
                        _update_dict)

__all__ = ("Radiobutton",)


class Radiobutton(tkradiobutton):
    _group_setting = {}
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "activebackground": None,
            "activeforeground": None,
            "anchor": "center",
            "background": None,
            "bd": None,
            "bg": None,
            "bitmap": "",
            "border": None,
            "borderwidth": None,
            "command": None,
            "compound": "none",
            "cursor": "",
            "disabledforeground": None,
            "fg": None,
            "font": None,
            "foreground": None,
            "height": 0,
            "highlightbackground": None,
            "highlightcolor": None,
            "highlightthickness": 1,
            "image": "",
            "indicatoron": True,
            "justify": "center",
            "name": None,
            "offrelief": None,
            "overrelief": "",
            "padx": 1,
            "pady": 1,
            "relief": "flat",
            "selectcolor": None,
            "selectimage": "",
            "state": "normal",
            "takefocus": "",
            "text": "",
            "textvariable": None,
            "tristateimage": "",
            "tristatevalue": "",
            "underline": -1,
            "width": 0,
            "wraplength": 0,
            "group": "default",
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        groupname = self._default_dict["group"]
        if not isinstance(groupname, str):
            groupname = "default"
        if groupname in self._group_setting:
            self._variable = self._group_setting[groupname]
        else:
            self._variable = BooleanVar(value=True, name=f"Radio_{groupname}")
            self._group_setting[groupname] = self._variable
        super().__init__(
            master,
            command=lambda x=self._default_dict["command"]: _do_func(x),
            variable=self._variable,
            value=self,
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
