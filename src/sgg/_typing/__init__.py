from typing import Literal

__all__ = (
    "_Type_icon",
    "_Type_types",
    "_Type_abortretryignore",
    "_Type_ok",
    "_Type_okcancel",
    "_Type_yesno",
    "_Type_yesnocancel",
    "_Type_retrycancel",
)
type _Type_icon = Literal["error", "info", "question", "warning"]
type _Type_types = Literal[
    "abortretryignore", "ok", "okcancel", "retrycancel", "yesno", "yesnocancel"
]
type _Type_abortretryignore = Literal["abort", "retry", "ignore"]
type _Type_ok = Literal["ok"]
type _Type_okcancel = Literal["ok", "cancel"]
type _Type_yesno = Literal["yes", "no"]
type _Type_yesnocancel = Literal["cancel", "yes", "no"]
type _Type_retrycancel = Literal["retry", "cancel"]
