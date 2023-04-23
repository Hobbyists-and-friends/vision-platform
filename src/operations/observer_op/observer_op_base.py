from abc import (
    abstractmethod,
)

from src.interfaces import (
    IPublisher,
)
from src.interfaces.operation import (
    IObserverOp,
)
from src.operations.OperationBase import (
    OperationBase,
)


class ObserverOpBase(OperationBase, IObserverOp):
    def __init__(self, trigger_id: str, operation_id: str):
        super().__init__(trigger_id)
        self.__operation_id = operation_id

    @property
    def operation_id(self) -> str:
        return self.__operation_id

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        self._update_impl(publisher, data)

    @abstractmethod
    def _update_impl(self, publisher: 'IPublisher', data: dict) -> None:
        raise NotImplementedError
