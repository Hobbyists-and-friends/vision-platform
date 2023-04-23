from abc import (
    abstractmethod,
)
from src.interfaces.operation import (
    ITriggerable,
)
from src.cores import (
    System,
)


class OperationBase(ITriggerable):
    """
    The OperationBase class is the base class for all operations in this platform which will
    be used to execute the operations in the system.

    Attributes:
        system: ISystem
            The system which is passed to all objects in this platform. 

        operation_id: str
            The ID of this operation.

        store: bool
            The flag to store this operation to the system, default is False.
    """

    def __init__(self, trigger_id: str):
        self.__trigger_id = trigger_id

    def set_trigger(self, trigger_id: str) -> None:
        self.__trigger_id = trigger_id

    def is_triggered(self) -> bool:
        return True
