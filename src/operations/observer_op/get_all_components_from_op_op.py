from src.interfaces import IPublisher
from src.constants import *
from src.operations.system_call.get_all_params_component_op import (
    GetAllParamsComponentOperation,
)
from .observer_op_base import ObserverOpBase


class GetAllComponentsFromOperationOperation(ObserverOpBase):
    def __init__(self, operation_id: str = None, trigger_id: str = None):
        super().__init__(operation_id, trigger_id)

    def _update_impl(self, publisher: "IPublisher", data: dict) -> None:
        GetAllParamsComponentOperation(
            operation_id=self._get_params_value(OPERATION_REF),
            variable_id=self._params[RESULT_VARIABLE],
        ).run()

    def _verify_variable(self, param_key: str, variable_id: str) -> None:
        return True

    @property
    def default_params(self) -> dict:
        return {
            OPERATION_REF: None,
            SRC_OPERATION: None,
        }
