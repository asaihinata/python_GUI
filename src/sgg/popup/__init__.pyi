from typing import ClassVar, Literal, overload

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
        self: Popup[Literal["ok"]],
        title: str | None = None,
        message: str | None = None,
        *,
        detail: str | None = None,
        icon: Literal["error", "info", "question", "warning"] | None = None,
        type: Literal["ok"] = ...,
        default: Literal["ok"] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Popup[Literal["ok", "cancel"]],
        title: str | None = None,
        message: str | None = None,
        *,
        detail: str | None = None,
        icon: Literal["error", "info", "question", "warning"] | None = None,
        type: Literal["okcancel"],
        default: Literal["ok", "cancel"] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Popup[Literal["yes", "no"]],
        title: str | None = None,
        message: str | None = None,
        *,
        detail: str | None = None,
        icon: Literal["error", "info", "question", "warning"] | None = None,
        type: Literal["yesno"],
        default: Literal["yes", "no"] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Popup[Literal["cancel", "yes", "no"]],
        title: str | None = None,
        message: str | None = None,
        *,
        detail: str | None = None,
        icon: Literal["error", "info", "question", "warning"] | None = None,
        type: Literal["yesnocancel"],
        default: Literal["cancel", "yes", "no"] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Popup[Literal["retry", "cancel"]],
        title: str | None = None,
        message: str | None = None,
        *,
        detail: str | None = None,
        icon: Literal["error", "info", "question", "warning"] | None = None,
        type: Literal["retrycancel"],
        default: Literal["retry", "cancel"] = ...,
    ) -> None: ...
    @overload
    def __init__(
        self: Popup[Literal["abort", "retry", "ignore"]],
        title: str | None = None,
        message: str | None = None,
        *,
        detail: str | None = None,
        icon: Literal["error", "info", "question", "warning"] | None = None,
        type: Literal["abortretryignore"],
        default: Literal["abort", "retry", "ignore"] = ...,
    ) -> None: ...
    def __dir__(self) -> list[str]: ...
    def __str__(self) -> str: ...
    @property
    def select(self) -> str: ...

class PopupInformation:
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
