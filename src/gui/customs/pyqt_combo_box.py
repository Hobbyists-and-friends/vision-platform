from PyQt5.QtWidgets import (
    QComboBox,
    QVBoxLayout,
    QLabel,
    QWidget,
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


class PyQtComboBox(PyQtComponentBase,
                   IVariableRelatedComponent, metaclass=PyQtMetaClass):
    def __init__(self,
                 component_id: str,
                 values: list,
                 alias: list = [],
                 **kwargs) -> None:
        PyQtComponentBase.__init__(self)
        self.__combo_box = QComboBox()
        self._add_widget(self.__combo_box)

        self.__variable_id = None
        self.__values = values
        self.__component_id = component_id
        self.__kwargs = kwargs

        if len(alias) == 0:
            self.__alias = values
        else:
            self.__alias = alias

    def init(self) -> None:
        for value in self.__alias:
            self.__combo_box.addItem(value)

        self.__combo_box.currentIndexChanged.connect(self._update_value)

        self.__combo_box.setCurrentIndex(0)
        self._set_label_text(f"{self.__kwargs['label']}")

    def _update_value(self, index: int) -> None:
        ChangeVariableValueOperation(
            variable_id=self.__variable_id,
            new_value=self.__values[index],
        ).run()

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        value = data[VALUE_KEY]
        for i in range(len(self.__values)):
            if self.__values[i] == value:
                self.__combo_box.setCurrentIndex(i)
                break

    def set_variable(self, variable_id: str) -> None:
        self.__variable_id = variable_id
        AddVariableObserverOperation(
            variable_id=variable_id,
            observer_id=self.__component_id,
        ).run()

    def on_update(self) -> None:
        pass
