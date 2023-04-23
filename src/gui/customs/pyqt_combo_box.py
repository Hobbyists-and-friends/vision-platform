from PyQt5.QtWidgets import (
    QComboBox,
)

from src.interfaces import (
    IPublisher,
)
from src.constants import *
from src.interfaces.ui import (
    PyQtMetaClass,
    IVariableRelatedComponent,
)
from src.operations.system_call import *
from .pyqt_component_base import PyQtComponentBase


class PyQtComboBox(PyQtComponentBase, QComboBox,
                   IVariableRelatedComponent, metaclass=PyQtMetaClass):
    def __init__(self,
                 component_id: str,
                 values: list = []) -> None:
        QComboBox.__init__(self)
        self.__variable_id = None
        self.__values = values
        self.__component_id = component_id

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
        value = data[VALUE_KEY]
        for i in range(len(self.__values)):
            if self.__values[i] == value:
                self.setCurrentIndex(i)
                break

    def set_variable(self, variable_id: str) -> None:
        self.__variable_id = variable_id
        AddVariableObserverOperation(
            variable_id=variable_id,
            observer_id=self.__component_id,
        ).run()

    def on_update(self) -> None:
        pass
