from sgg.popup import (Popup, PopupError, PopupInformation, PopupQuestion,
                       PopupWarning)
from sgg.version import __version__, __version_info__
from sgg.widget import *

__all__ = (
    "__version__",
    "__version_info__",
    "Popup",
    "PopupInformation",
    "PopupWarning",
    "PopupError",
    "PopupQuestion",
)


class gui:
    @classmethod
    def window(cls, cnf={}, **kw):
        return Window(cnf, **kw)

    @staticmethod
    def Label(**kw):
        return {"type": "label", "kw": kw}


def __dir__():
    return (i for i in globals().keys() if i.startswith("__") or not i.startswith("_"))
