from abc import (
    abstractmethod,
)
from src.interfaces import (
    IOperation,
    IPublisher,
    ISystem,
)


class OperationBase(IOperation):
    def __init__(self, system: 'ISystem', operation_id: str, store: bool = False):
        self.system = system
        self.__operation_id = operation_id

    @property
    def operation_id(self) -> str:
        return self.__operation_id

    def run(self) -> None:
        self._run()

    @abstractmethod
    def _run(self) -> None:
        raise NotImplementedError
