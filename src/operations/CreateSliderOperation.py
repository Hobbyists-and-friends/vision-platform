import types

from src.interfaces import (
    ISystem,
    IPublisher,
)
from src.gui.customs import Slider

from .OperationBase import OperationBase
from .ChangeVariableValueOperation import ChangeVariableValueOperation


class CreateSliderOperation(OperationBase):
    def __init__(self,
                 system: 'ISystem',
                 operation_id: str,
                 component_id: str,
                 min_value: int = 0,
                 max_value: int = 100,
                 step: int = 1,
                 store: bool = False,
                 run_at_first: bool = True):
        super().__init__(system, operation_id, store, run_at_first)
        self.__component_id = component_id
        self.__min_value = min_value
        self.__max_value = max_value
        self.__step = step

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _run(self) -> None:
        class_component = Slider if not isinstance(
            Slider, types.ModuleType) else Slider.Slider
        slider = class_component(
            system=self.system,
            component_id=self.__component_id,
            min=self.__min_value,
            max=self.__max_value,
            step=self.__step,
        )
        self.system.ui_components[self.__component_id] = slider

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass
