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
from src.operations.system_call import *
from .pyqt_component_base import PyQtComponentBase


class PyQtButtonList(PyQtComponentBase,
                     IVariableRelatedComponent):
    def __init__(self,
                 component_id: str) -> None:
        super().__init__()

        self.__variable_id = None
        self.__component_id = component_id

    def init(self) -> None:
        self.__clear_widgets()

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        if publisher.type != VariableType.LIST:
            RaiseErrorOperation(
                error_message="The variable is not a list.",
            ).run()

        values = data[VALUE_KEY]

        for value in values:
            self._add_widget(QPushButton(value))

    def __clear_widgets(self) -> None:
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            self.layout.removeWidget(widget)
            widget.deleteLater()

    def set_variable(self, variable_id: str) -> None:
        AddVariableObserverOperation(
            variable_id=variable_id,
            observer_id=self.__component_id,
        ).run()
