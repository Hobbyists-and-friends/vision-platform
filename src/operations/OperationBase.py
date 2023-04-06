from abc import (
    abstractmethod,
)
from src.interfaces import (
    IOperation,
    IPublisher,
    ISystem,
)


class OperationBase(IOperation):
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

    def __init__(self, system: 'ISystem', operation_id: str, store: bool = False):
        self.system = system
        self.__operation_id = operation_id
        self.__store = store

    @property
    def operation_id(self) -> str:
        return self.__operation_id

    def run(self) -> None:
        """
        The run method will be called to execute this operation. 
        """
        if self.__store:
            self.system.add_operation(self)
        self._run()

    @abstractmethod
    def _run(self) -> None:
        """
        The abstract method _run will be called to execute this operation. 
        """
        raise NotImplementedError
