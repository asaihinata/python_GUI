from tkinter import Frame as tkframe

from sgg.models import _setDefaultValues2

__all__ = ("Frame",)


class Frame(tkframe):
    __dict__ = {
        "background": None,
        "bd": 0,
        "bg": None,
        "border": 0,
        "borderwidth": 0,
        "class_": "Frame",
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

    def __init__(self, master=None, cnf={}, **kw):
        self.__dict__ = _setDefaultValues2(self.__dict__, cnf, **kw)
        super().__init__(master, self.__dict__)
