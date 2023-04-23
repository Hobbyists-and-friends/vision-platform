from src.cores import (
    System,
)

from .system_call_base import SystemCallBase


class SetComponentRelatedVariableOperation(SystemCallBase):
    def __init__(self,
                 component_id: str,
                 variable_id: str,
                 trigger_id: str = None):
        super().__init__(trigger_id)
        self.__component_id = component_id
        self.__variable_id = variable_id

    def load(self, data: dict) -> None:
        pass

    def export(self) -> dict:
        pass

    def _run_impl(self) -> None:
        System.system.ui_components[self.__component_id].set_variable(
            self.__variable_id
        )
