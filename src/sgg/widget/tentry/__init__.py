from tkinter.ttk import Entry as ttkentry

from sgg.models import _setDefaultValues2

__all__ = ("TEntry",)


class TEntry(ttkentry):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "background": None,
            "cursor": None,
            "exportselection": True,
            "font": None,
            "foreground": "",
            "invalidcommand": "",
            "justify": "left",
            "name": None,
            "show": "",
            "state": "normal",
            "takefocus": None,
            "textvariable": None,
            "validate": "none",
            "validatecommand": "",
            "width": 20,
            "xscrollcommand": "",
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        super().__init__(master, class_="TEntry", style="TEntry", **self._default_dict)
