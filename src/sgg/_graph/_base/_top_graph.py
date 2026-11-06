from inspect import stack
from pathlib import Path

__all__ = ("_Top_Graph",)


class _Top_Graph:
    def savefig(self, filename, path=None, dpi="figure"):
        if path is None:
            path = stack()[1].filename
        if not isinstance(filename, str):
            raise TypeError("filenameの型が不正です")
        self.fig.savefig(
            Path(path).parent / f"{filename}.png",
            format="png",
            dpi=dpi,
            orientation="portrait",
            bbox_inches="tight",
        )
