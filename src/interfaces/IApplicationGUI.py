from abc import ABC, abstractmethod, abstractproperty

from src.interfaces import (
    IGUIComponent,
)


class IApplicationGUI(ABC):
    """
    The IApplicationGUI class is the interface for all application GUIs in this platform. 

    Attributes:
        layouts: dict
            The dictionary which stores all layouts in this platform.
    """
    @abstractmethod
    def add_component(self, component: 'IGUIComponent') -> None:
        """
        Add a component to the GUI.

        Args:
            component: IGUIComponent
                The component which will be added to the GUI.
        """
        raise NotImplementedError

    @abstractmethod
    def load_layout(self, path: str) -> None:
        """
        Load the layout from the given path.

        Args:
            path: str
                The path to the layout file.
        """
        raise NotImplementedError

    @abstractproperty
    def layouts(self) -> dict:
        raise NotImplementedError
