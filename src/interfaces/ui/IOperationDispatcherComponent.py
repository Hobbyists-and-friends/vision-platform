from abc import abstractmethod
from .IUIComponent import IUIComponent


class IOperationDispatcherComponent(IUIComponent):
    """
    The IOperationDispatcherComponent class is the interface for all operation dispatcher
    components in this platform which will be used to dispatch the operations 
    (which is stored in the system). 
    """

    @abstractmethod
    def dispatch(self, operation_id: str) -> None:
        """
        Dispatch an operation by operation_id.

        Args:
            operation_id: str
                The id of the operation which will be dispatched.
        """
        raise NotImplementedError

    @abstractmethod
    def set_operation_id(self, operation_id: str) -> None:
        """
        Dispatch an operation by operation_id. 
        """
        raise NotImplementedError
