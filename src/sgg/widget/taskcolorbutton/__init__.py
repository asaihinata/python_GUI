from tkinter.ttk import Button as ttkbutton

from sgg._widget.askbtn import _Ask_Color_Btn
from sgg.dialog.chooser import AskColor
from sgg.models import _delete_keys, _setDefaultValues2, _setDefaultValues3

__all__ = ("TAskColorButton",)


class TAskColorButton(ttkbutton, _Ask_Color_Btn):
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
        cls._color = (None, None)
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        def _click_ask(kw):
            self._color = AskColor(
                color=kw["color"], **_setDefaultValues3(kw, {"color"})
            )

        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        super().__init__(
            master,
            command=lambda: _click_ask(self._exclusive_dict),
            class_="TButton",
            style="TButton",
            **_delete_keys(self._default_dict, self._exclusive_dict),
        )
