from tkinter import Entry as tkentry

from sgg.models import _setDefaultValues2

__all__ = ("Entry",)


class Entry(tkentry):
    __dict__ = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls.__dict__ = {
            "background": None,
            "bd": None,
            "bg": None,
            "border": None,
            "borderwidth": None,
            "cursor": "xterm",
            "disabledbackground": None,
            "disabledforeground": None,
            "exportselection": True,
            "fg": None,
            "font": None,
            "foreground": None,
            "highlightbackground": None,
            "highlightcolor": None,
            "highlightthickness": None,
            "insertbackground": None,
            "insertborderwidth": 0,
            "insertofftime": 300,
            "insertontime": 600,
            "insertwidth": None,
            "invalidcommand": "",
            "invcmd": "",
            "justify": "left",
            "name": None,
            "readonlybackground": None,
            "relief": "sunken",
            "selectbackground": None,
            "selectborderwidth": None,
            "selectforeground": None,
            "show": "",
            "state": "normal",
            "takefocus": "",
            "textvariable": None,
            "validate": "none",
            "validatecommand": "",
            "vcmd": "",
            "width": 20,
            "xscrollcommand": "",
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self.__dict__ = _setDefaultValues2(self.__dict__, cnf, **kw)
        super().__init__(master, self.__dict__)
