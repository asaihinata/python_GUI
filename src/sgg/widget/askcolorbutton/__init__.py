from functools import partial
from tkinter import Button as tkbutton

from sgg.dialog.chooser import AskColor
from sgg.models import _setDefaultValues2

__all__ = ("AskColorButton",)


class AskColorButton(tkbutton):
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
            "color": None,
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
            "initialcolor": None,
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
            "underline": -1,
            "width": 0,
            "wraplength": 0,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self.__dict__ = _setDefaultValues2(self.__dict__, cnf, **kw)
        self._color = (None, None)
        super().__init__(
            master,
            self.__dict__,
            command=partial(
                self._click_ask,
                **{
                    i: self.__dict__.pop(i)
                    for i in ("color", "initialcolor", "parent", "title")
                },
            ),
        )

    def get_color(self):
        return self._color

    def get_rgb(self):
        return self._color[0]

    def get_hex(self):
        return self._color[1]

    def _click_ask(self, **kw):
        color = kw.pop("color")
        self._color = AskColor(color=color, **kw)
