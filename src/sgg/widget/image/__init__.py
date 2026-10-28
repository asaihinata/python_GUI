from pathlib import Path
from tkinter import Label as tklabel
from tkinter import PhotoImage

from sgg.models import _setDefaultValues2

__all__ = ("Image",)


class Image(tklabel):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "activebackground": None,
            "activeforeground": None,
            "anchor": "center",
            "background": None,
            "bd": None,
            "bg": None,
            "bitmap": "",
            "border": None,
            "borderwidth": None,
            "compound": "none",
            "cursor": "",
            "disabledforeground": None,
            "fg": None,
            "font": None,
            "foreground": None,
            "height": 0,
            "highlightbackground": None,
            "highlightcolor": None,
            "highlightthickness": 0,
            "justify": "center",
            "name": None,
            "padx": 1,
            "pady": 1,
            "relief": "flat",
            "state": "normal",
            "takefocus": 0,
            "text": "",
            "textvariable": None,
            "underline": -1,
            "width": 0,
            "wraplength": 0,
            "file": None,
        }
        return cls

    def __init__(self, master=None, cnf={}, **kw):
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        file = self._default_dict.pop("file")
        if not isinstance(file, str | Path):
            raise TypeError(f"{file}が不正の値です")
        elif isinstance(file, str):
            file = Path(file)
        if not file.exists():
            raise FileNotFoundError("パスが存在しません")
        elif file.is_dir():
            raise ValueError("フォルダは指定できません")
        elif file.suffix.lower() not in (".pgm", ".ppm", ".gif", ".png"):
            raise ValueError(f"{file.suffix}は対応していない拡張子です")
        image = PhotoImage(file=file)
        super().__init__(master, self._default_dict, image=image)
        self.image = image
