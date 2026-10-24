from tkinter import Tk

from sgg.models import _setDefaultValues2
from sgg.widget.button import Button
from sgg.widget.label import Label

__all__ = ("Window",)


class Window:
    __dict__ = {
        "title": "window",
        "layout": None,
    }
    _key_widget_save = {}

    def __init__(self, cnf={}, **kw):
        self.__dict__ = _setDefaultValues2(self.__dict__, cnf, **kw)
        self._root = Tk()
        self.title = self.__dict__["title"]
        self._win_creat()

    def _win_creat(self):
        layout = self.__dict__["layout"]
        self._count = {"widget": 0}
        if not isinstance(layout, list | tuple):
            raise TypeError("layoutの値が不正です")
        for i in layout:
            if not isinstance(i, list | tuple):
                raise TypeError("layoutの値が不正です")
            for j in i:
                type_ = j.get("type", None)
                kw = j.get("kw", {})
                if type_ == "label":
                    widget = Label(self._root, **kw)
                elif type_ == "Button":
                    widget = Button(self._root, **kw)
                else:
                    widget = Label(self._root, text="ウィジェットが存在しません")
                self._key_set(kw.pop("key", None), widget)
                widget.pack()

    def _key_set(self, key, widget):
        if key is None or not isinstance(key, str):
            key = "widget"
        if key in self._count:
            self._key_widget_save[f"{key}_{self._count[key]}"] = widget
            self._count[key] = self._count[key] + 1
        else:
            self._count[key] = 0
            self._key_widget_save[key] = widget

    def run(self, n=0):
        self._root.mainloop(n=n)

    @property
    def title(self):
        return self.__dict__["title"]

    @title.setter
    def title(self, title):
        self.__dict__["title"] = title
        self._root.title(title)

    def resizable(self, width=None, height=None):
        return self._root.resizable(width, height)

    def maxsize(self, width=None, height=None):
        return self._root.maxsize(width, height)

    def minsize(self, width=None, height=None):
        return self._root.minsize(width, height)
