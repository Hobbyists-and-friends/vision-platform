from src.interfaces import (
    ISystem,
    IPublisher,
)
from src.constants import (
    VALUE_KEY,
)
from .OperationBase import OperationBase


class ChangeVariableValueOperation(OperationBase):
    def __init__(self,
                 system: 'ISystem',
                 operation_id: str,
                 variable_id: str,
                 new_value: object,
                 store: bool = False):
        super().__init__(system, operation_id, store)
        self.__variable_id = variable_id
        self.__new_value = new_value

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _run(self) -> None:
        if self.__variable_id not in self.system.variables.keys():
            return
        self.system.variables[self.__variable_id].change_value(
            **{
                VALUE_KEY: self.__new_value
            }
        )

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass
