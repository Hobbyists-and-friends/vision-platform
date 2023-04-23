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
from ..OperationBase import OperationBase


class LogVariable(OperationBase):
    def __init__(self, trigger_id: str = None):
        super().__init__(trigger_id)

    def _run(self) -> None:
        pass

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        print(data[VALUE_KEY])

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass
