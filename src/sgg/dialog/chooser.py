from sgg._dialog import Dialog

__all__ = ("AskColor",)


class Chooser(Dialog):
    command = "tk_chooseColor"

    def _fixoptions(self):
        try:
            color = self.options["initialcolor"]
            if isinstance(color, tuple):
                self.options["initialcolor"] = "#%02x%02x%02x" % color
        except KeyError:
            pass

    def _fixresult(self, widget, result):
        if not result or not str(result):
            return None, None
        r, g, b = widget.winfo_rgb(result)
        return (r // 256, g // 256, b // 256), str(result)


class AskColor:
    def __new__(cls, color=None, **options):
        cls = Chooser(**options).show()
        if color:
            options = options.copy()
            options["initialcolor"] = color
        return cls
