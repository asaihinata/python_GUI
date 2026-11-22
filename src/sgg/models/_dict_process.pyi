"""`辞書型(dict)`についての処理を行うモジュール"""

from typing import Any

__all__ = (
    "_delete_keys",
    "_setDefaultValues1",
    "_setDefaultValues2",
    "_setDefaultValues3",
    "_update_dict",
)

def _delete_keys(key1: dict, key2: dict = {}) -> dict: ...
def _setDefaultValues1(default: dict, kw: dict) -> dict: ...
def _setDefaultValues2(default: dict, cnf: dict | None = None, **kw: Any) -> dict: ...
def _setDefaultValues3(default: dict, removedict: set) -> dict: ...
def _update_dict(target: dict, input_dict: dict) -> dict: ...
