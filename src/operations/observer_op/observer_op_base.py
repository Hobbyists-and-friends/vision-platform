from abc import (
    abstractmethod,
    abstractproperty,
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


class ObserverOpBase(OperationBase, IObserverOp):
    def __init__(self, operation_id: str = None,
                 trigger_id: str = None):
        super().__init__(trigger_id)
        self._params = {}
        self._src_params = {}
        self.__operation_id = operation_id

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        self._update_impl(publisher, data)

    @abstractmethod
    def _update_impl(self, publisher: 'IPublisher', data: dict) -> None:
        raise NotImplementedError

    def set_src_variable(self, param_key: str, variable_id: str) -> None:
        if self._verify_variable(param_key, variable_id):
            self._params[param_key] = variable_id
            self._src_params[param_key] = variable_id

            if param_key in self.default_params:
                ChangeVariableValueOperation(
                    variable_id=variable_id,
                    new_value=self.default_params[param_key]
                ).run()
        else:
            RaiseErrorOperation(
                error_message=f"Variable {variable_id} is not valid for {param_key}"
            ).run()

    def set_res_variable(self, param_key: str, variable_id: str) -> None:
        if self._verify_variable(param_key, variable_id):
            self._params[param_key] = variable_id

    @abstractmethod
    def _verify_variable(self, param_key: str, variable_id: str) -> bool:
        raise NotImplementedError

    def observer_all_src(self) -> None:
        for variable_id in self._src_params.values():
            AddVariableObserverOperation(
                variable_id=variable_id,
                observer_id=self.__operation_id
            ).run()

    @abstractproperty
    def default_params(self) -> dict:
        raise NotImplementedError

    def _get_params_value(self, param_key: str) -> object:
        if param_key in self._params:
            return System.system.variables[self._params[param_key]].data[VALUE_KEY]
        else:
            return self.default_params[param_key]
