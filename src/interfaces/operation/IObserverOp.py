from abc import (
    abstractproperty,
)

from src.interfaces import (
    IObserver,
)

from src.interfaces.operation import (
    ITriggerable,
)


class IObserverOp(IObserver, ITriggerable):
    """
    The Observer interface for the objects which can be observed by the 
    publisher (variables, buttons, ...). 
    """

    @abstractproperty
    def operation_id(self) -> str:
        raise NotImplementedError
