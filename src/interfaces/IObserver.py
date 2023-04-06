from abc import ABC, abstractmethod

from src.interfaces import IPublisher


class IObserver(ABC):
    """
    The IObserver class is the interface for all observers in this platform which will 
    be notified by publishers when the publishers update their data.
    """
    @abstractmethod
    def update(self, publisher: 'IPublisher', data: dict) -> None:
        """
        Update the data of this observer.

        Args:
            publisher: IPublisher
                The publisher which will notify this observer.

            data: dict
                The data which will be updated to this observer.
        """
        raise NotImplementedError
