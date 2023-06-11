from src.utils.Logging import Logging
from src.interfaces import (
    ISystem,
    IPublisher,
)
from src.cores import (
    System,
)
from src.constants import *
from .observer_op_base import ObserverOpBase


class LogVariable(ObserverOpBase):
    def __init__(self, operation_id: str, trigger_id: str = None):
        super().__init__(operation_id, trigger_id)

    def _update_impl(self, publisher: "IPublisher", data: dict) -> None:
        variable_value = self._get_params_value(param_key=SRC_VARIABLE)
        Logging.info(msg=f"Variable Value: {variable_value}")

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _verify_variable(self, param_key: str, variable_id: str) -> bool:
        return True

    @property
    def default_params(self) -> dict:
        return {}
