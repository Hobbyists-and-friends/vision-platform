from src.cores import (
    System,
)
from .system_call_base import SystemCallBase


class AddVariableObserverOperation(SystemCallBase):
    def __init__(self,
                 variable_id: str,
                 observer_id: str,
                 trigger_id: str = None):
        super().__init__(trigger_id)
        self.__variable_id = variable_id
        self.__observer_id = observer_id

    def _run_impl(self) -> None:
        System.system.variables[self.__variable_id].add_observer(
            System.system.observerable_components[self.__observer_id]
        )

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass
