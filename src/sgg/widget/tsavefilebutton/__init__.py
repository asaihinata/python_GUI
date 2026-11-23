from tkinter.ttk import Button as ttkbutton

from sgg._widget.askbtn import _Ask_Path_Btn
from sgg.dialog.saveasfile import AskSaveAsFilename
from sgg.models import _delete_keys, _setDefaultValues2

__all__ = ("TSaveFileButton",)


class TSaveFileButton(_Ask_Path_Btn, ttkbutton):
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
            "confirmoverwrite": True,
            "filetypes": [("all files", "*")],
            "defaultextension": "",
            "initialdir": None,
            "initialfile": None,
            "parent": None,
            "title": None,
            "typevariable": None,
        }
        cls._path = ""
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        def _click_ask(kw):
            self._path = AskSaveAsFilename(**kw)

        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        ttkbutton.__init__(
            master,
            command=lambda: _click_ask(self._exclusive_dict),
            class_="TButton",
            style="TButton",
            **_delete_keys(self._default_dict, self._exclusive_dict),
        )
