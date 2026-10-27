"""フォントを設定するモジュール"""

from pathlib import Path
from tkinter.font import Font

from matplotlib.font_manager import FontProperties

from sgg.models import _setDefaultValues1

__all__ = ("TKFont",)


class TKFont(Font):
    """フォントを設定するオブジェクト"""

    _default_dict = {
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
            self._default_dict = _setDefaultValues1(self._default_dict, options)
            if isinstance(font, tuple):
                default = ("メイリオ", 12, "normal", "roman", False, False)
                font = font + default[len(font) :]
                for i, key in enumerate(self._default_dict):
                    self._default_dict[key] = font[i]
                super().__init__(root=root, name=name, **self._default_dict)
            else:
                super().__init__(root=root, name=name, **self._default_dict)

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
