from abc import abstractmethod, ABC, abstractproperty

from src.interfaces import (
    IObserver,
    IApplicationGUI,
    IPublisher
)


class IGUIComponent(IObserver, IPublisher):
    """
    The IGUIComponent class is the interface for all ui components in this platform.
    Each ui component must be an IObserver and IPubliser.

    Attributes:
        component_id: str
            The identifier of this component.
    """
    @abstractproperty
    def component_id(self) -> str:
        raise NotImplementedError
