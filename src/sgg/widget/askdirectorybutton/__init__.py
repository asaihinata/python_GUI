from tkinter import Button as tkbutton

from sgg._widget.askbtn import _Ask_Directory_Btn
from sgg.dialog.opendirectory import AskDirectoryname
from sgg.models import _delete_keys, _setDefaultValues1

__all__ = ("AskDirectoryButton",)


class AskDirectoryButton(tkbutton, _Ask_Directory_Btn):
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
        cls._path = ""
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        def _click_ask(kw):
            self._path = AskDirectoryname(**kw)

        self._default_dict = _setDefaultValues1(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues1(
            self._exclusive_dict, self._default_dict
        )
        super().__init__(
            master,
            command=lambda: _click_ask(self._exclusive_dict),
            **_delete_keys(self._default_dict, self._exclusive_dict),
        )
