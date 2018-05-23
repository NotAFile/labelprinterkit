import io
from abc import ABC, abstractmethod
from typing import Dict, Tuple

from ..label import Label


class BaseErrorStatus(ABC):
    """Represents the errors the printer has"""
    @abstractmethod
    def any(self):
        """return if any errors have occurred"""
        return any(self.data.values())

    def __getattr__(self, attr):
        return self.data[attr]

    def __repr__(self):
        return "<Errors {}>".format(self.data)


class BaseStatus(ABC):
    """Represents the status of the printer"""
    errors = None  # type: BaseErrorStatus

    def __repr__(self):
        return "<Status {} {}>".format(self.data, self.errors)

    @abstractmethod
    def __getattr__(self, attr):
        pass

    @abstractmethod
    def ready(self) -> bool:
        """return if the printer is ready for printing"""
        pass


class BasePrinter(ABC):
    """Base class for printers. All printers define this API.  Any other
    methods are prefixed with a _ to indicate they are not part of the
    printer API"""

    DPI = None  # type: Tuple[float, float]

    def __init__(self, io_obj: io.BufferedIOBase) -> None:
        self.io = io_obj

    def estimate_label_size(self, label: Label) -> Tuple[float, float]:
        """estimate the Labels size in mm"""

        xdpi, ydpi = self.DPI
        xpixels, ypixels = label.size
        return (xpixels / xdpi) * 2.54, (ypixels / ydpi) * 2.54

    def print_label(self, label: Label) -> BaseStatus:
        """Print the label"""

    @abstractmethod
    def connect(self) -> None:
        """Connect to the Printer"""
        pass
