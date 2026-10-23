"""フォントを設定するモジュール"""

from pathlib import Path
from tkinter.font import Font

from matplotlib.font_manager import FontProperties

from sgg.models import _setDefaultValues1

__all__ = ["TKFont"]


class TKFont(Font):
    """フォントを設定するオブジェクト"""

    __dict__ = {
        "family": "メイリオ",
        "size": 12,
        "weight": "normal",
        "slant": "roman",
        "underline": False,
        "overstrike": False,
    }

    def __init__(self, root=None, font=None, name=None, **options):
        if isinstance(font, FontProperties):
            self._set_font(root, font, name)
        elif isinstance(font, Path):
            self._set_font(root, FontProperties(fname=font), name)
        elif isinstance(font, Font):
            super().__init__(root=root, font=font, name=name)
        else:
            self.__dict__ = _setDefaultValues1(self.__dict__, options)
            if isinstance(font, tuple):
                default = ("メイリオ", 12, "normal", "roman", False, False)
                font = font + default[len(font) :]
                for i, key in enumerate(self.__dict__):
                    self.__dict__[key] = font[i]
                super().__init__(root=root, name=name, **self.__dict__)
            else:
                super().__init__(root=root, name=name, **self.__dict__)

    def _set_font(self, root, font, name):
        super().__init__(
            root=root,
            font=(
                font.get_family()[0],
                int(font.get_size()),
                font.get_weight(),
                "italic" if font.get_style() in ("italic", "oblique") else "roman",
            ),
            name=name,
        )
