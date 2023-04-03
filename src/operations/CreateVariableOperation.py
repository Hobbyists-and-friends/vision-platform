from src.interfaces import (
    IOperation,
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


class CreateVariableOperation(IOperation):
    def __init__(self, system: 'ISystem',
                 operation_id: str,
                 variable_name: str,
                 variable_value: object = None):
        self.system = system
        self.__operation_id = operation_id
        self.__variable_name = variable_name
        self.__variable_value = variable_value

    @property
    def operation_id(self) -> str:
        return self.__operation_id

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def run(self, publisher: 'IPublisher' = None, data: dict = None) -> None:
        if self.__variable_name in self.system.variables.keys():
            return
        variable = Variable(self.system, **{
            NAME_KEY: self.__variable_name,
            VALUE_KEY: self.__variable_value,
        })
        self.system.add_variable(variable)

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass

    def __repr__(self) -> str:
        return f"<CreateVariableOperation operation_id={self.operation_id} variable_name={self.__variable_name} variable_value={self.__variable_value}/>"
