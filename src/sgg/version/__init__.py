"""インストール済みの`sgg`のより詳細なバージョン情報を表示するモジュール"""

from collections import namedtuple
from re import split
from typing import final

__all__ = ("__version__", "__version_info__")


@final
class _Version:
    __slots__ = ("_major", "_minor", "_micro")

    def __init__(self, var):
        self._major, self._minor, self._micro = tuple(map(int, split(r"[.]", var)))

    @property
    def major(self):
        return self._major

    @property
    def minor(self):
        return self._minor

    @property
    def micro(self):
        return self._micro


def _varsion_info(var):
    v = _Version(var)
    return VersionInfo(v.major, v.minor, v.micro)


VersionInfo = namedtuple("VersionInfo", "major, minor, micro")
__version__ = "0.0.0"
__version_info__ = _varsion_info(__version__)
