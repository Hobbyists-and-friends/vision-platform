from abc import (
    abstractmethod,
    abstractproperty,
)
from src.interfaces.operation import (
    IStorable,
)


class IApplication(IStorable):
    """
    The System Call container, which is the main entry point of the application. 
    """
    @abstractproperty
    def application_id(self) -> str:
        """
        Get the id of the application.

        Returns:
            str: The id of the application.
        """
        raise NotImplementedError

    @abstractmethod
    def run(self) -> None:
        """
        Run the application.
        """
        raise NotImplementedError
