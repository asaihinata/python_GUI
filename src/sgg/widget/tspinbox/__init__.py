from tkinter.ttk import Spinbox as ttkspinbox

from sgg.models import _do_func, _setDefaultValues2, _setDefaultValues3

__all__ = ("TSpinbox",)


class TSpinbox(ttkspinbox):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "background": None,
            "command": None,
            "cursor": "",
            "exportselection": None,
            "font": None,
            "foreground": None,
            "format": "",
            "from_": 0.0,
            "increment": 1.0,
            "invalidcommand": None,
            "justify": None,
            "name": None,
            "show": None,
            "state": "normal",
            "takefocus": None,
            "textvariable": None,
            "to": 100.0,
            "validate": "none",
            "validatecommand": "",
            "values": None,
            "width": None,
            "wrap": False,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        super().__init__(
            master,
            command=lambda x=self._default_dict["command"]: _do_func(x),
            class_="TSpinbox",
            style="TSpinbox",
            **_setDefaultValues3(self._default_dict, {"command"}),
        )
