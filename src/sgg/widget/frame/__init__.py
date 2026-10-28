from tkinter import Frame as tkframe

from sgg.models import _setDefaultValues2

__all__ = ("Frame",)


class Frame(tkframe):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "background": None,
            "bd": 0,
            "bg": None,
            "border": 0,
            "borderwidth": 0,
            "colormap": "",
            "container": False,
            "cursor": "",
            "height": 0,
            "highlightbackground": None,
            "highlightcolor": None,
            "highlightthickness": 0,
            "name": None,
            "padx": 0,
            "pady": 0,
            "relief": "flat",
            "takefocus": 0,
            "visual": "",
            "width": 0,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        super().__init__(master, self._default_dict, class_="Frame")
