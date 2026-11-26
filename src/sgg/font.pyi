"""フォントを設定するモジュール"""

from pathlib import Path
from tkinter import Misc
from tkinter.font import Font
from typing import Literal, overload

from matplotlib.font_manager import FontProperties

__all__ = ("TKFont",)
type LITERAL_WEIGHT = Literal["normal", "bold"]
type LITERAL_SLANT = Literal["roman", "italic"]
type _FontDescription = (
    Font
    | TKFont
    | tuple[str, int, LITERAL_WEIGHT, LITERAL_SLANT, bool, bool]
    | tuple[str, int, LITERAL_WEIGHT, LITERAL_SLANT, bool]
    | tuple[str, int, LITERAL_WEIGHT, LITERAL_SLANT]
    | tuple[str, int, LITERAL_WEIGHT]
    | tuple[str, int]
    | tuple[str]
)

class TKFont(Font):
    """フォントを設定するオブジェクト"""

    @overload
    def __init__(
        self,
        root: Misc | None = ...,
        font: _FontDescription | Path | FontProperties = ...,
        name: str | None = None,
    ) -> None: ...
    @overload
    def __init__(
        self,
        root: Misc | None = ...,
        family: str = ...,
        size: int = ...,
        weight: LITERAL_WEIGHT = ...,
        slant: LITERAL_SLANT = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        name: str | None = None,
    ) -> None: ...
