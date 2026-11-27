from tkinter import Button as tkbutton

from sgg.models import (_do_func, _setDefaultValues2, _setDefaultValues3,
                        _update_dict)

__all__ = ("Button",)


class Button(tkbutton):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "activebackground": None,
            "activeforeground": None,
            "anchor": "center",
            "background": None,
            "bd": None,
            "bg": None,
            "bitmap": "",
            "border": None,
            "borderwidth": None,
            "command": None,
            "compound": "none",
            "cursor": "",
            "default": "disabled",
            "disabledforeground": None,
            "fg": None,
            "font": None,
            "foreground": None,
            "height": 0,
            "highlightbackground": None,
            "highlightcolor": None,
            "highlightthickness": 1,
            "image": "",
            "justify": "center",
            "name": None,
            "overrelief": "",
            "padx": None,
            "pady": None,
            "relief": None,
            "repeatdelay": None,
            "repeatinterval": None,
            "state": "normal",
            "takefocus": "",
            "text": "",
            "textvariable": None,
            "underline": -1,
            "width": 0,
            "wraplength": 0,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        super().__init__(
            master,
            command=lambda x=self._default_dict["command"]: _do_func(x),
            **_setDefaultValues3(self._default_dict, {"command"}),
        )

    def configure(self, cnf={}, **kw):
        if not cnf and not kw:
            return super().configure()
        self._default_dict = _update_dict(self._default_dict, cnf | kw)
        return super().configure(
            command=lambda x=self._default_dict["command"]: _do_func(x),
            **_setDefaultValues3(self._default_dict, {"command"}),
        )

    config = configure
