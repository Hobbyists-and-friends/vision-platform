import types

from PyQt5.QtWidgets import (
    QSlider,
    QSizePolicy,
)
from PyQt5.QtCore import Qt

from src.interfaces import (
    ISystem,
    IPublisher,
    IOperation,
)
from src.operations import (
    ChangeVariableValueOperation,
)

from .ComponentBase import ComponentBase


class Slider(ComponentBase, QSlider):
    def __init__(self,
                 system: 'ISystem',
                 component_id: str,
                 min: int = 0,
                 max: int = 100,
                 step: int = 1,
                 **kwargs):
        ComponentBase.__init__(self, system, component_id, **kwargs)
        QSlider.__init__(self, **kwargs)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed,
        )
        self.setOrientation(Qt.Orientation.Horizontal)
        self.__variable_id = None
        self.valueChanged.connect(self._update_value)
        self.setRange(min, max)

    def _update_value(self, value: float) -> None:
        update_class = ChangeVariableValueOperation if not isinstance(
            ChangeVariableValueOperation, types.ModuleType) else ChangeVariableValueOperation.ChangeVariableValueOperation
        update_class(
            self.system,
            operation_id="ChangeVariableValueOperation",
            variable_id=self.__variable_id,
            new_value=value,
        ).run()

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass

    def set_variable_id(self, variable_id: str) -> None:
        self.__variable_id = variable_id
