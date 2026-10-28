from pathlib import Path
from tkinter import PhotoImage
from tkinter.ttk import Label as ttklabel

from sgg.models import _setDefaultValues2

__all__ = ("TImage",)


class TImage(ttklabel):
    _default_dict = {}

    def __new__(cls, *args, **kw):
        cls = super().__new__(cls)
        cls._default_dict = {
            "anchor": None,
            "background": "",
            "border": None,
            "borderwidth": None,
            "compound": "",
            "cursor": "",
            "font": None,
            "foreground": "",
            "justify": None,
            "name": None,
            "padding": None,
            "relief": None,
            "state": "normal",
            "takefocus": "",
            "text": "",
            "textvariable": None,
            "underline": -1,
            "width": "",
            "wraplength": None,
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
        super().__init__(
            master, class_="TLabel", style="TLabel", image=image, **self._default_dict
        )
        self.image = image
