from abc import abstractmethod, abstractproperty

from src.interfaces import (
    IObserver,
    IPublisher,
)


class IOperation(IObserver):
    @abstractproperty
    def operation_id(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def export(self) -> dict:
        raise NotImplementedError

    @abstractmethod
    def load(self, data: dict) -> None:
        raise NotImplementedError

    @abstractmethod
    def run(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, publisher: 'IPublisher', data: dict) -> None:
        raise NotImplementedError
