from pkg_resources import get_distribution

__all__ = ["printers", "backends", "items", "label"]
__version__ = get_distribution(__name__).version
