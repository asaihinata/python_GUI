from tkinter.ttk import Frame as ttkframe

from sgg.models import _setDefaultValues2

__all__ = ("TFrame",)


class TFrame(ttkframe):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "border": None,
            "borderwidth": None,
            "cursor": "",
            "height": 0,
            "name": None,
            "padding": None,
            "relief": None,
            "takefocus": "",
            "width": 0,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        super().__init__(master, style="TFrame", class_="TFrame", **self._default_dict)
