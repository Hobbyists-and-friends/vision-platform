from abc import (
    abstractproperty,
    abstractmethod,
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
    @abstractmethod
    def set_src_variable(self, param_key: str, variable_id: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def set_res_variable(self, param_key: str, variable_id: str) -> None:
        raise NotImplementedError

    @abstractmethod
    def observer_all_src(self) -> None:
        raise NotImplementedError
