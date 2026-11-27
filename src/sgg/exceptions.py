"""例外を収めたモジュール"""

from numpy.exceptions import AxisError

__all__ = ("ColorError", "VersionError", "FraudAxis")


class ColorError(ValueError):
    """色に関する例外"""

    pass


class VersionError(AttributeError):
    """ライブラリのバージョンが不正の時に発生させる例外"""

    pass


class FraudAxis(AxisError):
    """配列の次元数が不正の時に発生させる例外"""

    pass
