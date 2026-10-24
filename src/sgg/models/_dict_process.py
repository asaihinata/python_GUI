"""`辞書型(dict)`についての処理を行うモジュール"""

__all__ = ("_setDefaultValues1", "_setDefaultValues2")


def _setDefaultValues1(default, kw):
    for key in default:
        default[key] = kw.pop(key, default[key])
    return default


def _setDefaultValues2(default, cnf=None, **kw):
    for i in (cnf or {}, kw):
        for key, val in i.items():
            if key in default:
                default[key] = val
    return default
