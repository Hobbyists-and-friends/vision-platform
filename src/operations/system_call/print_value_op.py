from src.cores import System
from src.constants import (
    VALUE_KEY,
)

from .system_call_base import SystemCallBase
from .raise_error_op import RaiseErrorOperation


class PrintValueOperation(SystemCallBase):
    def __init__(self, variable_id: str,
                 trigger_id: str = None):
        super().__init__(trigger_id)
        self.__variable_id = variable_id

    def load(self, data: dict) -> None:
        pass

    def export(self) -> dict:
        pass

    def _run_impl(self) -> None:
        if self.__variable_id in System.system.variables:
            print(System.system.variables[self.__variable_id].data[VALUE_KEY])
        else:
            RaiseErrorOperation(
                error_message=f'Variable "{self.__variable_id}" does not exist.'
            ).run()
