from types import MappingProxyType

from sgg.version import __matplotlib_version_info__

__all__ = (
    "_POLAR_PROPERTY_DICT",
    "_RADAR_PROPERTY_DICT",
    "_SCALE_TUPLE",
    "_THREEDIMENSIONAL_PROPERTY_DICT",
    "_TWODIMENSIONAL_PROPERTY_DICT",
)
_POLAR_PROPERTY_DICT = MappingProxyType(
    {
        "dpi": 100,
        "edgecolor": None,
        "facecolor": None,
        "grid": True,
        "grid_alpha": 0.5,
        "grid_axis": "both",
        "grid_color": "gray",
        "grid_linestyle": "--",
        "grid_linewidth": 0.7,
        "grid_which": "major",
        "theta_direction": True,
        "theta_offset": 0,
        "theta_zero_location_loc": "E",
        "theta_zero_location_offset": 0.0,
        "title": None,
    }
)
"""
    References:
        ### theta_direction,theta_offset
            https://matplotlib.org/stable/api/projections/polar.html
        ### title
            https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html
"""
_RADAR_PROPERTY_DICT = MappingProxyType(
    {
        "dpi": 100,
        "edgecolor": None,
        "facecolor": None,
        "grid": True,
        "grid_alpha": 0.5,
        "grid_axis": "both",
        "grid_color": "gray",
        "grid_linestyle": "--",
        "grid_linewidth": 0.7,
        "grid_which": "major",
        "title": None,
        "value": None,
        "xlabel": None,
        "ylabel": None,
    }
)
"""
    References:
        ### title
            https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html
        ### xlabel,ylabel
            https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html
            https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html
"""
if __matplotlib_version_info__ >= (3, 10):
    _THREEDIMENSIONAL_PROPERTY_DICT = MappingProxyType(
        {
            "axlim_clip": False,
            "dpi": 100,
            "edgecolor": None,
            "facecolor": None,
            "linewidth": 0.0,
            "grid": True,
            "grid_alpha": 0.5,
            "grid_axis": "both",
            "grid_color": "gray",
            "grid_linestyle": "--",
            "grid_linewidth": 0.7,
            "grid_which": "major",
            "title": None,
            "xlabel": None,
            "ylabel": None,
            "zlabel": None,
        }
    )
else:
    _THREEDIMENSIONAL_PROPERTY_DICT = MappingProxyType(
        {
            "dpi": 100,
            "edgecolor": None,
            "facecolor": None,
            "linewidth": 0.0,
            "grid": True,
            "grid_alpha": 0.5,
            "grid_axis": "both",
            "grid_color": "gray",
            "grid_linestyle": "--",
            "grid_linewidth": 0.7,
            "grid_which": "major",
            "title": None,
            "xlabel": None,
            "ylabel": None,
            "zlabel": None,
        }
    )
"""
    References:
        ### title
            https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html
        ### xlabel,ylabel,zlabel
            https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html
            https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html
            https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.set_zlabel.html
"""
_TWODIMENSIONAL_PROPERTY_DICT = MappingProxyType(
    {
        "dpi": 100,
        "edgecolor": None,
        "facecolor": None,
        "grid": True,
        "grid_alpha": 0.5,
        "grid_axis": "both",
        "grid_color": "gray",
        "grid_linestyle": "--",
        "grid_linewidth": 0.7,
        "grid_which": "major",
        "title": None,
        "xlabel": None,
        "ylabel": None,
    }
)
"""
    References:
        ### title
            https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_title.html
        ### xlabel,ylabel
            https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_xlabel.html
            https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.set_ylabel.html
"""
_SCALE_TUPLE = ("asinh", "function", "functionlog", "linear", "log", "logit", "symlog")
"""
    グラフの軸上のデータ値の分布を定義する値の配列

    References:
        https://matplotlib.org/stable/api/scale_api.html
"""
