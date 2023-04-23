from src.interfaces import (
    ISystem,
    IPublisher,
)
from src.cores import (
    Variable,
    System,
)
from src.cores import (
    System,
)
from src.constants import (
    NAME_KEY,
    VALUE_KEY,
)

from .system_call_base import SystemCallBase


class RaiseErrorOperation(SystemCallBase):
    def __init__(self, error_message: str,
                 trigger_id: str = None):
        super().__init__(trigger_id)
        self.__error_message = error_message

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _run_impl(self) -> None:
        System.system.error.change_value(
            **{
                VALUE_KEY: self.__error_message
            }
        )

    def __repr__(self) -> str:
        return f"<CreateVariableOperation operation_id={self.operation_id} variable_name={self.__variable_id} variable_value={self.__variable_value}/>"
