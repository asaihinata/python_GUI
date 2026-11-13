"""
マーカーのスタイルを設定するモジュール

References:
    https://matplotlib.org/stable/api/markers_api.html
"""

from matplotlib.markers import MarkerStyle

__all__ = ("Marker",)


class Marker(MarkerStyle):
    def __init__(
        self, marker, fillstyle=None, transform=None, capstyle=None, joinstyle=None
    ):
        super().__init__(
            marker,
            fillstyle=fillstyle,
            transform=transform,
            capstyle=capstyle,
            joinstyle=joinstyle,
        )
