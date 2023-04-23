from abc import ABC, abstractproperty, abstractmethod


class IUIComponent(ABC):
    """
    The IUIComponent class is the interface for all UI components in this platform which will 
    be used to display the data of the variables in the system.
    """
    @abstractmethod
    def on_update(self) -> None:
        """
        The function which will be called each update loop (if using the update loop). 
        """
        raise NotImplementedError
