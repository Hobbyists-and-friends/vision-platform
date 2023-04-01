from abc import abstractmethod, abstractproperty

from src.interfaces import IObserver


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
