"""インストール済みの`sgg`のより詳細なバージョン情報を表示するモジュール"""

from typing import Final, NamedTuple

__all__ = ("__version__", "__version_info__")

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int

__version__: Final[str]
__version_info__: Final[VersionInfo]
