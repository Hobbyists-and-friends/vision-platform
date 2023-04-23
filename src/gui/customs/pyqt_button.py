from PyQt5.QtWidgets import QPushButton


from src.cores import (
    System,
)
from src.interfaces.ui import (
    IOperationDispatcherComponent,
    PyQtMetaClass,
)

from .pyqt_component_base import PyQtComponentBase


class PyQtButton(PyQtComponentBase, QPushButton,
                 IOperationDispatcherComponent, metaclass=PyQtMetaClass):
    def __init__(self,
                 text: str = "Button",
                 *args, **kwargs):
        QPushButton.__init__(self)

        self.__variable_id = None
        self.__text = text
        self.__operation_id = None
        self.clicked.connect(self.dispatch)

    def init(self) -> None:
        """
        """
        self.setText(self.__text)

    def dispatch(self) -> None:
        """

        """
        System.system.operations[self.__operation_id].run()

    def on_update(self) -> None:
        """

        """
        pass

    def set_operation_id(self, operation_id: str) -> None:
        """

        """
        self.__operation_id = operation_id
