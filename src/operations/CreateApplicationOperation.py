from typing import (
    List,
)

from src.interfaces import (
    ISystem,
    IPublisher,
    IOperation,
)
from src.cores import (
    Variable,
)
from src.constants import (
    NAME_KEY,
    VALUE_KEY,
)
from .OperationBase import OperationBase
from .ResetSystemOperation import ResetSystemOperation


class CreateApplicationOperation(OperationBase):
    def __init__(self,
                 system: 'ISystem',
                 operation_id: str,
                 application_name: str,
                 operations: List['IOperation'] = [],
                 store: bool = False):
        super().__init__(system, operation_id, store)
        self.__application_name = application_name
        self.__operations = operations

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _run(self) -> None:
        operations = [
            ResetSystemOperation(
                system=self.system,
                operation_id='reset_system_operation_id',
            )
        ] + self.__operations
        application = Variable(
            system=self.system,
            **{
                NAME_KEY: self.__application_name,
            },
            value=operations,
        )
        self.system.applications[self.__application_name] = application

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass
