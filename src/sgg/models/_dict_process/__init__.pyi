"""`辞書型(dict)`についての処理を行うモジュール"""

__all__: tuple[str,] = ("_setDefaultValues",)

def _setDefaultValues(default: dict, kw: dict) -> dict:
    """
    `default`で保存されている初期値を`kw`で代入させ,それを返す関数

    :param default: 初期値の辞書型
    :type default: dict
    :param kw: 更新させる辞書型
    :type kw: dict
    """
