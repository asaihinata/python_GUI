from functools import partial
from tkinter.ttk import Button as ttkbutton

from sgg.dialog.saveasfile import AskSaveAsFilename
from sgg.models import _setDefaultValues2

__all__ = ("TSaveFileButton",)


class TSaveFileButton(ttkbutton):
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
            "confirmoverwrite": True,
            "defaultextension": "",
            "filetypes": [("all files", "*")],
            "initialdir": None,
            "initialfile": None,
            "parent": None,
            "title": None,
            "typevariable": None,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._path = ""
        command_ = partial(
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
        )
        super().__init__(
            master,
            command=command_,
            class_="TButton",
            style="TButton",
            **self._default_dict,
        )

    def _click_ask(self, **kw):
        self._path = AskSaveAsFilename(**kw)

    def __fspath__(self):
        return str(self._path)
