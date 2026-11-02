from tkinter import Listbox as tklistbox
from tkinter import Variable

from numpy import ndarray

from sgg.models import _setDefaultValues2, _to_tuple

__all__ = ("Listbox",)


class Listbox(tklistbox):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "activestyle": None,
            "background": None,
            "bd": 1,
            "bg": None,
            "border": 1,
            "borderwidth": 1,
            "cursor": "",
            "disabledforeground": None,
            "exportselection": 1,
            "fg": None,
            "font": None,
            "foreground": None,
            "height": 5,
            "highlightbackground": None,
            "highlightcolor": None,
            "highlightthickness": None,
            "justify": "left",
            "name": None,
            "relief": None,
            "selectbackground": None,
            "selectborderwidth": 0,
            "selectforeground": None,
            "state": "normal",
            "takefocus": "",
            "values": None,
            "width": 20,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        values = self._default_dict.pop("values", None)
        if values is None:
            values = ("",)
        elif isinstance(values, ndarray):
            if values.ndim == 1:
                values = values.tolist()
            else:
                # 次元数が1次元ではない時に例外を発生させる
                raise ValueError
        else:
            values = _to_tuple(values)
        listvariable = Variable(value=values)
        super().__init__(master, self._default_dict, listvariable=listvariable)

    def __len__(self):
        return self.size()

    def __iter__(self):
        return iter(self.get(0, "end"))

    def __contains__(self, items):
        return items in self.get(0, "end")

    def all_items(self):
        return self.get(0, "end")

    def add_height(self, add=1, /):
        if not isinstance(add, int):
            raise TypeError("型が不正です")
        return self.config(height=self.cget("height") + add)

    def max_set_height(self):
        return self.config(height=self.__len__())
