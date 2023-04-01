from abc import ABC, abstractmethod

from src.interfaces import IPublisher


class IObserver(ABC):
    @abstractmethod
    def update(self, publisher: 'IPublisher', data: dict):
        raise NotImplementedError
