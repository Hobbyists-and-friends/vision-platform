from abc import (
    ABC,
    abstractmethod,
)


class IStorable(ABC):
    """
    The Storable interface for the objects which can be stored.
    """

    @abstractmethod
    def export(self) -> dict:
        """
        Export the object to a dictionary.

        Returns:
            dict: The dictionary of the object.
        """
        raise NotImplementedError

    @abstractmethod
    def load(self, data: dict) -> None:
        """
        Load the object from a dictionary.

        Args:
            data: dict
                The dictionary of the object.
        """
        raise NotImplementedError
