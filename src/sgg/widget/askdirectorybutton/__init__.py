from functools import partial
from tkinter import Button as tkbutton

from sgg.dialog.opendirectory import AskDirectoryname
from sgg.models import _setDefaultValues2

__all__ = ("AskDirectoryButton",)


class AskDirectoryButton(tkbutton):
    __dict__ = {
        "activebackground": None,
        "activeforeground": None,
        "anchor": "center",
        "background": None,
        "bd": None,
        "bg": None,
        "bitmap": "",
        "border": None,
        "borderwidth": None,
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
        "initialdir": None,
        "justify": "center",
        "mustexist": False,
        "name": None,
        "overrelief": "",
        "padx": None,
        "pady": None,
        "parent": None,
        "relief": None,
        "repeatdelay": None,
        "repeatinterval": None,
        "state": "normal",
        "takefocus": "",
        "text": "",
        "textvariable": None,
        "title": None,
        "underline": -1,
        "width": 0,
        "wraplength": 0,
    }

    def __init__(self, master=None, cnf={}, **kw):
        self.__dict__ = _setDefaultValues2(self.__dict__, cnf, **kw)
        self._path = ""
        super().__init__(
            master,
            self.__dict__,
            command=partial(
                self._click_ask,
                **{
                    i: self.__dict__.pop(i)
                    for i in ("initialdir", "mustexist", "parent", "title")
                },
            ),
        )

    def _click_ask(self, **kw):
        self._path = AskDirectoryname(**kw)

    def __str__(self):
        return str(self._path)

    def __fspath__(self):
        return str(self._path)
