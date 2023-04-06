from abc import abstractmethod, abstractproperty

from src.interfaces import (
    IObserver,
    IPublisher,
)


class IOperation(IObserver):
    """
    The IOperation class is the interface for all operations in this platform.
    Each operation must be an IObserver.

    Attributes:
        operation_id: str
            The identifier of this operation.
    """

    @abstractproperty
    def operation_id(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def export(self) -> dict:
        """
        This function will be exported to the FileSystem 

        Returns:
            dict: The data which will be exported to the FileSystem.
        """
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
