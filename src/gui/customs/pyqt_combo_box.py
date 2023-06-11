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


class PyQtComboBox(
    PyQtComponentBase, IVariableRelatedComponent, metaclass=PyQtMetaClass
):
    def __init__(
        self, component_id: str, values: list, alias: list = [], **kwargs
    ) -> None:
        PyQtComponentBase.__init__(self, component_id)
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

        for value in self.__alias:
            self.__combo_box.addItem(value)

        self.__combo_box.currentIndexChanged.connect(self._update_value)

        self.__combo_box.setCurrentIndex(0)
        self._set_label_text(f"{self.__kwargs['label']}")

    def init(self) -> None:
        pass

    def _update_value(self, index: int) -> None:
        ChangeVariableValueOperation(
            variable_id=self._params[SRC_VARIABLE],
            new_value=self.__values[index],
        ).run()

    def update(self, publisher: "IPublisher", data: dict) -> None:
        value = data[VALUE_KEY]
        for i in range(len(self.__values)):
            if self.__values[i] == value:
                self.__combo_box.setCurrentIndex(i)
                break

    def on_update(self) -> None:
        pass

    def _verify_variable(self, param_key: str, variable_id: str) -> None:
        return True

    @property
    def default_params(self) -> dict:
        return {}
