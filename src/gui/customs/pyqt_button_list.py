from functools import partial

from PyQt5.QtWidgets import (
    QVBoxLayout,
    QPushButton,
)

from src.interfaces import (
    IPublisher,
)
from src.interfaces.ui import (
    IVariableRelatedComponent,
)
from src.constants import *
from src.cores import System
from src.operations.system_call import *
from .pyqt_component_base import PyQtComponentBase


class PyQtButtonList(PyQtComponentBase,
                     IVariableRelatedComponent):
    def __init__(self,
                 component_id: str) -> None:
        super().__init__(component_id=component_id, horizontal=True)

        self.__variable_id = None
        self.__component_id = component_id

    def init(self) -> None:
        self.__clear_widgets()

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        values = System.system.variables[self._params[SRC_VARIABLE]
                                         ].data[VALUE_KEY]

        for value in values:
            button = QPushButton(value)
            button.clicked.connect(partial(self._button_clicked, value))
            self._add_widget(button)

    def _button_clicked(self, value: str) -> None:
        if RESULT_VARIABLE in self._params:
            ChangeVariableValueOperation(
                variable_id=self._params[RESULT_VARIABLE],
                new_value=value,
            ).run()

    def __clear_widgets(self) -> None:
        for i in reversed(range(self._layout.count())):
            widget = self._layout.itemAt(i).widget()
            self._layout.removeWidget(widget)
            widget.deleteLater()

    def on_update(self) -> None:
        pass

    def _verify_variable(self, param_key: str, variable_id: str) -> None:
        if param_key == SRC_VARIABLE:
            return System.system.variables[variable_id].type == VariableType.LIST
        else:
            return True

    @property
    def default_params(self) -> dict:
        return {}
