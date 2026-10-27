from tkinter import Frame as tkframe
from tkinter import Tk, Wm

from sgg.models import _setDefaultValues2
from sgg.widget.askcolorbutton import AskColorButton
from sgg.widget.askdirectorybutton import AskDirectoryButton
from sgg.widget.askfilebutton import AskFileButton
from sgg.widget.button import Button
from sgg.widget.checkbutton import Checkbutton
from sgg.widget.entry import Entry
from sgg.widget.frame import Frame
from sgg.widget.framelabel import FrameLabel
from sgg.widget.label import Label
from sgg.widget.listbox import Listbox
from sgg.widget.menu import Menu
from sgg.widget.radiobutton import Radiobutton
from sgg.widget.savefilebutton import SaveFileButton
from sgg.widget.scale import Scale
from sgg.widget.spinbox import Spinbox
from sgg.widget.text import Text

__all__ = ("Window",)


class Window(Wm):
    _default_dict = {
        "alpha": 1.0,
        "layout": None,
        "title": "window"
    }

    def __init__(self, cnf={}, **kw):
        self._key_widget_save = {}
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._root = Tk()
        self._count = {"widget": 0}
        self.title = self._default_dict["title"]
        self.alpha = self._default_dict["alpha"]
        self._win_creat(self._root, self._default_dict["layout"])

    def _win_creat(self, root, layout):
        if layout is None:
            return
        elif not isinstance(layout, list | tuple):
            raise TypeError("layoutの値が不正です")
        for c, i in enumerate(layout):
            if not isinstance(i, list | tuple):
                raise TypeError("layoutの値が不正です")
            row_frame = tkframe(root, name=f"layout_row_{c}")
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
                elif type_ == "Checkbutton":
                    widget = Checkbutton(row_frame, **kw)
                elif type_ == "Radiobutton":
                    widget = Radiobutton(row_frame, **kw)
                elif type_ == "Scale":
                    widget = Scale(row_frame, **kw)
                elif type_ == "Listbox":
                    widget = Listbox(row_frame, **kw)
                elif type_ == "Text":
                    widget = Text(row_frame, **kw)
                elif type_ == "Entry":
                    widget = Entry(row_frame, **kw)
                elif type_ == "Spinbox":
                    widget = Spinbox(row_frame, **kw)
                elif type_ == "Menu":
                    widget = Menu(row_frame, **kw)
                elif type_ == "Frame":
                    layout = kw.pop("layout", None)
                    widget = Frame(row_frame, **kw)
                    self._win_creat(widget, layout)
                elif type_ == "FrameLabel":
                    layout = kw.pop("layout", None)
                    widget = FrameLabel(row_frame, **kw)
                    self._win_creat(widget, layout)
                else:
                    widget = Label(row_frame, text="ウィジェットが存在しません")
                self._key_set(kw.pop("key", None), widget)
                if type_ == "Menu":
                    self._root.config(menu=widget)
                else:
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
    def root(self):
        return self._root

    @property
    def title(self):
        return self._default_dict["title"]

    @title.setter
    def title(self, title):
        self._default_dict["title"] = title
        self._root.title(title)

    @property
    def alpha(self):
        return self._default_dict["alpha"]

    @alpha.setter
    def alpha(self, alpha):
        if not isinstance(alpha, int | float | bool):
            raise TypeError("alphaの型が不正です")
        elif isinstance(alpha, bool):
            alpha = int(alpha)
        if not 0 <= alpha <= 1:
            raise ValueError("alphaの値が不正です")
        self._default_dict["alpha"] = alpha
        self._root.attributes("-alpha", alpha)

    def cget(self, key):
        return self.root.cget(key)

    def keys(self):
        return self.root.keys()
