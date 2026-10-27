from sgg._dialog import Dialog
from sgg.models import _setDefaultValues1

__all__ = (
    "Popup",
    "PopupError",
    "PopupInformation",
    "PopupQuestion",
    "PopupWarning",
)


class Message(Dialog):
    command = "tk_messageBox"


class _Popup:
    _default_dict = {
        "default": None,
        "detail": None,
        "icon": None,
        "message": None,
        "title": None,
        "type": None,
    }

    def __init__(self, **kw):
        self._default_dict = _setDefaultValues1(self._default_dict, kw)
        self._select = Message(**self._default_dict).show()

    def __str__(self):
        return str(self._select)

    def __dir__(self):
        return ["__dir__", "__init__", "__str__", "select"]

    @property
    def select(self):
        return self._select


class Popup(_Popup):
    def __init__(
        self,
        title=None,
        message=None,
        *,
        detail=None,
        icon=None,
        type=None,
        default=None,
    ):
        super().__init__(
            title=title,
            message=message,
            detail=detail,
            icon=icon,
            type=type,
            default=default,
        )


class PopupInformation(_Popup):
    def __init__(self, title="Information", message="Information", *, detail=None):
        super().__init__(
            title=title,
            message=message,
            detail=detail,
            icon="info",
            type="ok",
            default="ok",
        )


class PopupError(_Popup):
    def __init__(self, title="Error", message="Error", *, detail=None):
        super().__init__(
            title=title,
            message=message,
            detail=detail,
            icon="error",
            type="ok",
            default="ok",
        )


class PopupWarning(_Popup):
    def __init__(self, title="Warning", message="Warning", *, detail=None):
        super().__init__(
            title=title,
            message=message,
            detail=detail,
            icon="warning",
            type="ok",
            default="ok",
        )


class PopupQuestion(_Popup):
    def __init__(
        self, title="Question", message="Question", *, detail=None, default="yes"
    ):
        if default not in ("yes", "no"):
            default = "yes"
        super().__init__(
            title=title,
            message=message,
            detail=detail,
            icon="question",
            type="yesno",
            default=default,
        )

    def __dir__(self):
        return ["__bool__", "__dir__", "__init__", "__str__", "select"]

    def __bool__(self):
        return True if self.select == "yes" else False

    def __invert__(self):
        return False if self.select == "yes" else True

    __not__ = __invert__
