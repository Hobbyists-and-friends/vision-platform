from src.interfaces import (
    IPublisher,
    IObserver,
)


class PublisherBase(IPublisher):
    def __init__(self, **kwargs):
        self.__observers = []
        self._dict = kwargs

    def add_observer(self, observer: 'IObserver') -> None:
        if observer not in self.__observers:
            self.__observers.append(observer)
            # observer.update(self, self._dict)

    def remove_observer(self, observer: 'IObserver') -> None:
        if observer in self.__observers:
            self.__observers.remove(observer)

    def notify(self) -> None:
        for observer in self.__observers:
            observer.update(self, self._dict)
