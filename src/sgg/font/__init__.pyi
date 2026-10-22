"""フォントを設定するモジュール"""

from pathlib import Path
from tkinter import Misc
from tkinter.font import Font
from typing import Literal, overload

from matplotlib.font_manager import FontProperties

__all__ = ["TKFont"]

type _FontDescription = (
    Font
    | tuple[str, int, Literal["normal", "bold"], Literal["roman", "italic"], bool, bool]
    | tuple[str, int, Literal["normal", "bold"], Literal["roman", "italic"], bool]
    | tuple[str, int, Literal["normal", "bold"], Literal["roman", "italic"]]
    | tuple[str, int, Literal["normal", "bold"]]
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
        weight: Literal["normal", "bold"] = ...,
        slant: Literal["roman", "italic"] = ...,
        underline: bool = ...,
        overstrike: bool = ...,
        name: str | None = None,
    ) -> None: ...
