from tkinter import Spinbox as tkspinbox

from sgg.models import _setDefaultValues2

__all__ = ("Spinbox",)


class Spinbox(tkspinbox):
    __dict__ = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls.__dict__ = {
            "activebackground": None,
            "background": None,
            "bd": None,
            "bg": None,
            "border": None,
            "borderwidth": None,
            "buttonbackground": None,
            "buttoncursor": "",
            "buttondownrelief": None,
            "buttonuprelief": None,
            "command": "",
            "cursor": "xterm",
            "disabledbackground": None,
            "disabledforeground": None,
            "exportselection": True,
            "fg": None,
            "font": None,
            "foreground": None,
            "format": "",
            "from_": 100.0,
            "highlightbackground": None,
            "highlightcolor": None,
            "highlightthickness": None,
            "increment": 1.0,
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
            "repeatdelay": 400,
            "repeatinterval": 100,
            "selectbackground": None,
            "selectborderwidth": None,
            "selectforeground": None,
            "state": "normal",
            "takefocus": "",
            "textvariable": None,
            "to": 0.0,
            "validate": "none",
            "validatecommand": "",
            "vcmd": "",
            "values": None,
            "width": 20,
            "wrap": False,
            "xscrollcommand": "",
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self.__dict__ = _setDefaultValues2(self.__dict__, cnf, **kw)
        super().__init__(master, self.__dict__)
