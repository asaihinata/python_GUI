from typing import overload

from numpy import ndarray

__all__ = ("_to_list", "_to_tuple")

@overload
def _to_list(array: list | tuple | range | ndarray) -> list: ...
@overload
def _to_list[T](array: T) -> list[T]: ...
@overload
def _to_tuple(array: list | tuple | range | ndarray) -> tuple: ...
@overload
def _to_tuple[T](array: T) -> tuple[T, ...]: ...
