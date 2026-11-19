from tkinter import BooleanVar
from tkinter import Checkbutton as tkcheckbutton

from sgg.models import _do_func, _setDefaultValues2, _setDefaultValues3

__all__ = ("Checkbutton",)


class Checkbutton(tkcheckbutton):
    _group_setting = {}
    _default_dict = {}
    _count = 0

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
            "group": "default",
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
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        groupname = self._default_dict["group"]
        if not isinstance(groupname, str):
            groupname = "default"
        self._variable = BooleanVar(
            value=False, name=f"Checkbutton_{groupname}_{Checkbutton._count}"
        )
        Checkbutton._count = Checkbutton._count + 1
        super().__init__(
            master,
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

    def get(self):
        return self._variable.get()

    def set(self, value):
        if not isinstance(value, bool):
            raise TypeError("値の型が不正です")
        self._variable.set(value=value)
