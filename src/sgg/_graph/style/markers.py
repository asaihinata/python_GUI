from matplotlib.markers import MarkerStyle

__all__ = ("Marker",)


class Marker(MarkerStyle):
    def __init__(
        self, marker, fillstyle=None, transform=None, capstyle=None, joinstyle=None
    ):
        if marker is None:
            marker = "none"
        super().__init__(marker, fillstyle, transform, capstyle, joinstyle)
