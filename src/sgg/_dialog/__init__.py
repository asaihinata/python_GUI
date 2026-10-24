from os.path import split
from tkinter import _destroy_temp_root, _get_temp_root

__all__ = ("Dialog", "_Dialog")


class Dialog:

    command = None

    def __init__(self, master=None, **options):
        if master is None:
            master = options.get("parent")
        self.master = master
        self.options = options

    def _fixoptions(self):
        pass

    def _fixresult(self, widget, result):
        return result

    def show(self, **options):
        for k, v in options.items():
            self.options[k] = v

        self._fixoptions()

        master = self.master
        if master is None:
            master = _get_temp_root()
        try:
            self._test_callback(master)
            s = master.tk.call(self.command, *master._options(self.options))
            s = self._fixresult(master, s)
        finally:
            _destroy_temp_root(master)

        return s

    def _test_callback(self, master):
        pass


class _Dialog(Dialog):

    def _fixoptions(self):
        try:
            # make sure "filetypes" is a tuple
            self.options["filetypes"] = tuple(self.options["filetypes"])
        except KeyError:
            pass

    def _fixresult(self, widget, result):
        if result:
            # keep directory and filename until next time
            # convert Tcl path objects to strings
            try:
                result = result.string
            except AttributeError:
                # it already is a string
                pass
            path, file = split(result)
            self.options["initialdir"] = path
            self.options["initialfile"] = file
        self.filename = result  # compatibility
        return result
