from types import MappingProxyType

__all__ = (
    "_TWODIMENSIONAL_PROPERTY_DICT",
    "_THREEDIMENSIONAL_PROPERTY_DICT",
    "_RADAR_PROPERTY_DICT",
)
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
        "xlabel": None,
        "ylabel": None,
        "value": None,
    }
)
