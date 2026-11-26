from zoneinfo import available_timezones

__all__ = ("TimeZoneList",)


class TimeZoneList:
    __slots__ = ("_set",)

    def __new__(cls, *, sort=False):
        cls = super().__new__(cls)
        if sort:
            cls._set = sorted(available_timezones())
        else:
            cls._set = available_timezones()
        return cls._set

    def __iter__(self):
        return iter(self._set)

    def __contains__(self, item):
        return item in self._set

    def __reversed__(self):
        return reversed(self._set)

    def __len__(self):
        return len(self._set)

    def __getitem__(self, key):
        if not isinstance(key,str):
            raise TypeError("keyの型が不正です")
        for tz in self:
            if key in tz:
                return tz
        else:
            raise KeyError(f"{key}というキー名は存在しません")