from src.interfaces import (
    ISystem,
    IPublisher,
)
from src.constants import (
    VALUE_KEY,
)
from .OperationBase import OperationBase


class LogVariableOperation(OperationBase):
    def __init__(self,
                 system: 'ISystem',
                 operation_id: str,
                 variable_id: str,
                 store: bool = False):
        super().__init__(system, operation_id, store)
        self.__variable_id = variable_id

    def _run(self) -> None:
        pass

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        print(self.system.variables[self.__variable_id].data[VALUE_KEY])

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass
