from copy import deepcopy
from tkinter.ttk import Button as ttkbutton

from sgg.dialog.chooser import AskColor
from sgg.models import _delete_keys, _setDefaultValues2

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
        }
        cls._exclusive_dict = {
            "color": None,
            "initialcolor": None,
            "parent": None,
            "title": None,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        def _click_ask():
            kw = deepcopy(self._exclusive_dict)
            color = kw.pop("color")
            self._color = AskColor(color=color, **kw)
            del kw

        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        _default_dict = _delete_keys(self._default_dict, self._exclusive_dict)
        self._color = (None, None)
        super().__init__(
            master,
            command=_click_ask,
            class_="TButton",
            style="TButton",
            **_default_dict,
        )

    def get_color(self):
        return self._color

    def get_rgb(self):
        return self._color[0]

    def get_hex(self):
        return self._color[1]

    def configure(self, cnf={}, **kw):
        if not cnf and not kw:
            return super().configure()
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        return super().configure(_delete_keys(self._default_dict, self._exclusive_dict))

    config = configure
