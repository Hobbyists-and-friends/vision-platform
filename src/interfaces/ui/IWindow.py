from abc import ABC, abstractmethod


class IWindow(ABC):
    """
    The interface of the window in this platform which is used to display the UI components.
    """

    @abstractmethod
    def init(self):
        """
        The preconfigurations of the window in this platform.
        """
        raise NotImplementedError

    @abstractmethod
    def exit(self):
        """
        Delete the window in this platform.
        """
        raise NotImplementedError

    @abstractmethod
    def update(self):
        """
        Update the window in this platform. (If using the while loop)
        """
        raise NotImplementedError

    @abstractmethod
    def load_layout(self, layout: str):
        """
        Load the layout of the window in this platform.

        Args:
            layout: str
                The layout of the window in this platform.
        """
        raise NotImplementedError

    @abstractmethod
    def add_component(self, component_id: str):
        """
        Add a component by component_id to the window in this platform.

        Args:
            component_id: str
                The id of the component which will be added to the window(from system object).
        """
        raise NotImplementedError

    @abstractmethod
    def clear(self):
        """
        Clear all components in the window in this platform.
        """
        raise NotImplementedError
