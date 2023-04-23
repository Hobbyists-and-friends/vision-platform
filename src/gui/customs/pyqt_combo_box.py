from PyQt5.QtWidgets import (
    QComboBox,
)

from src.interfaces import (
    IPublisher,
)
from src.interfaces.ui import (
    PyQtMetaClass,
    IVariableRelatedComponent,
)
from src.operations.system_call import *
from .pyqt_component_base import PyQtComponentBase


class PyQtComboBox(PyQtComponentBase, QComboBox,
                   IVariableRelatedComponent, metaclass=PyQtMetaClass):
    def __init__(self, values: list = []) -> None:
        QComboBox.__init__(self)
        self.__variable_id = None
        self.__values = values

    def init(self) -> None:
        for value in self.__values:
            self.addItem(value)

        self.currentIndexChanged.connect(self._update_value)

        self.setCurrentIndex(0)

    def _update_value(self, index: int) -> None:
        ChangeVariableValueOperation(
            variable_id=self.__variable_id,
            new_value=self.__values[index],
        ).run()

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass

    def set_variable(self, variable_id: str) -> None:
        self.__variable_id = variable_id

    def on_update(self) -> None:
        pass
