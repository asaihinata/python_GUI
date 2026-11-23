from sgg.models import _delete_keys, _setDefaultValues2

__all__ = ("_Ask_Color_Btn", "_Ask_Path_Btn")


class _Ask_Btn_base:
    def configure(self, cnf={}, **kw):
        if not cnf and not kw:
            return super().configure()
        self._default_dict = _setDefaultValues2(self._default_dict, cnf, **kw)
        self._exclusive_dict = _setDefaultValues2(
            self._exclusive_dict, self._default_dict
        )
        return super().configure(_delete_keys(self._default_dict, self._exclusive_dict))

    config = configure


class _Ask_Color_Btn(_Ask_Btn_base):
    def get_color(self):
        return self._color

    def get_rgb(self):
        return self._color[0]

    def get_hex(self):
        return self._color[1]


class _Ask_Path_Btn(_Ask_Btn_base):
    def __fspath__(self):
        return str(self._path)
