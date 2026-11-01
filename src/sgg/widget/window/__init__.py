from tkinter import Canvas
from tkinter import Frame as tkframe
from tkinter import Tk, Wm
from tkinter.ttk import Scrollbar

from sgg._graph._base import _Top_Graph
from sgg.models import _setDefaultValues2
from sgg.widget.askcolorbutton import AskColorButton
from sgg.widget.askdirectorybutton import AskDirectoryButton
from sgg.widget.askfilebutton import AskFileButton
from sgg.widget.bar import Bar
from sgg.widget.barh import Barh
from sgg.widget.boxplot import Boxplot
from sgg.widget.button import Button
from sgg.widget.checkbutton import Checkbutton
from sgg.widget.ecdf import Ecdf
from sgg.widget.entry import Entry
from sgg.widget.errorbar import Errorbar
from sgg.widget.eventplot import Eventplot
from sgg.widget.fill_between import Fill_Between
from sgg.widget.frame import Frame
from sgg.widget.framelabel import FrameLabel
from sgg.widget.hexbin import Hexbin
from sgg.widget.hist import Hist
from sgg.widget.hist2d import Hist2D
from sgg.widget.image import Image
from sgg.widget.label import Label
from sgg.widget.listbox import Listbox
from sgg.widget.menu import Menu
from sgg.widget.pie import Pie
from sgg.widget.plot import Plot
from sgg.widget.radiobutton import Radiobutton
from sgg.widget.savefilebutton import SaveFileButton
from sgg.widget.scale import Scale
from sgg.widget.scatter import Scatter
from sgg.widget.spinbox import Spinbox
from sgg.widget.stackplot import Stackplot
from sgg.widget.stairs import Stairs
from sgg.widget.stem import Stem
from sgg.widget.taskcolorbutton import TAskColorButton
from sgg.widget.taskdirectorybutton import TAskDirectoryButton
from sgg.widget.taskfilebutton import TAskFileButton
from sgg.widget.tbutton import TButton
from sgg.widget.tcheckbutton import TCheckbutton
from sgg.widget.tentry import TEntry
from sgg.widget.text import Text
from sgg.widget.tframe import TFrame
from sgg.widget.tframelabel import TFrameLabel
from sgg.widget.timage import TImage
from sgg.widget.tlabel import TLabel
from sgg.widget.tnotebook import TNotebook
from sgg.widget.tprogressbar import TProgressbar
from sgg.widget.tradiobutton import TRadiobutton
from sgg.widget.tsavefilebutton import TSaveFileButton
from sgg.widget.tscale import TScale
from sgg.widget.tspinbox import TSpinbox
from sgg.widget.violinplot import Violinplot

__all__ = ("Window",)


class Window(Wm):
    _default_dict = {
        "alpha": 1.0,
        "layout": None,
        "title": "window",
        "scroll": False,
        "scroll_x": False,
        "scroll_y": False,
    }

    def __init__(self, cnf={}, **kw):
        self._key_widget_save = {}
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._root = Tk()
        self._count = {"widget": 0}
        self._scroll_canvas = None
        parent = self._root
        self.title = self._default_dict["title"]
        self.alpha = self._default_dict["alpha"]
        scroll = self._default_dict["scroll"]
        if scroll:
            scroll_x, scroll_y = True, True
        else:
            scroll_x = self._default_dict["scroll_x"]
            scroll_y = self._default_dict["scroll_y"]
        if scroll_x or scroll_y:
            parent = self._setup_scroll(scroll_x, scroll_y)
        self._win_creat(parent, self._default_dict["layout"])
        if self._scroll_canvas is not None:
            self._fit_canvas_to_content(parent)

    def _setup_scroll(self, scroll_x, scroll_y):
        canvas = Canvas(self._root, highlightthickness=0)
        inner = tkframe(canvas)
        win_id = canvas.create_window((0, 0), window=inner, anchor="nw")
        self._scroll_canvas = canvas

        def _update_scroll(e=None):
            req_w = inner.winfo_reqwidth()
            req_h = inner.winfo_reqheight()
            cvs_w = canvas.winfo_width()
            cvs_h = canvas.winfo_height()
            if scroll_x:
                w = max(req_w, cvs_w)
            else:
                w = cvs_w if cvs_w > 1 else req_w
            if scroll_y:
                h = max(req_h, cvs_h)
            else:
                h = cvs_h if cvs_h > 1 else req_h
            canvas.itemconfigure(win_id, width=w, height=h)
            canvas.configure(scrollregion=(0, 0, w, h))

        inner.bind("<Configure>", _update_scroll)
        canvas.bind("<Configure>", _update_scroll)
        if scroll_y:
            ybar = Scrollbar(self._root, orient="vertical", command=canvas.yview)
            canvas.configure(yscrollcommand=ybar.set)
            ybar.pack(side="right", fill="y")
        if scroll_x:
            xbar = Scrollbar(self._root, orient="horizontal", command=canvas.xview)
            canvas.configure(xscrollcommand=xbar.set)
            xbar.pack(side="bottom", fill="x")
        canvas.pack(fill="both", expand=True)
        return inner

    def _fit_canvas_to_content(self, inner):
        self._root.update_idletasks()
        max_w = self._root.winfo_screenwidth() - 100
        max_h = self._root.winfo_screenheight() - 150
        self._scroll_canvas.configure(
            width=min(inner.winfo_reqwidth(), max_w),
            height=min(inner.winfo_reqheight(), max_h),
        )

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
                elif type_ == "Image":
                    widget = Image(row_frame, **kw)
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
                elif type_ == "TLabel":
                    widget = TLabel(row_frame, **kw)
                elif type_ == "TImage":
                    widget = TImage(row_frame, **kw)
                elif type_ == "TButton":
                    widget = TButton(row_frame, **kw)
                elif type_ == "TAskColorButton":
                    widget = TAskColorButton(row_frame, **kw)
                elif type_ == "TAskDirectoryButton":
                    widget = TAskDirectoryButton(row_frame, **kw)
                elif type_ == "TAskFileButton":
                    widget = TAskFileButton(row_frame, **kw)
                elif type_ == "TSaveFileButton":
                    widget = TSaveFileButton(row_frame, **kw)
                elif type_ == "TCheckbutton":
                    widget = TCheckbutton(row_frame, **kw)
                elif type_ == "TRadiobutton":
                    widget = TRadiobutton(row_frame, **kw)
                elif type_ == "TEntry":
                    widget = TEntry(row_frame, **kw)
                elif type_ == "TSpinbox":
                    widget = TSpinbox(row_frame, **kw)
                elif type_ == "TScale":
                    widget = TScale(row_frame, **kw)
                elif type_ == "TProgressbar":
                    widget = TProgressbar(row_frame, **kw)
                elif type_ == "TFrame":
                    layout = kw.pop("layout", None)
                    widget = TFrame(row_frame, **kw)
                    self._win_creat(widget, layout)
                elif type_ == "TFrameLabel":
                    layout = kw.pop("layout", None)
                    widget = TFrameLabel(row_frame, **kw)
                    self._win_creat(widget, layout)
                elif type_ == "TNotebook":
                    tabs = kw.pop("tab", None)
                    widget = TNotebook(row_frame, **kw)
                    for tab in tabs:
                        if not isinstance(tab, dict):
                            raise TypeError
                        frame = Frame(widget)
                        widget.add(frame, text=tab.get("tabname", ""))
                        self._win_creat(frame, tab.get("layout", None))
                elif type_ == "Plot":
                    widget = Plot(**kw)
                elif type_ == "Bar":
                    widget = Bar(**kw)
                elif type_ == "Barh":
                    widget = Barh(**kw)
                elif type_ == "Scatter":
                    widget = Scatter(**kw)
                elif type_ == "Stem":
                    widget = Stem(**kw)
                elif type_ == "Stackplot":
                    widget = Stackplot(**kw)
                elif type_ == "Stairs":
                    widget = Stairs(**kw)
                elif type_ == "Fill_Between":
                    widget = Fill_Between(**kw)
                elif type_ == "Hist":
                    widget = Hist(**kw)
                elif type_ == "Boxplot":
                    widget = Boxplot(**kw)
                elif type_ == "Errorbar":
                    widget = Errorbar(**kw)
                elif type_ == "Violinplot":
                    widget = Violinplot(**kw)
                elif type_ == "Eventplot":
                    widget = Eventplot(**kw)
                elif type_ == "Hist2D":
                    widget = Hist2D(**kw)
                elif type_ == "Hexbin":
                    widget = Hexbin(**kw)
                elif type_ == "Pie":
                    widget = Pie(**kw)
                elif type_ == "Ecdf":
                    widget = Ecdf(**kw)
                else:
                    widget = Label(row_frame, text="ウィジェットが存在しません")
                self._key_set(kw.pop("key", None), widget)
                if isinstance(widget, Menu):
                    self._root.config(menu=widget)
                elif isinstance(widget, _Top_Graph):
                    widget.widget(row_frame).pack(side="left")
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

    def widget_key_namelist(self):
        return self._key_widget_save

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
        return self._root.cget(key)

    def keys(self):
        return self._root.keys()

    def configure(self, cnf=None, **kw):
        if cnf is None and not kw:
            return self._root.configure()
        self._root.configure(cnf, **kw)
        cnf = {
            i: self._root.cget(i)
            for i in self._root.keys()
            if i
            in (
                "background",
                "bd",
                "bg",
                "border",
                "borderwidth",
                "cursor",
                "height",
                "highlightbackground",
                "highlightcolor",
                "highlightthickness",
                "padx",
                "pady",
                "relief",
                "takefocus",
                "width",
            )
        }
        for child in self._root.winfo_children():
            if isinstance(child, tkframe):
                child.config(cnf)

    config = configure
