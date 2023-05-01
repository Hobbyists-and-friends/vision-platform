from abc import (
    abstractmethod,
    abstractproperty,
)

from src.utils.MultiObserverBase import (
    MultiObserverBase,
)
from src.interfaces import (
    IPublisher,
)
from src.cores import System
from src.constants import *
from src.interfaces.operation import (
    IObserverOp,
)
from src.operations.OperationBase import (
    OperationBase,
)
from src.operations.system_call import *


class ObserverOpBase(OperationBase, MultiObserverBase, IObserverOp):
    def __init__(self, operation_id: str = None,
                 trigger_id: str = None):
        super().__init__(trigger_id)
        MultiObserverBase.__init__(self, observer_id=operation_id,
                                   observer_class=AddVariableObserverOperation,
                                   change_value_class=ChangeVariableValueOperation,
                                   raise_error_class=RaiseErrorOperation)
        self._params = {}
        self._src_params = {}
        self.__operation_id = operation_id

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        self._update_impl(publisher, data)

    @abstractmethod
    def _update_impl(self, publisher: 'IPublisher', data: dict) -> None:
        raise NotImplementedError
