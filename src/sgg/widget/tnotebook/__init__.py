from tkinter.ttk import Notebook as ttknotebook

from sgg.models import _setDefaultValues2

__all__ = ("TNotebook",)


class TNotebook(ttknotebook):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "cursor": "",
            "height": 0,
            "name": None,
            "padding": None,
            "takefocus": None,
            "width": 0,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        super().__init__(
            master, class_="TNotebook", style="TNotebook", **self._default_dict
        )
