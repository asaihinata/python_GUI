from tkinter import Frame, Tk

from sgg.models import _setDefaultValues2
from sgg.widget.askcolorbutton import AskColorButton
from sgg.widget.askdirectorybutton import AskDirectoryButton
from sgg.widget.askfilebutton import AskFileButton
from sgg.widget.button import Button
from sgg.widget.label import Label
from sgg.widget.savefilebutton import SaveFileButton

__all__ = ("Window",)


class Window:
    __slots__ = ("__dict__", "_root", "_count", "_key_widget_save")
    __dict__ = {
        "layout": None,
        "title": "window",
    }

    def __init__(self, cnf={}, **kw):
        self._key_widget_save = {}
        self.__dict__ = _setDefaultValues2(self.__dict__, cnf, **kw)
        self._root = Tk()
        self.title = self.__dict__["title"]
        self._win_creat()

    def _win_creat(self):
        layout = self.__dict__["layout"]
        self._count = {"widget": 0}
        if not isinstance(layout, list | tuple):
            raise TypeError("layoutの値が不正です")
        for c, i in enumerate(layout):
            if not isinstance(i, list | tuple):
                raise TypeError("layoutの値が不正です")
            row_frame = Frame(self._root, name=f"layout_row_{c}")
            row_frame.pack(fill="x")
            for j in i:
                type_ = j.get("type", None)
                kw = j.get("kw", {})
                if type_ == "label":
                    widget = Label(row_frame, **kw)
                elif type_ == "Button":
                    widget = Button(row_frame, **kw)
                elif type_ == "AskColorButton":
                    widget = AskColorButton(row_frame, **kw)
                elif type_ == "AskDirectoryButton":
                    widget = AskDirectoryButton(row_frame, **kw)
                elif type_ == "AskFileButton":
                    widget = AskFileButton(row_frame, **kw)
                elif type_ == "SaveFileButton":
                    widget = SaveFileButton(row_frame, **kw)
                else:
                    widget = Label(row_frame, text="ウィジェットが存在しません")
                self._key_set(kw.pop("key", None), widget)
                widget.pack(side="left")

    def _key_set(self, key, widget):
        if key is None or not isinstance(key, str):
            key = "widget"
        if key in self._count:
            self._key_widget_save[f"{key}_{self._count[key]}"] = widget
            self._count[key] = self._count[key] + 1
        else:
            self._count[key] = 0
            self._key_widget_save[key] = widget

    def get_key(self, key):
        return self._key_widget_save.get(key)

    get = get_key

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
