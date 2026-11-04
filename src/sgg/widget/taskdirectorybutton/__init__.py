from functools import partial
from tkinter.ttk import Button as ttkbutton

from sgg.dialog.opendirectory import AskDirectoryname
from sgg.models import _delete_keys, _setDefaultValues2

__all__ = ("TAskDirectoryButton",)


class TAskDirectoryButton(ttkbutton):
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
            "initialdir": None,
            "mustexist": False,
            "parent": None,
            "title": None,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        def _click_ask(**kw):
            self._path = AskDirectoryname(**kw)

        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        _default_dict = _delete_keys(self._default_dict, self._exclusive_dict)
        self._path = ""
        super().__init__(
            master,
            command=partial(_click_ask, **self._exclusive_dict),
            class_="TButton",
            style="TButton",
            **_default_dict,
        )

    def __fspath__(self):
        return str(self._path)
