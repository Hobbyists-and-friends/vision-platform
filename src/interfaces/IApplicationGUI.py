from abc import ABC, abstractmethod, abstractproperty

from src.interfaces import (
    IGUIComponent,
)


class IApplicationGUI(ABC):
    @abstractmethod
    def add_component(self, component: 'IGUIComponent') -> None:
        raise NotImplementedError

    @abstractmethod
    def load_layout(self, path: str) -> None:
        raise NotImplementedError

    @abstractproperty
    def layouts(self) -> dict:
        raise NotImplementedError
