from src.cores import (
    System,
)
from src.operations.system_call import *
from .system_call_base import SystemCallBase


class AddVariableObserverOperation(SystemCallBase):
    def __init__(self,
                 variable_id: str,
                 observer_id: str,
                 update: bool = True,
                 trigger_id: str = None):
        super().__init__(trigger_id)
        self.__variable_id = variable_id
        self.__observer_id = observer_id
        self.__update = update

    def _run_impl(self) -> None:
        if self.__variable_id not in System.system.variables:
            RaiseErrorOperation(
                error_message=f"Variable {self.__variable_id} does not exist",
            ).run()
            return
        System.system.variables[self.__variable_id].add_observer(
            System.system.observerable_components[self.__observer_id]
        )

        if self.__update:
            System.system.variables[self.__variable_id].notify()

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass
