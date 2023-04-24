from PyQt5.QtWidgets import (
    QSlider,
    QSizePolicy,
    QWidget,
    QVBoxLayout,
    QLabel,
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


class PyQtSlider(PyQtComponentBase,
                 IVariableRelatedComponent, metaclass=PyQtMetaClass):
    def __init__(self,
                 component_id: str,
                 min: int = 0,
                 max: int = 100,
                 step: int = 1,
                 **kwargs):

        PyQtComponentBase.__init__(self)

        self.__slider = QSlider(Qt.Orientation.Horizontal)
        self._add_widget(self.__slider)

        self.__variable_id = None
        self.__component_id = component_id
        self.__min = min
        self.__max = max
        self.__step = step
        self.__kwargs = kwargs

    def init(self):
        self.__slider.valueChanged.connect(self._update_value)
        self.__slider.setRange(self.__min, self.__max)
        self.__slider.setSingleStep(self.__step)
        self.__setText(self.__slider.value())

    def __setText(self, value: int):
        self._set_label_text(f"{self.__kwargs['label']}: {value}")

    def _update_value(self, value: float) -> None:
        ChangeVariableValueOperation(
            variable_id=self.__variable_id,
            new_value=value,
        ).run()

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        self.__slider.setValue(data[VALUE_KEY])
        self.__setText(data[VALUE_KEY])

    def set_variable(self, variable_id: str) -> None:
        self.__variable_id = variable_id
        AddVariableObserverOperation(
            variable_id=variable_id,
            observer_id=self.__component_id,
        ).run()

    def on_update(self) -> None:
        pass
