from numpy import ndarray

__all__ = ("_to_list", "_to_tuple")


def _to_list(array):
    if isinstance(array, list):
        return array
    elif isinstance(array, tuple | range):
        return list(array)
    elif isinstance(array, ndarray):
        return array.tolist()
    return [array]


def _to_tuple(array):
    if isinstance(array, tuple):
        return array
    elif isinstance(array, list | range):
        return tuple(array)
    elif isinstance(array, ndarray):
        return tuple(array.tolist())
    return (array,)
