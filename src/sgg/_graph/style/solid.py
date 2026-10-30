from numpy import asarray

__all__ = ("_check_linestyle",)


def _check_linestyle(ls):
    if isinstance(ls, str):
        if ls in (
            "-",
            "solid",
            "--",
            "dashed",
            "-.",
            "dashdot",
            ":",
            "dotted",
            "",
            "none",
        ):
            return ls
        raise NameError(f"{ls}という線種は存在しません")
    elif isinstance(ls, tuple):
        if len(ls) != 2:
            raise ValueError
        offset, onoffseq = ls
        if not isinstance(offset, int | float):
            raise TypeError
        if not isinstance(onoffseq, list | tuple):
            raise TypeError
        if asarray(onoffseq).dtype.kind not in ("i", "u", "f"):
            raise TypeError
        return ls
    else:
        raise TypeError
