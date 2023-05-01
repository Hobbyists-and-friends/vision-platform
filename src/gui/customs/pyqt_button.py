from PyQt5.QtWidgets import QPushButton


from src.cores import (
    System,
)
from src.interfaces.ui import (
    IOperationDispatcherComponent,
    PyQtMetaClass,
)

from .pyqt_component_base import PyQtComponentBase


class PyQtButton(PyQtComponentBase,
                 IOperationDispatcherComponent, metaclass=PyQtMetaClass):
    def __init__(self,
                 component_id: str,
                 text: str = "Button",
                 *args, **kwargs):
        PyQtComponentBase.__init__(self, component_id)

        self.button = QPushButton()
        self._add_widget(self.button)

        self.__variable_id = None
        self.__text = text
        self.__operation_id = None
        self.button.clicked.connect(self.dispatch)

    def init(self) -> None:
        """
        """
        self.button.setText(self.__text)

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

    def _verify_variable(self, param_key: str, variable_id: str) -> None:
        return True

    @property
    def default_params(self) -> str:
        return {}
