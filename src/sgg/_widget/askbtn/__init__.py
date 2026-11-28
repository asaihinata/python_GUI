from pathlib import Path

from sgg.models import _delete_keys, _setDefaultValues2

__all__ = ("_Ask_Color_Btn", "_Ask_File_Btn", "_Ask_Directory_Btn")


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

    def to_str(self):
        return str(self.path)

    @property
    def path(self):
        return Path(self._path)

    @property
    def parent(self):
        return self.path.parent

    @property
    def parents(self):
        return self.path.parents

    @property
    def stem(self):
        return self.path.stem

    @property
    def suffix(self):
        return self.path.suffix

    @property
    def suffixes(self):
        return self.path.suffixes

    @property
    def name(self):
        return self.path.name

    def is_file(self, follow_symlinks=True):
        return self.path.is_file(follow_symlinks=follow_symlinks)

    def is_dir(self, follow_symlinks=True):
        return self.path.is_dir(follow_symlinks=follow_symlinks)

    def exists(self, follow_symlinks=True):
        return self.path.exists(follow_symlinks=follow_symlinks)

    def absolute(self):
        return self.path.absolute()

    def resolve(self, strict=False):
        return self.path.resolve(strict)


class _Ask_File_Btn(_Ask_Path_Btn):
    def with_suffix(self, suffix):
        self.path.with_suffix(suffix)


class _Ask_Directory_Btn(_Ask_Path_Btn):
    def iterdir(self):
        return self.path.iterdir()

    def glob(self, pattern, *, case_sensitive=None, recurse_symlinks=False):
        return self.path.glob(
            pattern, case_sensitive=case_sensitive, recurse_symlinks=recurse_symlinks
        )

    def rglob(self, pattern, *, case_sensitive=None, recurse_symlinks=False):
        return self.path.rglob(
            pattern, case_sensitive=case_sensitive, recurse_symlinks=recurse_symlinks
        )
