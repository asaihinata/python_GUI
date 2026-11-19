from tkinter.ttk import Button as ttkbutton

from sgg.models import _do_func, _setDefaultValues2, _setDefaultValues3

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
        super().__init__(
            master,
            command=lambda x=self._default_dict["command"]: _do_func(x),
            class_="TButton",
            style="TButton",
            **_setDefaultValues3(self._default_dict, {"command"}),
        )
