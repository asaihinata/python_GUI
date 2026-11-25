"""
References:
    https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html
"""

from matplotlib.scale import ScaleBase
from matplotlib.ticker import (AutoLocator, FuncFormatter, LogLocator,
                               MaxNLocator, NullFormatter, NullLocator,
                               PercentFormatter, ScalarFormatter,
                               StrMethodFormatter)
from mpl_toolkits.mplot3d import Axes3D

from sgg._constant import _SCALE_TUPLE
from sgg._graph._axes import _AXES

__all__ = ("_AXES3D",)


class _AXES3D(_AXES):
    # axis
    _ax: Axes3D

    @property
    def ax(self) -> Axes3D:
        return self._ax

    # x軸
    def set_xlim(
        self,
        min=None,
        max=None,
        *,
        emit=True,
        auto=False,
        view_margin=None,
        xmin=None,
        xmax=None,
    ):
        self._ax.set_xlim(
            min,
            max,
            emit=emit,
            auto=auto,
            view_margin=view_margin,
            xmin=xmin,
            xmax=xmax,
        )
        self._redraw()

    def set_xbound(self, min=None, max=None, view_margin=None):
        self._ax.set_xbound(min, max, view_margin=view_margin)
        self._redraw()

    # y軸
    def set_ylim(
        self,
        min=None,
        max=None,
        *,
        emit=True,
        auto=False,
        view_margin=None,
        ymin=None,
        ymax=None,
    ):
        self._ax.set_ylim(
            min,
            max,
            emit=emit,
            auto=auto,
            view_margin=view_margin,
            ymin=ymin,
            ymax=ymax,
        )
        self._redraw()

    def set_ybound(self, min=None, max=None, view_margin=None):
        self._ax.set_ybound(min, max, view_margin=view_margin)
        self._redraw()

    # z軸
    def set_zlim(
        self,
        min=None,
        max=None,
        *,
        emit=True,
        auto=False,
        view_margin=None,
        zmin=None,
        zmax=None,
    ):
        self._ax.set_zlim(
            min,
            max,
            emit=emit,
            auto=auto,
            view_margin=view_margin,
            zmin=zmin,
            zmax=zmax,
        )
        self._redraw()

    def get_zlim(self):
        return self._ax.get_zlim()

    def set_zinverted(self, inverted):
        self._ax.set_zinverted(inverted)
        self._redraw()

    def get_zinverted(self):
        return self._ax.get_zinverted()

    def invert_zaxis(self):
        ax = self._ax
        ax.set_zinverted(not ax.get_zinverted())
        self._redraw()

    def set_zbound(self, min=None, max=None, view_margin=None):
        self._ax.set_zbound(min, max, view_margin=view_margin)
        self._redraw()

    def get_zbound(self):
        return self._ax.get_zbound()

    def set_zlabel(self, label, fontdict=None, labelpad=None, *, loc=None, **kw):
        self._ax.set_zlabel(label, fontdict, labelpad, loc=loc, **kw)
        self._redraw()

    def get_zlabel(self):
        return self._ax.get_zlabel()

    def set_zticks(self, ticks, labels=None, *, minor=False, **kw):
        self._ax.set_zticks(ticks, labels=labels, minor=minor, **kw)
        self._redraw()

    def get_zticks(self, *, minor=False):
        return self._ax.get_zticks(minor=minor)

    def set_zscale(self, value, **kw):
        if value in _SCALE_TUPLE or isinstance(value, ScaleBase):
            self._ax.set_zscale(value, **kw)
            self._redraw()

    def get_zscale(self):
        return self._ax.get_zscale()

    def zmajor_setlocator(
        self,
        nbins=10,
        steps=None,
        integer=False,
        symmetric=False,
        prune=None,
        min_n_ticks=2,
    ):
        self._ax.zaxis.set_major_locator(
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

    def zmajor_auto(self):
        self._ax.zaxis.set_major_locator(AutoLocator())
        self._redraw()

    def zmajor_setlog(self, base=10.0, subs=(1.0,), numticks=None):
        if not isinstance(base, int | float):
            raise TypeError("baseの型が不正です")
        elif base < 0:
            raise ValueError("baseの値が不正です")
        self._ax.zaxis.set_major_locator(LogLocator(base, subs, numticks=numticks))
        self._redraw()

    def zmajor_hide(self):
        self._ax.zaxis.set_major_locator(NullLocator())
        self._redraw()

    def zmajor_strformat(self, format):
        self._ax.zaxis.set_major_formatter(StrMethodFormatter(format))
        self._redraw()

    def zmajor_percentformat(self, xmax=100, decimals=None, symbol="%", is_latex=False):
        self._ax.zaxis.set_major_formatter(
            PercentFormatter(xmax, decimals, symbol, is_latex)
        )
        self._redraw()

    def zmajor_funcformat(self, func):
        self._ax.zaxis.set_major_formatter(FuncFormatter(func))
        self._redraw()

    def zmajor_scalarformat(
        self, useOffset=None, useMathText=None, useLocale=None, usetex=None
    ):
        self._ax.zaxis.set_major_formatter(
            ScalarFormatter(useOffset, useMathText, useLocale, usetex=usetex)
        )
        self._redraw()

    def zmajor_hideformat(self):
        self._ax.zaxis.set_major_formatter(NullFormatter())
        self._redraw()

    def zminor_setlocator(
        self,
        nbins=10,
        steps=None,
        integer=False,
        symmetric=False,
        prune=None,
        min_n_ticks=2,
    ):
        self._ax.zaxis.set_minor_locator(
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

    def zminor_auto(self):
        self._ax.zaxis.set_minor_locator(AutoLocator())
        self._redraw()

    def zminor_setlog(self, base=10.0, subs=(1.0,), numticks=None):
        if not isinstance(base, int | float):
            raise TypeError("baseの型が不正です")
        elif base < 0:
            raise ValueError("baseの値が不正です")
        self._ax.zaxis.set_minor_locator(LogLocator(base, subs, numticks=numticks))
        self._redraw()

    def zminor_hide(self):
        self._ax.zaxis.set_minor_locator(NullLocator())
        self._redraw()

    def zminor_strformat(self, format):
        self._ax.zaxis.set_minor_formatter(StrMethodFormatter(format))
        self._redraw()

    def zminor_percentformat(self, xmax=100, decimals=None, symbol="%", is_latex=False):
        self._ax.zaxis.set_minor_formatter(
            PercentFormatter(xmax, decimals, symbol, is_latex)
        )
        self._redraw()

    def zminor_funcformat(self, func):
        self._ax.zaxis.set_minor_formatter(FuncFormatter(func))
        self._redraw()

    def zminor_scalarformat(
        self, useOffset=None, useMathText=None, useLocale=None, usetex=None
    ):
        self._ax.zaxis.set_minor_formatter(
            ScalarFormatter(useOffset, useMathText, useLocale, usetex=usetex)
        )
        self._redraw()

    def zminor_hideformat(self):
        self._ax.zaxis.set_minor_formatter(NullFormatter())
        self._redraw()
