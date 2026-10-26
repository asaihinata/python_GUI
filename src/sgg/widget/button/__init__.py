from tkinter import Button as tkbutton

from sgg.models import _setDefaultValues2

__all__ = ("Button",)


class Button(tkbutton):
    __dict__ = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls.__dict__ = {
            "activebackground": None,
            "activeforeground": None,
            "anchor": "center",
            "background": None,
            "bd": None,
            "bg": None,
            "bitmap": "",
            "border": None,
            "borderwidth": None,
            "command": "",
            "compound": "none",
            "cursor": "",
            "default": "disabled",
            "disabledforeground": None,
            "fg": None,
            "font": None,
            "foreground": None,
            "height": 0,
            "highlightbackground": None,
            "highlightcolor": None,
            "highlightthickness": 1,
            "image": "",
            "justify": "center",
            "name": None,
            "overrelief": "",
            "padx": None,
            "pady": None,
            "relief": None,
            "repeatdelay": None,
            "repeatinterval": None,
            "state": "normal",
            "takefocus": "",
            "text": "",
            "textvariable": None,
            "underline": -1,
            "width": 0,
            "wraplength": 0,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self.__dict__ = _setDefaultValues2(self.__dict__, cnf, **kw)
        super().__init__(master, self.__dict__)
