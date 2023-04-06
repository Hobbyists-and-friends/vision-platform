from abc import abstractmethod, ABC, abstractproperty

from src.interfaces import (
    IObserver,
    IApplicationGUI,
    IPublisher
)


class IGUIComponent(IObserver, IPublisher):
    @abstractproperty
    def component_id(self) -> str:
        raise NotImplementedError
