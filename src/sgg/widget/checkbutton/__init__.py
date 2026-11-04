from tkinter import BooleanVar
from tkinter import Checkbutton as tkcheckbutton

from sgg.models import _do_func, _setDefaultValues2

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
        self._group = self._default_dict.pop("group", "default")
        command = self._default_dict.pop("command", None)
        variable = BooleanVar(
            value=False, name=f"Checkbutton_{self._group}_{Checkbutton._count}"
        )
        Checkbutton._count = Checkbutton._count + 1
        super().__init__(
            master,
            self._default_dict,
            variable=variable,
            command=lambda: _do_func(command),
            onvalue=0,
            offvalue=1,
        )
        if not isinstance(self._group, str):
            self._group = "default"
        if self._group in self._group_setting:
            self._group_setting[self._group].append(self)
        else:
            self._group_setting[self._group] = [self]
