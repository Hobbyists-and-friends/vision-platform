from src.interfaces import (
    ISystem,
    IPublisher,
)
from src.cores import (
    Variable,
    System,
)
from src.constants import (
    NAME_KEY,
    VALUE_KEY,
)

from .system_call_base import SystemCallBase


class CreateVariableOperation(SystemCallBase):
    def __init__(self, variable_id: str,
                 trigger_id: str = None,
                 variable_value: object = None):
        super().__init__(trigger_id)
        self.__variable_id = variable_id
        self.__variable_value = variable_value

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _run_impl(self) -> None:
        if self.__variable_id in System.system.variables.keys():
            return
        variable = Variable(**{
            NAME_KEY: self.__variable_id,
            VALUE_KEY: self.__variable_value,
        })
        System.system.variables[self.__variable_id] = variable

    def __repr__(self) -> str:
        return f"<CreateVariableOperation operation_id={self.operation_id} variable_name={self.__variable_id} variable_value={self.__variable_value}/>"
