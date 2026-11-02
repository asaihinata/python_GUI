from tkinter.ttk import Button as ttkbutton

from sgg.models import _do_func, _setDefaultValues2

__all__ = ("TButton",)


class TButton(ttkbutton):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "command": None,
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
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        command = self._default_dict.pop("command", None)
        super().__init__(
            master,
            command=lambda: _do_func(command),
            class_="TButton",
            style="TButton",
            **self._default_dict,
        )
