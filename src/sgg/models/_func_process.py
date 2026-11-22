from types import FunctionType

__all__ = ("_do_func",)


def _do_func(
    f: list[FunctionType] | tuple[FunctionType, ...] | FunctionType | None = None,
):
    if f is not None:
        if not isinstance(f, list | tuple | FunctionType):
            raise TypeError("型が不正です")
        if isinstance(f, FunctionType):
            f()
        else:
            for i in f:
                if isinstance(i, FunctionType):
                    i()
                else:
                    continue
