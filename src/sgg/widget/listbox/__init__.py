from tkinter import Listbox as tklistbox

from sgg.models import _setDefaultValues2

__all__ = ("Listbox",)


class Listbox(tklistbox):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "activestyle": None,
            "background": None,
            "bd": 1,
            "bg": None,
            "border": 1,
            "borderwidth": 1,
            "cursor": "",
            "disabledforeground": None,
            "exportselection": 1,
            "fg": None,
            "font": None,
            "foreground": None,
            "height": 10,
            "highlightbackground": None,
            "highlightcolor": None,
            "highlightthickness": None,
            "justify": "left",
            "list": None,
            "listvariable": None,
            "name": None,
            "relief": None,
            "selectbackground": None,
            "selectborderwidth": 0,
            "selectforeground": None,
            "state": "normal",
            "takefocus": "",
            "width": 20,
            "xscrollcommand": "",
            "yscrollcommand": "",
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        list_ = self._default_dict.pop("list")
        super().__init__(master, self._default_dict)
        if isinstance(list_, list | tuple | range):
            self.insert("end", *list_)
