from functools import partial
from tkinter.ttk import Button as ttkbutton

from sgg.dialog.chooser import AskColor
from sgg.models import _setDefaultValues2

__all__ = ("TAskColorButton",)


class TAskColorButton(ttkbutton):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "compound": "",
            "cursor": "",
            "default": "normal",
            "image": "",
            "name": None,
            "padding": None,
            "state": "normal",
            "takefocus": None,
            "text": "",
            "textvariable": None,
            "underline": -1,
            "width": "",
            "color": None,
            "initialcolor": None,
            "parent": None,
            "title": None,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._color = (None, None)
        command_ = partial(
            self._click_ask,
            **{
                i: self._default_dict.pop(i)
                for i in ("color", "initialcolor", "parent", "title")
            },
        )
        super().__init__(
            master,
            command=command_,
            class_="TButton",
            style="TButton",
            **self._default_dict,
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
