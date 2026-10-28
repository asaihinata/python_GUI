from tkinter.ttk import Label as ttklabel

from sgg.models import _setDefaultValues2

__all__ = ("TLabel",)


class TLabel(ttklabel):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "anchor": None,
            "background": "",
            "border": None,
            "borderwidth": None,
            "compound": "",
            "cursor": "",
            "font": None,
            "foreground": "",
            "image": "",
            "justify": None,
            "name": None,
            "padding": None,
            "relief": None,
            "state": "normal",
            "takefocus": "",
            "text": "",
            "textvariable": None,
            "underline": -1,
            "width": "",
            "wraplength": None,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        super().__init__(master, class_="TLabel", style="TLabel", **self._default_dict)
