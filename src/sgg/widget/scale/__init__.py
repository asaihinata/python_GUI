from tkinter import Scale as tkscale

from sgg.models import _setDefaultValues2

__all__ = ("Scale",)


class Scale(tkscale):
    __dict__ = {
        "activebackground": None,
        "background": None,
        "bd": 1,
        "bg": None,
        "bigincrement": 0.0,
        "border": 1,
        "borderwidth": 1,
        "command": "",
        "cursor": "",
        "digits": 0,
        "fg": None,
        "font": None,
        "foreground": None,
        "from_": 0.0,
        "highlightbackground": None,
        "highlightcolor": None,
        "highlightthickness": None,
        "label": "",
        "length": 100,
        "name": None,
        "orient": "horizontal",
        "relief": "flat",
        "repeatdelay": 300,
        "repeatinterval": 100,
        "resolution": 1.0,
        "showvalue": True,
        "sliderlength": 30,
        "sliderrelief": "raised",
        "state": "normal",
        "takefocus": "",
        "tickinterval": 0.0,
        "to": 100.0,
        "troughcolor": None,
        "variable": None,
        "width": 15,
    }

    def __init__(self, master=None, cnf={}, **kw):
        self.__dict__ = _setDefaultValues2(self.__dict__, cnf, **kw)
        super().__init__(master, self.__dict__)
