from tkinter import LabelFrame as tklabelframe

from sgg.models import _setDefaultValues2

__all__ = ("FrameLabel",)


class FrameLabel(tklabelframe):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "background": None,
            "bd": 2,
            "bg": None,
            "border": 2,
            "borderwidth": 2,
            "colormap": "",
            "container": False,
            "cursor": "",
            "fg": None,
            "font": None,
            "foreground": None,
            "height": 0,
            "highlightbackground": None,
            "highlightcolor": None,
            "highlightthickness": 0,
            "labelanchor": "nw",
            "labelwidget": None,
            "name": None,
            "padx": 0,
            "pady": 0,
            "relief": "groove",
            "takefocus": 0,
            "text": "",
            "visual": "",
            "width": 0,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        super().__init__(master, self._default_dict, class_="Labelframe")
