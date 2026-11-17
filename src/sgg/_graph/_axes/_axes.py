"""
References:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html
"""

from matplotlib.scale import ScaleBase

from sgg._constant import _SCALE_TUPLE

__all__ = ("_AXES",)


class _AXES:
    # x軸
    def set_xlim(
        self, min=None, max=None, *, emit=True, auto=False, xmin=None, xmax=None
    ):
        self._ax.set_xlim(min, max, emit=emit, auto=auto, xmin=xmin, xmax=xmax)

    def get_xlim(self):
        return self._ax.get_xlim()

    def set_xinverted(self, inverted):
        self._ax.set_xinverted(inverted)

    def get_xinverted(self):
        return self._ax.get_xinverted()

    def invert_xaxis(self):
        ax = self._ax
        ax.set_xinverted(not ax.get_xinverted())

    def set_xbound(self, min=None, max=None):
        self._ax.set_xbound(min, max)

    def get_xbound(self):
        return self._ax.get_xbound()

    def set_xlabel(self, label, fontdict=None, labelpad=None, *, loc=None, **kw):
        return self._ax.set_xlabel(label, fontdict, labelpad, loc=loc, **kw)

    def get_xlabel(self):
        return self._ax.get_xlabel()

    def set_xticks(self, ticks, labels=None, *, minor=False, **kw):
        return self._ax.set_xticks(ticks, labels=labels, minor=minor, **kw)

    def get_xticks(self, *, minor=False):
        return self._ax.get_xticks(minor=minor)

    def set_xscale(self, value, **kw):
        if value in _SCALE_TUPLE or isinstance(value, ScaleBase):
            self._ax.set_xscale(value, **kw)

    def get_xscale(self):
        return self._ax.get_xscale()

    # y軸
    def set_ylim(
        self, min=None, max=None, *, emit=True, auto=False, ymin=None, ymax=None
    ):
        self._ax.set_ylim(min, max, emit=emit, auto=auto, ymin=ymin, ymax=ymax)

    def get_ylim(self):
        return self._ax.get_ylim()

    def set_yinverted(self, inverted):
        self._ax.set_yinverted(inverted)

    def get_yinverted(self):
        return self._ax.get_yinverted()

    def invert_yaxis(self):
        ax = self._ax
        ax.set_yinverted(not ax.get_yinverted())

    def set_ybound(self, min=None, max=None):
        self._ax.set_ybound(min, max)

    def get_ybound(self):
        return self._ax.get_ybound()

    def set_ylabel(self, label, fontdict=None, labelpad=None, *, loc=None, **kw):
        return self._ax.set_ylabel(label, fontdict, labelpad, loc=loc, **kw)

    def get_ylabel(self):
        return self._ax.get_ylabel()

    def set_yticks(self, ticks, labels=None, *, minor=False, **kw):
        return self._ax.set_yticks(ticks, labels=labels, minor=minor, **kw)

    def get_yticks(self, *, minor=False):
        return self._ax.get_yticks(minor=minor)

    def set_yscale(self, value, **kw):
        if value in _SCALE_TUPLE or isinstance(value, ScaleBase):
            self._ax.set_yscale(value, **kw)

    def get_yscale(self):
        return self._ax.get_yscale()

    # axis
    def get_title(self, loc="center"):
        if not loc.lower() in ("left", "center", "right"):
            loc = "center"
        return self._ax.get_title(loc)

    def set_title(self, label, fontdict=None, loc=None, pad=None, *, y=None, **kw):
        return self._ax.set_title(label, fontdict, loc, pad, y=y, **kw)
