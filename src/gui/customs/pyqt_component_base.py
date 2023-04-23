from PyQt5.QtWidgets import (
    QWidget,
)
from abc import (
    abstractmethod,
)

from src.interfaces.ui import (
    IUIComponent,
    PyQtMetaClass,
)


class PyQtComponentBase(IUIComponent, metaclass=PyQtMetaClass):
    @abstractmethod
    def init(self) -> None:
        """
        Initialize the component (only for PyQt Component). 
        """
        raise NotImplementedError
