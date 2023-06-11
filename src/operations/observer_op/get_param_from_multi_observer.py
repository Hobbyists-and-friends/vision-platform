from src.interfaces import IPublisher
from src.cores import System
from src.constants import *
from src.operations.system_call import *

from .observer_op_base import ObserverOpBase


class GetParamFromMultiObserver(ObserverOpBase):
    def __init__(self, operation_id: str, trigger_id: str = None):
        super().__init__(operation_id, trigger_id)

    def _update_impl(self, publisher: IPublisher, data: dict) -> None:
        operation_id = self._get_params_value(SRC_OPERATION)

        if isinstance(operation_id, list):
            RaiseErrorOperation(
                error_message=f"Operation {operation_id} is not a list. <GetParamFromMultiObserver operation={operation_id}>",
            ).run()
            return

        if operation_id is not None:
            operation = System.system.operations[operation_id]
            params = self._get_params_value(PARAM_VALUE)

            if isinstance(params, list):
                param_variable_names = [operation.params[param] for param in params]
            else:
                param_variable_names = operation.params[params]

            print("[Working] Change value here")
            ChangeVariableValueOperation(
                variable_id=self._get_params_value(RESULT_VARIABLE),
                new_value=param_variable_names,
            ).run()

    def _verify_variable(self, param_key: str, variable_id: str) -> None:
        return True

    @property
    def default_params(self) -> dict:
        return {PARAM_VALUE: [SRC_VARIABLE]}
