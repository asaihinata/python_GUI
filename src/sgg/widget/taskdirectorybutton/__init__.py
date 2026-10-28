from functools import partial
from tkinter.ttk import Button as ttkbutton

from sgg.dialog.opendirectory import AskDirectoryname
from sgg.models import _setDefaultValues2

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
            "initialdir": None,
            "mustexist": False,
            "parent": None,
            "title": None,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._path = ""
        command_ = partial(
            self._click_ask,
            **{
                i: self._default_dict.pop(i)
                for i in ("initialdir", "mustexist", "parent", "title")
            },
        )
        super().__init__(
            master,
            command=command_,
            class_="TButton",
            style="TButton",
            **self._default_dict,
        )

    def _click_ask(self, **kw):
        self._path = AskDirectoryname(**kw)

    def __fspath__(self):
        return str(self._path)
