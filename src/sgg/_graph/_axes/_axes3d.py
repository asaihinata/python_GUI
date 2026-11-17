"""
References:
    https://matplotlib.org/stable/api/toolkits/mplot3d/axes3d.html
"""

from matplotlib.scale import ScaleBase

from sgg._constant import _SCALE_TUPLE
from sgg._graph._axes import _AXES

__all__ = ("_AXES3D",)


class _AXES3D(_AXES):
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

    def set_xbound(self, min=None, max=None, view_margin=None):
        self._ax.set_xbound(min, max, view_margin=view_margin)

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

    def set_ybound(self, min=None, max=None, view_margin=None):
        self._ax.set_ybound(min, max, view_margin=view_margin)

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

    def get_zlim(self):
        return self._ax.get_zlim()

    def set_zinverted(self, inverted):
        self._ax.set_zinverted(inverted)

    def get_zinverted(self):
        return self._ax.get_zinverted()

    def invert_zaxis(self):
        ax = self._ax
        ax.set_zinverted(not ax.get_zinverted())

    def set_zbound(self, min=None, max=None, view_margin=None):
        self._ax.set_zbound(min, max, view_margin=view_margin)

    def get_zbound(self):
        return self._ax.get_zbound()

    def set_zlabel(self, label, fontdict=None, labelpad=None, *, loc=None, **kw):
        return self._ax.set_zlabel(label, fontdict, labelpad, loc=loc, **kw)

    def get_zlabel(self):
        return self._ax.get_zlabel()

    def set_zticks(self, ticks, labels=None, *, minor=False, **kw):
        return self._ax.set_zticks(ticks, labels=labels, minor=minor, **kw)

    def get_zticks(self, *, minor=False):
        return self._ax.get_zticks(minor=minor)

    def set_zscale(self, value, **kw):
        if value in _SCALE_TUPLE or isinstance(value, ScaleBase):
            self._ax.set_zscale(value, **kw)

    def get_zscale(self):
        return self._ax.get_zscale()
