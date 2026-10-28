from tkinter import BooleanVar
from tkinter import Radiobutton as tkradiobutton

from sgg.models import _setDefaultValues2

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
        self._group = self._default_dict.pop("group", "default")
        if not isinstance(self._group, str):
            self._group = "default"
        if self._group in self._group_setting:
            var = self._group_setting[self._group]
        else:
            var = BooleanVar(value=True, name=self._group)
            self._group_setting[self._group] = var
        super().__init__(master, self._default_dict, variable=var, value=self)
