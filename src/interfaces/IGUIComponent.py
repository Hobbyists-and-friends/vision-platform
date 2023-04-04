from abc import abstractmethod, ABC, abstractproperty

from src.interfaces import (
    IObserver,
    IApplicationGUI,
)


class IGUIComponent(IObserver):
    @abstractproperty
    def component_id(self) -> str:
        raise NotImplementedError
