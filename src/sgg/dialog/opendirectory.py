from sgg._dialog import Dialog

__all__ = ("AskDirectoryname",)


class Directory(Dialog):
    command = "tk_chooseDirectory"

    def _fixresult(self, widget, result):
        if result:
            try:
                result = result.string
            except AttributeError:
                pass
            self.options["initialdir"] = result
        self.directory = result
        return result


class AskDirectoryname:
    __slots__ = ("_path",)

    def __new__(cls, **options):
        cls = super().__new__(cls)
        cls._path = Directory(**options).show()
        return cls

    def __str__(self):
        return str(self._path)

    def __fspath__(self):
        return str(self._path)
