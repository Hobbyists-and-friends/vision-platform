from src.interfaces import (
    ISystem,
    IPublisher,
)
from src.constants import (
    VALUE_KEY,
)

from .OperationBase import OperationBase


class RunApplicationOperation(OperationBase):
    def __init__(self,
                 system: 'ISystem',
                 operation_id: str,
                 application_name: str,
                 store: bool = False,
                 run_at_first: bool = True):
        super().__init__(system, operation_id, store, run_at_first)
        self.__application_name = application_name

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _run(self) -> None:
        for operation in self.system.applications[self.__application_name].data[VALUE_KEY]:
            operation.run()

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        self._run()
