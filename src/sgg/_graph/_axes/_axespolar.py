"""
References:
    https://matplotlib.org/stable/api/projections/polar.html#matplotlib.projections.polar.PolarAxes
"""

from matplotlib.projections.polar import PolarAxes

from sgg._graph._axes import _AXES

__all__ = ("_AXESPOLAR",)


class _AXESPOLAR(_AXES):
    # axis
    _ax: PolarAxes

    @property
    def ax(self) -> PolarAxes:
        return self._ax

    # x軸
    def get_xaxis_transform(self, which="grid"):
        return self._ax.get_xaxis_transform(which)

    # y軸
    def get_yaxis_transform(self, which="grid"):
        return self._ax.get_yaxis_transform(which)

    # axes
    def set_thetamax(self, thetamax):
        self._ax.set_thetamax(thetamax)
        self._redraw()

    def get_thetamax(self):
        return self._ax.get_thetamax()

    def set_thetamin(self, thetamin):
        self._ax.set_thetamin(thetamin)
        self._redraw()

    def get_thetamin(self):
        return self._ax.get_thetamin()

    def set_rmax(self, rmax):
        self._ax.set_rmax(rmax)
        self._redraw()

    def get_rmax(self):
        return self._ax.get_rmax()

    def set_rmin(self, rmin):
        self._ax.set_rmin(rmin)
        self._redraw()

    def get_rmin(self):
        return self._ax.get_rmin()

    def set_theta_direction(self, direction):
        self._ax.set_theta_direction(direction)
        self._redraw()

    def set_theta_offset(self, offset):
        self._ax.set_theta_offset(offset)
        self._redraw()

    def set_theta_zero_location(self, loc, offset=0):
        self._ax.set_theta_zero_location(loc, offset)
        self._redraw()

    def set_thetagrids(self, angles, labels=None, fmt=None, **kwargs):
        self._ax.set_thetagrids(angles, labels=labels, fmt=fmt, **kwargs)
        self._redraw()
