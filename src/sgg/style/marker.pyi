"""
マーカーのスタイルを設定するモジュール

References:
    https://matplotlib.org/stable/api/markers_api.html
"""

from matplotlib.markers import MarkerStyle
from matplotlib.path import Path
from matplotlib.transforms import Transform
from matplotlib.typing import CapStyleType, FillStyleType, JoinStyleType
from numpy.typing import ArrayLike

__all__ = ("Marker",)

class Marker(MarkerStyle):
    def __init__(
        self,
        marker: str | ArrayLike | Path | MarkerStyle | Marker,
        fillstyle: FillStyleType | None = ...,
        transform: Transform | None = ...,
        capstyle: CapStyleType | None = ...,
        joinstyle: JoinStyleType | None = ...,
    ):
        """マーカーの種類を表すオブジェクト"""
