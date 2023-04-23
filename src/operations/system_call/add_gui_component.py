from src.interfaces import (
    ISystem,
    IOperation,
    IVariable,
    IGUIComponent,
    IPublisher,
)
from src.cores import (
    System,
)
from .system_call_base import SystemCallBase
from .raise_error_op import RaiseErrorOperation


class AddGUIComponentOperation(SystemCallBase):
    def __init__(self, component_id: str,
                 layout: dict,
                 trigger_id: str = None):
        super().__init__(trigger_id)
        self.__component_id = component_id
        self.__layout = layout

    def load(self, data: dict) -> None:
        pass

    def export(self) -> dict:
        pass

    def _run_impl(self) -> None:
        if self.__component_id not in System.system.ui_components:
            RaiseErrorOperation(
                error_message=f"Component {self.__component_id} does not exist",
            ).run()
            return

        System.system.application.add_component(
            self.__component_id, self.__layout)
