from types import FunctionType

__all__ = ("_do_func",)


def _do_func(f):
    if not isinstance(f, list | tuple | FunctionType):
        return
    if isinstance(f, FunctionType):
        f()
    else:
        for i in f:
            if not isinstance(i, FunctionType):
                continue
            else:
                i()
