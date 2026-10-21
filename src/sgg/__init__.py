from sgg.version import __version__, __version_info__

__all__ = ("__version__", "__version_info__")


def __dir__():
    return (
        i for i in globals().keys() if i.startswith("__") or not i.startswith("_")
    )
