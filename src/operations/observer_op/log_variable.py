from src.interfaces import (
    ISystem,
    IPublisher,
)
from src.cores import (
    System,
)
from src.constants import (
    VALUE_KEY,
)
from .observer_op_base import ObserverOpBase


class LogVariable(ObserverOpBase):
    def __init__(self, trigger_id: str = None):
        super().__init__(trigger_id)

    def _update_impl(self, publisher: 'IPublisher', data: dict) -> None:
        print(data[VALUE_KEY])

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _verify_variable(self, param_key: str, variable_id: str) -> bool:
        pass
