"""`辞書型(dict)`についての処理を行うモジュール"""

import copy

__all__ = ("_setDefaultValues1", "_setDefaultValues2")


def _setDefaultValues1(default, kw):
    for key in default:
        default[key] = kw.pop(key, default[key])
    return default


def _setDefaultValues2(default, cnf=None, **kw):
    result = copy.deepcopy(default)
    result.update(cnf or {})
    result.update(kw)
    return result
