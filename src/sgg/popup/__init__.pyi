from typing import ClassVar, Literal

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
    __slots__: tuple[Literal["__select"]]
    def __init__(
        self,
        title: str | None = None,
        message: str | None = None,
        *,
        detail: str | None = None,
        icon: str | None = None,
        type: str | None = ...,
        default: str = ...,
    ) -> None: ...
    def __dir__(self) -> list[str]: ...
    def __str__(self) -> str: ...
    @property
    def select(self) -> str: ...

class PopupInformation:
    __slots__: tuple[Literal["__select"]]
    def __init__(
        self,
        title: str | None = "Information",
        message: str | None = "Information",
        *,
        detail: str | None = None,
    ) -> None: ...
    def __dir__(self) -> list[str]: ...
    def __str__(self) -> Literal["ok"]: ...
    @property
    def select(self) -> Literal["ok"]: ...

class PopupError:
    __slots__: tuple[Literal["__select"]]
    def __init__(
        self,
        title: str | None = "Error",
        message: str | None = "Error",
        *,
        detail: str | None = None,
    ) -> None: ...
    def __dir__(self) -> list[str]: ...
    def __str__(self) -> Literal["ok"]: ...
    @property
    def select(self) -> Literal["ok"]: ...

class PopupWarning:
    __slots__: tuple[Literal["__select"]]
    def __init__(
        self,
        title: str | None = "Warning",
        message: str | None = "Warning",
        *,
        detail: str | None = None,
    ) -> None: ...
    def __dir__(self) -> list[str]: ...
    def __str__(self) -> Literal["ok"]: ...
    @property
    def select(self) -> Literal["ok"]: ...

class PopupQuestion:
    __slots__: tuple[Literal["__select"]]
    def __init__(
        self,
        title: str | None = "Question",
        message: str | None = "Question",
        *,
        detail: str | None = None,
        default: Literal["yes", "no"] = "yes",
    ) -> None: ...
    def __dir__(self) -> list[str]: ...
    def __bool__(self) -> bool: ...
    def __invert__(self) -> bool: ...
    __not__ = __invert__
    def __str__(self) -> Literal["yes", "no"]: ...
    @property
    def select(self) -> Literal["yes", "no"]: ...
