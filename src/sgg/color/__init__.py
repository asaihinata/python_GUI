from re import IGNORECASE, compile, sub

from sgg.color._color_data import _COLOR_DICT

__all__ = ("Color",)

_HEX_RE = compile(r"^#?([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})$")
_FUNC_RE = compile(
    r"^rgba?\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*(?:,\s*(\d*\.?\d+)\s*)?\)$",
    IGNORECASE,
)


class Color:
    __slots__ = ("r", "g", "b", "a")

    def __new__(cls, r, g=None, b=None, a=1.0):
        cls = super().__new__(cls)
        if isinstance(r, str) and g is None and b is None:
            r, g, b, a = cls._parse_text(r)
        for label, value in (("r", r), ("g", g), ("b", b)):
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError(f"{label} は整数で指定してください: {value!r}")
            if not 0 <= value <= 255:
                raise ValueError(f"{label} は 0 - 255 で指定してください: {value}")
        if not 0.0 <= a <= 1.0:
            raise ValueError(f"a は 0.0 - 1.0 で指定してください: {a}")
        cls.r, cls.g, cls.b, cls.a = r, g, b, float(a)
        return cls

    @staticmethod
    def _parse_text(text):
        s = text.strip()
        if s.startswith("#"):
            return Color._parse_hex(s)
        func = _FUNC_RE.match(s)
        if func is not None:
            r, g, b = (int(func.group(i)) for i in (1, 2, 3))
            a = float(func.group(4)) if func.group(4) is not None else 1.0
            return r, g, b, a
        key = sub(r"[\s\-_]", "", s).lower()
        if key == "transparent":
            return 0, 0, 0, 0.0
        hex6 = _COLOR_DICT.get(key)
        if hex6 is not None:
            return Color._parse_hex(hex6)
        if _HEX_RE.match(s):
            return Color._parse_hex(s)
        raise ValueError(f"色として解釈できません: {text!r}")

    @staticmethod
    def _parse_hex(code):
        match = _HEX_RE.match(code.strip())
        if match is None:
            raise ValueError(f"16進数カラーコードの形式が不正です: {code!r}")
        digits = match.group(1)
        if len(digits) in (3, 4):
            digits = "".join(ch * 2 for ch in digits)
        r, g, b = (int(digits[i : i + 2], 16) for i in (0, 2, 4))
        a = int(digits[6:8], 16) / 255 if len(digits) == 8 else 1.0
        return r, g, b, a

    def __repr__(self):
        return f"Color(r={self.r}, g={self.g}, b={self.b}, a={self.a})"

    def __str__(self):
        return self.to_hex()

    def to_rgb(self):
        return (self.r, self.g, self.b)

    def to_rgba(self):
        return (self.r, self.g, self.b, self.a)

    def to_rgb_str(self):
        return f"rgb({self.r}, {self.g}, {self.b})"

    def to_rgba_str(self):
        return f"rgba({self.r}, {self.g}, {self.b}, {round(self.a, 3):g})"

    def to_hex(self, with_alpha=None, upper=False):
        if with_alpha is None:
            with_alpha = self.a < 1.0
        code = f"#{self.r:02x}{self.g:02x}{self.b:02x}"
        if with_alpha:
            code += f"{round(self.a * 255):02x}"
        return code.upper() if upper else code
