from functools import partial
from tkinter import Button as tkbutton

from sgg.dialog.saveasfile import AskSaveAsFilename
from sgg.models import _setDefaultValues2

__all__ = ("SaveFileButton",)


class SaveFileButton(tkbutton):
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
            "confirmoverwrite": True,
            "cursor": "",
            "default": "disabled",
            "defaultextension": "",
            "disabledforeground": None,
            "fg": None,
            "filetypes": [("all files", "*")],
            "font": None,
            "foreground": None,
            "height": 0,
            "highlightbackground": None,
            "highlightcolor": None,
            "highlightthickness": 1,
            "image": "",
            "initialdir": None,
            "initialfile": None,
            "justify": "center",
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
            "typevariable": None,
            "underline": -1,
            "width": 0,
            "wraplength": 0,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._path = ""
        super().__init__(
            master,
            self._default_dict,
            command=partial(
                self._click_ask,
                **{
                    i: self._default_dict.pop(i)
                    for i in (
                        "confirmoverwrite",
                        "defaultextension",
                        "filetypes",
                        "initialdir",
                        "initialfile",
                        "parent",
                        "title",
                        "typevariable",
                    )
                },
            ),
        )

    def _click_ask(self, **kw):
        self._path = AskSaveAsFilename(**kw)

    def __str__(self):
        return str(self._path)

    def __fspath__(self):
        return str(self._path)
