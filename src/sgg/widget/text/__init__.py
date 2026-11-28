from tkinter import Text as tktext

from numpy import ndarray

from sgg.models import _setDefaultValues1, _setDefaultValues2

__all__ = ("Text",)


class Text(tktext):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
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
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues1(self._default_dict, cnf, **kw)
        super().__init__(master, **_setDefaultValues2(self._default_dict, {"text"}))
        text = self._default_dict["text"]
        if isinstance(text, list | tuple | range | ndarray):
            for i in reversed(text):
                self.insert("1.0", i)
        else:
            self.insert("1.0", text)

    def all_clear(self):
        self.delete("1.0", "end")

    def all_get(self):
        return self.get("1.0", "end")

    def numberlines(self):
        return int(self.index("end-1c").split(".")[0])
