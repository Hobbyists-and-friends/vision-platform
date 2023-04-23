from src.cores import (
    System,
)
from src.constants import ComponentType
from src.gui.customs import *
from .system_call_base import SystemCallBase
from .raise_error_op import RaiseErrorOperation


class CreateGUIComponentOperation(SystemCallBase):
    def __init__(self, component_id: str,
                 component_type: ComponentType,
                 trigger_id: str = None, **kwargs):
        super().__init__(trigger_id)
        self.__component_id = component_id
        self.__component_type = component_type
        self.__kwargs = kwargs

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _run_impl(self) -> None:
        if self.__component_id in System.system.ui_components:
            RaiseErrorOperation(
                error_message=f"Component with id {self.__component_id} already exists",
            ).run()
        else:
            if self.__component_type == ComponentType.BUTTON.value:
                component = PyQtButton(
                    component_id=self.__component_id,
                    text=self.__component_id,
                )

            elif self.__component_type == ComponentType.SLIDER.value:
                component = PyQtSlider(
                    component_id=self.__component_id,
                )
            elif self.__component_type == ComponentType.COMBO_BOX.value:
                component = PyQtComboBox(
                    **self.__kwargs
                )

            System.system.ui_components[self.__component_id] = component
