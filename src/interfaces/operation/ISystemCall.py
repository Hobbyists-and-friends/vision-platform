from abc import (
    abstractmethod,
)

from src.interfaces.operation import (
    IStorable,
    ITriggerable,
)


class ISystemCall(IStorable, ITriggerable):
    """
    The System Call interface for the system calls which are creating, adding observability, ... 
    """
    @abstractmethod
    def run(self) -> None:
        """
        Execute the system call.
        """
        raise NotImplementedError
