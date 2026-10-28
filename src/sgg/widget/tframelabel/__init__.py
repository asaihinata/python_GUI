from tkinter.ttk import LabelFrame as ttklabelframe

from sgg.models import _setDefaultValues2

__all__ = ("TFrameLabel",)


class TFrameLabel(ttklabelframe):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "border": None,
            "borderwidth": None,
            "cursor": "",
            "height": 0,
            "labelanchor": None,
            "labelwidget": None,
            "name": None,
            "padding": None,
            "relief": None,
            "takefocus": "",
            "text": "",
            "underline": -1,
            "width": 0,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        super().__init__(
            master, class_="TLabelframe", style="TLabelframe", **self._default_dict
        )
