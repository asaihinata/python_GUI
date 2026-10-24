from sgg._dialog import _Dialog

__all__ = ("AskSaveAsFilename",)


class SaveAs(_Dialog):
    command = "tk_getSaveFile"


class AskSaveAsFilename:
    __slots__ = ("_path",)

    def __new__(cls, **options):
        cls = super().__new__(cls)
        cls._path = SaveAs(**options).show()
        return cls

    def __str__(self):
        return str(self._path)

    def __fspath__(self):
        return str(self._path)
