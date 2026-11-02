from functools import partial
from tkinter.ttk import Button as ttkbutton

from sgg.dialog.openfile import AskOpenFilename
from sgg.models import _setDefaultValues2

__all__ = ("TAskFileButton",)


class TAskFileButton(ttkbutton):
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
            "defaultextension": "",
            "filetypes": [("all files", "*")],
            "initialdir": None,
            "initialfile": None,
            "parent": None,
            "typevariable": None,
            "title": None,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        def _click_ask(**kw):
            self._path = AskOpenFilename(**kw)

        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        self._path = ""
        super().__init__(
            master,
            command=partial(_click_ask, **self._exclusive_dict),
            class_="TButton",
            style="TButton",
            **self._default_dict,
        )

    def __fspath__(self):
        return str(self._path)
