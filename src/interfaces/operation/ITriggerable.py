from abc import (
    ABC,
    abstractmethod,
)


class ITriggerable(ABC):
    """
    The Triggerable interface for the objects which can be triggered. It can only be executed
    when the trigger is triggered.
    """

    @abstractmethod
    def set_trigger(self, trigger_id: str) -> None:
        """
        Set the trigger of the object.

        Args:
            trigger_id: str
                The id of the trigger which is added.
        """
        raise NotImplementedError

    def is_triggered(self) -> bool:
        """
        Check if the trigger is triggered. 
        """
        raise NotImplementedError
