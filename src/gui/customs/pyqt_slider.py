from PyQt5.QtWidgets import (
    QSlider,
    QSizePolicy,
)
from PyQt5.QtCore import (
    Qt,
)

from src.cores import (
    System,
)
from src.constants import *
from src.interfaces import (
    IPublisher,
)
from src.interfaces.ui import (
    IOperationDispatcherComponent,
    PyQtMetaClass,
    IVariableRelatedComponent,
)

from src.operations.system_call import *
from .pyqt_component_base import PyQtComponentBase


class PyQtSlider(PyQtComponentBase, QSlider,
                 IVariableRelatedComponent, metaclass=PyQtMetaClass):
    def __init__(self,
                 component_id: str,
                 min: int = 0,
                 max: int = 100,
                 step: int = 1,
                 **kwargs):
        QSlider.__init__(self)
        self.__component_id = component_id

        self.__variable_id = None
        self.__min = min
        self.__max = max
        self.__step = step

    def init(self):
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )
        self.setOrientation(Qt.Orientation.Horizontal)
        self.valueChanged.connect(self._update_value)
        self.setRange(self.__min, self.__max)

    def _update_value(self, value: float) -> None:
        ChangeVariableValueOperation(
            variable_id=self.__variable_id,
            new_value=value,
        ).run()

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        self.setValue(data[VALUE_KEY])

    def set_variable(self, variable_id: str) -> None:
        self.__variable_id = variable_id
        AddVariableObserverOperation(
            variable_id=variable_id,
            observer_id=self.__component_id,
        ).run()

    def on_update(self) -> None:
        pass
