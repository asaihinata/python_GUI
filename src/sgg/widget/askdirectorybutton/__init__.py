from functools import partial
from tkinter import Button as tkbutton

from sgg.dialog.opendirectory import AskDirectoryname
from sgg.models import _setDefaultValues2

__all__ = ("AskDirectoryButton",)


class AskDirectoryButton(tkbutton):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
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
        cls._exclusive_dict = {
            "initialdir": None,
            "mustexist": False,
            "parent": None,
            "title": None,
        }
        cls._default_dict = cls._exclusive_dict | cls._default_dict
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        def _click_ask(**kw):
            self._path = AskDirectoryname(**kw)

        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        self._path = ""
        super().__init__(
            master,
            self._default_dict,
            command=partial(_click_ask, **self._exclusive_dict),
        )

    def __fspath__(self):
        return str(self._path)
