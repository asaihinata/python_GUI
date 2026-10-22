"""`辞書型(dict)`についての処理を行うモジュール"""

__all__ = ("_setDefaultValues",)


def _setDefaultValues(default, kw):
    for key in default:
        default[key] = kw.pop(key, default[key])
    return default
