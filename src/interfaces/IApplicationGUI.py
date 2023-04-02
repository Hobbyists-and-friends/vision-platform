from abc import ABC, abstractmethod

from src.interfaces import (
    IGUIComponent,
)


class IApplicationGUI(ABC):
    @abstractmethod
    def add_component(self, component: IGUIComponent, layout_name: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def load_layout(self, path: str) -> None:
        raise NotImplementedError
