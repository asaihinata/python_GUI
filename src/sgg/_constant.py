from types import MappingProxyType

__all__ = (
    "_POLAR_PROPERTY_DICT",
    "_RADAR_PROPERTY_DICT",
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
        "title_fontdict": None,
        "title_loc": "center",
        "title_pad": 6.0,
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
        "title_fontdict": None,
        "title_loc": "center",
        "title_pad": 6.0,
        "value": None,
        "xlabel": None,
        "xlabel_fontdict": None,
        "xlabel_labelpad": 4.0,
        "xlabel_loc": "center",
        "ylabel": None,
        "ylabel_fontdict": None,
        "ylabel_labelpad": 4.0,
        "ylabel_loc": "center",
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
        "title_fontdict": None,
        "title_pad": 6.0,
        "title_loc": "center",
        "xlabel": None,
        "ylabel": None,
        "zlabel": None,
        "xlabel_labelpad": 4.0,
        "xlabel_loc": "center",
        "xlabel_fontdict": None,
        "ylabel_labelpad": 4.0,
        "ylabel_loc": "center",
        "ylabel_fontdict": None,
        "zlabel_labelpad": 4.0,
        "zlabel_fontdict": None,
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
        "title_fontdict": None,
        "title_pad": 6.0,
        "title_loc": "center",
        "xlabel": None,
        "xlabel_fontdict": None,
        "xlabel_labelpad": 4.0,
        "xlabel_loc": "center",
        "ylabel": None,
        "ylabel_fontdict": None,
        "ylabel_labelpad": 4.0,
        "ylabel_loc": "center",
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
