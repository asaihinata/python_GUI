"""`辞書型(dict)`についての処理を行うモジュール"""

__all__ = ("_delete_keys", "_setDefaultValues1", "_setDefaultValues2", "_update_dict")


def _delete_keys(key1, key2={}):
    common_keys = set(key1.keys()) & set(key2.keys())
    return {k: v for k, v in key1.items() if k not in common_keys}


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


def _update_dict(target, input_dict):
    for k, v in input_dict.items():
        if k in target:
            target[k] = v
    return target
