from tkinter import Checkbutton as tkcheckbutton

from sgg.models import _setDefaultValues2

__all__ = ("Checkbutton",)


class Checkbutton(tkcheckbutton):
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
            "check": False,
            "group": "default",
            "command": "",
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
            "offvalue": 0,
            "onvalue": 1,
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
            "variable": None,
            "width": 0,
            "wraplength": 0,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        check = self._default_dict.pop("check", False)
        self._group = self._default_dict.pop("group", "default")
        super().__init__(master, self._default_dict)
        if check:
            self.select()
        if not isinstance(self._group, str):
            self._group = "default"
        if self._group in self._group_setting:
            self._group_setting[self._group].append(self)
        else:
            self._group_setting[self._group] = [self]
