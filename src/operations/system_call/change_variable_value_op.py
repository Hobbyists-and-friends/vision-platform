from src.interfaces import (
    ISystem,
    IPublisher,
)
from src.cores import (
    System,
)
from src.constants import (
    VALUE_KEY,
)
from .system_call_base import SystemCallBase
from .raise_error_op import RaiseErrorOperation


class ChangeVariableValueOperation(SystemCallBase):
    def __init__(self, variable_id: str,
                 new_value: object,
                 trigger_id: str = None):
        super().__init__(trigger_id)
        self.__variable_id = variable_id
        self.__new_value = new_value

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _run_impl(self) -> None:
        if self.__variable_id not in System.system.variables.keys():
            RaiseErrorOperation(
                error_message=f"Variable with id {self.__variable_id} does not exist. <ChangeVariableValueOperation variable={self.__variable_id} new_value={self.__new_value}>"
            ).run()
            return
        System.system.variables[self.__variable_id].change_value(
            **{
                VALUE_KEY: self.__new_value
            }
        )
