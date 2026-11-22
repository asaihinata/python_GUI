from itertools import product

import numpy as np

__all__ = ("_Pairwise_Process", "_ThreeD_Process")


class _Pairwise_Process(product):
    def __new__(cls, x, y, /, *iterables):
        x = np.asanyarray(x)
        if x.ndim <= 1:
            x = np.expand_dims(x, axis=0)
        y = np.asanyarray(y)
        if y.ndim <= 1:
            y = np.expand_dims(y, axis=0)
        return super().__new__(
            cls,
            x,
            y,
            *map(lambda i: (i,) if np.isscalar(i) else i, iterables),
            repeat=1,
        )


class _ThreeD_Process(product):
    def __new__(cls, x, y, z, /, *iterables):
        x = np.asanyarray(x)
        if x.ndim <= 1:
            x = np.expand_dims(x, axis=0)
        y = np.asanyarray(y)
        if y.ndim <= 1:
            y = np.expand_dims(y, axis=0)
        z = np.asanyarray(z)
        if z.ndim <= 1:
            z = np.expand_dims(z, axis=0)
        iterables = ((i,) if np.isscalar(i) else i for i in iterables)
        return super().__new__(cls, x, y, z, *iterables, repeat=1)
