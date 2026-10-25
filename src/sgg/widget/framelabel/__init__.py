from tkinter import LabelFrame as Fml

from sgg.models import _setDefaultValues2

__all__ = ("FrameLabel",)


class FrameLabel(Fml):
    __dict__ = {
        "background": None,
        "bd": 2,
        "bg": None,
        "border": 2,
        "borderwidth": 2,
        "class_": "Labelframe",
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

    def __init__(self, master=None, cnf={}, **kw):
        self.__dict__ = _setDefaultValues2(self.__dict__, cnf, **kw)
        super().__init__(master, self.__dict__)
