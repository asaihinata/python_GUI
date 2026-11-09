from inspect import stack
from pathlib import Path
from tkinter import Misc

from sgg._graph._base import _Base_Graph

__all__ = ("_Top_Graph",)


class _Top_Graph:
    _last_child_ids = {}
    _master = None
    _widget = None

    def __str__(self):
        return self._name

    def __repr__(self):
        class_ = self.__class__
        return f"<{class_.__module__}.{class_.__qualname__} object {self._name}>"

    @property
    def master(self):
        return self._master

    @master.setter
    def master(self, master):
        if not isinstance(master, Misc):
            raise TypeError
        self._master = master

    @property
    def ax(self):
        return self._ax

    def savefig(self, filename, path=None, dpi="figure"):
        if path is None:
            path = stack()[1].filename
        if not isinstance(filename, str):
            raise TypeError("filenameの型が不正です")
        self.fig.savefig(
            Path(path).parent / f"{filename}.png",
            format="png",
            dpi=dpi,
            orientation="portrait",
            bbox_inches="tight",
        )

    def widget(self, master=None):
        name = self.__class__.__name__.lower()
        if name[-1].isdigit():
            name += "!"
        if self._last_child_ids is None:
            self._last_child_ids = {}
        count = self._last_child_ids.get(name, 0) + 1
        self._last_child_ids[name] = count
        name = f"!{name}" if count == 1 else f"!{name}{count}"
        self._name = "." + name if master._w == "." else master._w + "." + name
        self._widget = _Base_Graph.__new__(self, master=master, figure=self.fig)
        self._canvas = self._widget.get_tk_widget()
        return self._canvas

    def configure(self, cnf=None, **kw):
        return self._canvas.configure(cnf=cnf, **kw)

    config = configure

    def _redraw(self):
        if self._widget is not None:
            self._widget.draw()

    def _clear(self):
        self._ax.clear()

    def _update(self, kw):
        for k, v in kw.items():
            self._default_dict[k] = v
