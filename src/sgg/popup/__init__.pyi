from typing import ClassVar, Literal, overload
from sgg._typing import *
from sgg._dialog import Dialog

__all__ = (
    "Popup",
    "PopupError",
    "PopupInformation",
    "PopupQuestion",
    "PopupWarning",
)

class Message(Dialog):
    command: ClassVar[str]

class Popup:
    @overload
    def __init__(
        self: Popup[_Type_ok],
        title: str | None = None,
        message: str | None = None,
        *,
        detail: str | None = None,
        icon: _Type_icon | None = None,
        type: _Type_ok = ...,
        default: _Type_ok = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Popup[_Type_okcancel],
        title: str | None = None,
        message: str | None = None,
        *,
        detail: str | None = None,
        icon: _Type_icon | None = None,
        type: Literal["okcancel"],
        default: _Type_okcancel = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Popup[_Type_yesno],
        title: str | None = None,
        message: str | None = None,
        *,
        detail: str | None = None,
        icon: _Type_icon | None = None,
        type: Literal["yesno"],
        default: _Type_yesno = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Popup[_Type_yesnocancel],
        title: str | None = None,
        message: str | None = None,
        *,
        detail: str | None = None,
        icon: _Type_icon | None = None,
        type: Literal["yesnocancel"],
        default: _Type_yesnocancel = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Popup[_Type_retrycancel],
        title: str | None = None,
        message: str | None = None,
        *,
        detail: str | None = None,
        icon: _Type_icon | None = None,
        type: Literal["retrycancel"],
        default: _Type_retrycancel = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Popup[_Type_abortretryignore],
        title: str | None = None,
        message: str | None = None,
        *,
        detail: str | None = None,
        icon: _Type_icon | None = None,
        type: Literal["abortretryignore"],
        default: _Type_abortretryignore = ...,
    ) -> None: ...
    def __dir__(self) -> list[str]: ...
    def __str__(self) -> str: ...
    @property
    def select(self) -> str: ...

class PopupError:
    def __init__(
        self,
        title: str | None = "Error",
        message: str | None = "Error",
        *,
        detail: str | None = None,
    ) -> None: ...
    def __dir__(self) -> list[str]: ...
    def __str__(self) -> _Type_ok: ...
    @property
    def select(self) -> _Type_ok: ...

class PopupWarning:
    def __init__(
        self,
        title: str | None = "Warning",
        message: str | None = "Warning",
        *,
        detail: str | None = None,
    ) -> None: ...
    def __dir__(self) -> list[str]: ...
    def __str__(self) -> _Type_ok: ...
    @property
    def select(self) -> _Type_ok: ...

class PopupQuestion:
    def __init__(
        self,
        title: str | None = "Question",
        message: str | None = "Question",
        *,
        detail: str | None = None,
        default: _Type_yesno = "yes",
    ) -> None: ...
    def __dir__(self) -> list[str]: ...
    def __bool__(self) -> bool: ...
    def __invert__(self) -> bool: ...
    __not__ = __invert__
    def __str__(self) -> _Type_yesno: ...
    @property
    def select(self) -> _Type_yesno: ...
