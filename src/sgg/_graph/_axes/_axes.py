"""
References:
    https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.html
    https://matplotlib.org/stable/api/ticker_api.html
"""

from matplotlib.axes import Axes
from matplotlib.scale import ScaleBase
from matplotlib.ticker import (AutoLocator, FuncFormatter, LogLocator,
                               MaxNLocator, NullFormatter, NullLocator,
                               PercentFormatter, ScalarFormatter,
                               StrMethodFormatter)

from sgg._constant import _SCALE_TUPLE

__all__ = ("_AXES",)


class _AXES:
    # axis
    _ax: Axes

    @property
    def ax(self) -> Axes:
        return self._ax

    # x軸
    def set_xlim(
        self, min=None, max=None, *, emit=True, auto=False, xmin=None, xmax=None
    ):
        self._ax.set_xlim(min, max, emit=emit, auto=auto, xmin=xmin, xmax=xmax)
        self._redraw()

    def get_xlim(self):
        return self._ax.get_xlim()

    def set_xinverted(self, inverted):
        self._ax.set_xinverted(inverted)
        self._redraw()

    def get_xinverted(self):
        return self._ax.get_xinverted()

    def invert_xaxis(self):
        ax = self._ax
        ax.set_xinverted(not ax.get_xinverted())
        self._redraw()

    def set_xbound(self, min=None, max=None):
        self._ax.set_xbound(min, max)
        self._redraw()

    def get_xbound(self):
        return self._ax.get_xbound()

    def set_xlabel(self, label, fontdict=None, labelpad=None, *, loc=None, **kw):
        self._ax.set_xlabel(label, fontdict, labelpad, loc=loc, **kw)
        self._redraw()

    def get_xlabel(self):
        return self._ax.get_xlabel()

    def set_xticks(self, ticks, labels=None, *, minor=False, **kw):
        self._ax.set_xticks(ticks, labels=labels, minor=minor, **kw)
        self._redraw()

    def get_xticks(self, *, minor=False):
        return self._ax.get_xticks(minor=minor)

    def set_xscale(self, value, **kw):
        if value in _SCALE_TUPLE or isinstance(value, ScaleBase):
            self._ax.set_xscale(value, **kw)
            self._redraw()

    def get_xscale(self):
        return self._ax.get_xscale()

    def xmajor_setlocator(
        self,
        nbins=10,
        steps=None,
        integer=False,
        symmetric=False,
        prune=None,
        min_n_ticks=2,
    ):
        self._ax.xaxis.set_major_locator(
            MaxNLocator(
                nbins,
                steps=steps,
                integer=integer,
                symmetric=symmetric,
                prune=prune,
                min_n_ticks=min_n_ticks,
            )
        )
        self._redraw()

    def xmajor_auto(self):
        self._ax.xaxis.set_major_locator(AutoLocator())
        self._redraw()

    def xmajor_setlog(self, base=10.0, subs=(1.0,), numticks=None):
        if not isinstance(base, int | float):
            raise TypeError("baseの型が不正です")
        elif base < 0:
            raise ValueError("baseの値が不正です")
        self._ax.xaxis.set_major_locator(LogLocator(base, subs, numticks=numticks))
        self._redraw()

    def xmajor_hide(self):
        self._ax.xaxis.set_major_locator(NullLocator())
        self._redraw()

    def xmajor_strformat(self, format):
        self._ax.xaxis.set_major_formatter(StrMethodFormatter(format))
        self._redraw()

    def xmajor_percentformat(self, xmax=100, decimals=None, symbol="%", is_latex=False):
        self._ax.xaxis.set_major_formatter(
            PercentFormatter(xmax, decimals, symbol, is_latex)
        )
        self._redraw()

    def xmajor_funcformat(self, func):
        self._ax.xaxis.set_major_formatter(FuncFormatter(func))
        self._redraw()

    def xmajor_scalarformat(
        self, useOffset=None, useMathText=None, useLocale=None, usetex=None
    ):
        self._ax.xaxis.set_major_formatter(
            ScalarFormatter(useOffset, useMathText, useLocale, usetex=usetex)
        )
        self._redraw()

    def xmajor_hideformat(self):
        self._ax.xaxis.set_major_formatter(NullFormatter())
        self._redraw()

    def xminor_setlocator(
        self,
        nbins=10,
        steps=None,
        integer=False,
        symmetric=False,
        prune=None,
        min_n_ticks=2,
    ):
        self._ax.xaxis.set_minor_locator(
            MaxNLocator(
                nbins,
                steps=steps,
                integer=integer,
                symmetric=symmetric,
                prune=prune,
                min_n_ticks=min_n_ticks,
            )
        )
        self._redraw()

    def xminor_auto(self):
        self._ax.xaxis.set_minor_locator(AutoLocator())
        self._redraw()

    def xminor_setlog(self, base=10.0, subs=(1.0,), numticks=None):
        if not isinstance(base, int | float):
            raise TypeError("baseの型が不正です")
        elif base < 0:
            raise ValueError("baseの値が不正です")
        self._ax.xaxis.set_minor_locator(LogLocator(base, subs, numticks=numticks))
        self._redraw()

    def xminor_hide(self):
        self._ax.xaxis.set_minor_locator(NullLocator())
        self._redraw()

    def xminor_strformat(self, format):
        self._ax.xaxis.set_minor_formatter(StrMethodFormatter(format))
        self._redraw()

    def xminor_percentformat(self, xmax=100, decimals=None, symbol="%", is_latex=False):
        self._ax.xaxis.set_minor_formatter(
            PercentFormatter(xmax, decimals, symbol, is_latex)
        )
        self._redraw()

    def xminor_funcformat(self, func):
        self._ax.xaxis.set_minor_formatter(FuncFormatter(func))
        self._redraw()

    def xminor_scalarformat(
        self, useOffset=None, useMathText=None, useLocale=None, usetex=None
    ):
        self._ax.xaxis.set_minor_formatter(
            ScalarFormatter(useOffset, useMathText, useLocale, usetex=usetex)
        )
        self._redraw()

    def xminor_hideformat(self):
        self._ax.xaxis.set_minor_formatter(NullFormatter())
        self._redraw()

    # y軸
    def set_ylim(
        self, min=None, max=None, *, emit=True, auto=False, ymin=None, ymax=None
    ):
        self._ax.set_ylim(min, max, emit=emit, auto=auto, ymin=ymin, ymax=ymax)
        self._redraw()

    def get_ylim(self):
        return self._ax.get_ylim()

    def set_yinverted(self, inverted):
        self._ax.set_yinverted(inverted)
        self._redraw()

    def get_yinverted(self):
        return self._ax.get_yinverted()

    def invert_yaxis(self):
        ax = self._ax
        ax.set_yinverted(not ax.get_yinverted())
        self._redraw()

    def set_ybound(self, min=None, max=None):
        self._ax.set_ybound(min, max)
        self._redraw()

    def get_ybound(self):
        return self._ax.get_ybound()

    def set_ylabel(self, label, fontdict=None, labelpad=None, *, loc=None, **kw):
        self._ax.set_ylabel(label, fontdict, labelpad, loc=loc, **kw)
        self._redraw()

    def get_ylabel(self):
        return self._ax.get_ylabel()

    def set_yticks(self, ticks, labels=None, *, minor=False, **kw):
        self._ax.set_yticks(ticks, labels=labels, minor=minor, **kw)
        self._redraw()

    def get_yticks(self, *, minor=False):
        return self._ax.get_yticks(minor=minor)

    def set_yscale(self, value, **kw):
        if value in _SCALE_TUPLE or isinstance(value, ScaleBase):
            self._ax.set_yscale(value, **kw)
            self._redraw()

    def get_yscale(self):
        return self._ax.get_yscale()

    def ymajor_setlocator(
        self,
        nbins=10,
        steps=None,
        integer=False,
        symmetric=False,
        prune=None,
        min_n_ticks=2,
    ):
        self._ax.yaxis.set_major_locator(
            MaxNLocator(
                nbins,
                steps=steps,
                integer=integer,
                symmetric=symmetric,
                prune=prune,
                min_n_ticks=min_n_ticks,
            )
        )
        self._redraw()

    def ymajor_auto(self):
        self._ax.yaxis.set_major_locator(AutoLocator())
        self._redraw()

    def ymajor_setlog(self, base=10.0, subs=(1.0,), numticks=None):
        if not isinstance(base, int | float):
            raise TypeError("baseの型が不正です")
        elif base < 0:
            raise ValueError("baseの値が不正です")
        self._ax.yaxis.set_major_locator(LogLocator(base, subs, numticks=numticks))
        self._redraw()

    def ymajor_hide(self):
        self._ax.yaxis.set_major_locator(NullLocator())
        self._redraw()

    def ymajor_strformat(self, format):
        self._ax.yaxis.set_major_formatter(StrMethodFormatter(format))
        self._redraw()

    def ymajor_percentformat(self, xmax=100, decimals=None, symbol="%", is_latex=False):
        self._ax.yaxis.set_major_formatter(
            PercentFormatter(xmax, decimals, symbol, is_latex)
        )
        self._redraw()

    def ymajor_funcformat(self, func):
        self._ax.yaxis.set_major_formatter(FuncFormatter(func))
        self._redraw()

    def ymajor_scalarformat(
        self, useOffset=None, useMathText=None, useLocale=None, usetex=None
    ):
        self._ax.yaxis.set_major_formatter(
            ScalarFormatter(useOffset, useMathText, useLocale, usetex=usetex)
        )
        self._redraw()

    def ymajor_hideformat(self):
        self._ax.yaxis.set_major_formatter(NullFormatter())
        self._redraw()

    def yminor_setlocator(
        self,
        nbins=10,
        steps=None,
        integer=False,
        symmetric=False,
        prune=None,
        min_n_ticks=2,
    ):
        self._ax.yaxis.set_minor_locator(
            MaxNLocator(
                nbins,
                steps=steps,
                integer=integer,
                symmetric=symmetric,
                prune=prune,
                min_n_ticks=min_n_ticks,
            )
        )
        self._redraw()

    def yminor_auto(self):
        self._ax.yaxis.set_minor_locator(AutoLocator())
        self._redraw()

    def yminor_setlog(self, base=10.0, subs=(1.0,), numticks=None):
        if not isinstance(base, int | float):
            raise TypeError("baseの型が不正です")
        elif base < 0:
            raise ValueError("baseの値が不正です")
        self._ax.yaxis.set_minor_locator(LogLocator(base, subs, numticks=numticks))
        self._redraw()

    def yminor_hide(self):
        self._ax.yaxis.set_minor_locator(NullLocator())
        self._redraw()

    def yminor_strformat(self, format):
        self._ax.yaxis.set_minor_formatter(StrMethodFormatter(format))
        self._redraw()

    def yminor_percentformat(self, xmax=100, decimals=None, symbol="%", is_latex=False):
        self._ax.yaxis.set_minor_formatter(
            PercentFormatter(xmax, decimals, symbol, is_latex)
        )
        self._redraw()

    def yminor_funcformat(self, func):
        self._ax.yaxis.set_minor_formatter(FuncFormatter(func))
        self._redraw()

    def yminor_scalarformat(
        self, useOffset=None, useMathText=None, useLocale=None, usetex=None
    ):
        self._ax.yaxis.set_minor_formatter(
            ScalarFormatter(useOffset, useMathText, useLocale, usetex=usetex)
        )
        self._redraw()

    def yminor_hideformat(self):
        self._ax.yaxis.set_minor_formatter(NullFormatter())
        self._redraw()
