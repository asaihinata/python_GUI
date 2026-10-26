from tkinter import BooleanVar
from tkinter import Radiobutton as tkradiobutton

from sgg.models import _setDefaultValues2

__all__ = ("Radiobutton",)


class Radiobutton(tkradiobutton):
    _group_setting = {}
    __dict__ = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls.__dict__ = {
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
            "font": "TkDefaultFont",
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
        self.__dict__ = _setDefaultValues2(self.__dict__, cnf, **kw)
        self._group = self.__dict__.pop("group", "default")
        if not isinstance(self._group, str):
            self._group = "default"
        if self._group in self._group_setting:
            var = self._group_setting[self._group]
        else:
            var = BooleanVar(value=True, name=self._group)
            self._group_setting[self._group] = var
        super().__init__(master, self.__dict__, variable=var, value=self)
