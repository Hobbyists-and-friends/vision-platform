from src.interfaces import (
    ISystem,
    IPublisher,
)
from src.cores import (
    Variable,
)
from src.constants import (
    NAME_KEY,
    VALUE_KEY,
)
from .OperationBase import OperationBase


class CreateVariableOperation(OperationBase):
    def __init__(self, system: 'ISystem',
                 operation_id: str,
                 variable_name: str,
                 variable_value: object = None,
                 store: bool = False,
                 run_at_first: bool = True):
        super().__init__(system, operation_id, store=store, run_at_first=run_at_first)
        self.__variable_name = variable_name
        self.__variable_value = variable_value

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _run(self) -> None:
        if self.__variable_name in self.system.variables.keys():
            return
        variable = Variable(self.system, **{
            NAME_KEY: self.__variable_name,
            VALUE_KEY: self.__variable_value,
        })
        self.system.variables[self.__variable_name] = variable

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass

    def __repr__(self) -> str:
        return f"<CreateVariableOperation operation_id={self.operation_id} variable_name={self.__variable_name} variable_value={self.__variable_value}/>"
