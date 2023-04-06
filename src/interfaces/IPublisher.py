from abc import ABC, abstractmethod

from src.interfaces import IObserver


class IPublisher(ABC):
    """
    The IPublisher class is the interface for all publishers in this platform which will
    notify all observers when the publishers update their data.
    """
    @abstractmethod
    def add_observer(self, observer: 'IObserver') -> None:
        """
        Add an observer to this publisher. 

        Args:
            observer: IObserver
                The observer which will be added to this publisher.
        """
        raise NotImplementedError

    @abstractmethod
    def remove_observer(self, observer: 'IObserver') -> None:
        """
        Remove an observer from this publisher.

        Args:
            observer: IObserver
                The observer which will be removed from this publisher.
        """
        raise NotImplementedError

    @abstractmethod
    def notify(self) -> None:
        """
        Notify all observers which are subscribed to this publisher.
        """
        raise NotImplementedError
