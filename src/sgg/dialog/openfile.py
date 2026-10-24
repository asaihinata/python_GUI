from os.path import split

from sgg._dialog import _Dialog

__all__ = ("AskOpenFilename",)


class Open(_Dialog):
    command = "tk_getOpenFile"

    def _fixresult(self, widget, result):
        if isinstance(result, tuple):
            result = tuple([getattr(r, "string", r) for r in result])
            if result:
                path, file = split(result[0])
                self.options["initialdir"] = path
            return result
        if not widget.tk.wantobjects() and "multiple" in self.options:
            return self._fixresult(widget, widget.tk.splitlist(result))
        return _Dialog._fixresult(self, widget, result)


class AskOpenFilename:
    __slots__ = ("_path",)

    def __new__(cls, **options):
        cls = super().__new__(cls)
        cls._path = Open(**options).show()
        return cls

    def __str__(self):
        return str(self._path)

    def __fspath__(self):
        return str(self._path)
