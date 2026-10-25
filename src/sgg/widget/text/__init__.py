from tkinter import Text as tktext

from sgg.models import _setDefaultValues2

__all__ = ("Text",)


class Text(tktext):
    __dict__ = {
        "autoseparators": True,
        "background": None,
        "bd": None,
        "bg": None,
        "blockcursor": False,
        "border": None,
        "borderwidth": None,
        "cursor": "xterm",
        "endline": "",
        "exportselection": True,
        "fg": None,
        "font": None,
        "foreground": None,
        "height": 5,
        "highlightbackground": None,
        "highlightcolor": None,
        "highlightthickness": None,
        "inactiveselectbackground": None,
        "insertbackground": None,
        "insertborderwidth": 0,
        "insertofftime": 300,
        "insertontime": 600,
        "insertunfocussed": "none",
        "insertwidth": None,
        "maxundo": 0,
        "name": None,
        "padx": 1,
        "pady": 1,
        "relief": None,
        "selectbackground": None,
        "selectborderwidth": None,
        "selectforeground": None,
        "setgrid": False,
        "spacing1": 0,
        "spacing2": 0,
        "spacing3": 0,
        "startline": "",
        "state": "normal",
        "tabs": "",
        "tabstyle": "tabular",
        "takefocus": "",
        "text": None,
        "undo": False,
        "width": 40,
        "wrap": "char",
        "xscrollcommand": "",
        "yscrollcommand": "",
    }

    def __init__(self, master=None, cnf={}, **kw):
        self.__dict__ = _setDefaultValues2(self.__dict__, cnf, **kw)
        text = self.__dict__.pop("text", "")
        super().__init__(master, self.__dict__)
        if isinstance(text, str):
            self.insert("1.0", text)
