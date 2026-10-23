"""`辞書型(dict)`についての処理を行うモジュール"""

from typing import Any

__all__: tuple[str,] = ("_setDefaultValues1", "_setDefaultValues2")

def _setDefaultValues1(default: dict, kw: dict) -> dict: ...
def _setDefaultValues2(default: dict, cnf: dict | None = None, **kw: Any) -> dict: ...
