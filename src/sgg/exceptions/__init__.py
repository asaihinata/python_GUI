"""例外を収めたモジュール"""

__all__ = ("ColorError", "VersionError")


class ColorError(ValueError):
    """色に関する例外"""

    pass


class VersionError(AttributeError):
    """ライブラリのバージョンが不正の時に発生させる例外"""

    pass
