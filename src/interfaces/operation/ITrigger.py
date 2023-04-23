from abc import (
    abstractmethod,
    abstractproperty,
)
from src.interfaces.operation import (
    IStorable,
)


class ITrigger(IStorable):
    """
    The Trigger interface for the opertions' triggers wheras if the publisher is updated, but the observer
    can only be notified when the trigger returns true.
    """
    @abstractproperty
    def trigger_id(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def is_trigger(self) -> bool:
        """
        Check if the trigger is triggered. 

        Returns:
            bool: True if the trigger is triggered, vice versa.
        """
        raise NotImplementedError
