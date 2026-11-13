"""
カーソルのスタイルを設定するモジュール

References:
    https://www.tcl-lang.org/man/tcl9.0/TkCmd/cursors.html
"""

from typing import Final

__all__ = ("Curosr",)
_cursor_list: Final[tuple]

class Cursor:
    def __new__(cls, cursor: str) -> str:
        """
        ウィジェットで使用できるカーソル名を調べそれを返す
        使用できないカーソル名を指定した場合,\"\"を返す

        :param cursor: 使用できるカーソル名を指定する
        :type cursor: str
        :return: カーソルを返す
        :rtype: str
        """
