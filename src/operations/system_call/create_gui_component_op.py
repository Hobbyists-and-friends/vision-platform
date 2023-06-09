from src.utils.Logging import Logging

from src.cores import (
    System,
)
from src.constants import ComponentType
from src.gui.customs import *
from .system_call_base import SystemCallBase
from .raise_error_op import RaiseErrorOperation
from .add_gui_component import AddGUIComponentOperation


class CreateGUIComponentOperation(SystemCallBase):
    def __init__(
        self,
        component_id: str,
        component_type: ComponentType,
        trigger_id: str = None,
        **kwargs,
    ):
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
                    **self.__kwargs,
                )
            elif self.__component_type == ComponentType.COMBO_BOX.value:
                component = PyQtComboBox(
                    component_id=self.__component_id, **self.__kwargs
                )
            elif self.__component_type == ComponentType.IMAGE_DISPLAY.value:
                component = PyQtImageDisplay(
                    component_id=self.__component_id,
                    **self.__kwargs,
                )
            elif self.__component_type == ComponentType.BUTTON_LIST.value:
                component = PyQtButtonList(
                    component_id=self.__component_id,
                    **self.__kwargs,
                )
            elif self.__component_type == ComponentType.COMPONENT_LIST.value:
                component = PyQtComponentList(
                    component_id=self.__component_id,
                    add_component_class=AddGUIComponentOperation,
                    **self.__kwargs,
                )
                Logging.debug(msg=f"Component Id: {self.__component_id}")

            System.system.ui_components[self.__component_id] = component
