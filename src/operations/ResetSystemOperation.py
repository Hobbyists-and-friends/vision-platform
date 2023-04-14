from src.interfaces import (
    ISystem,
    IPublisher,
)

from .OperationBase import OperationBase


class ResetSystemOperation(OperationBase):
    def __init__(self,
                 system: 'ISystem',
                 operation_id: str,
                 store: bool = False):
        super().__init__(system, operation_id, store)

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _run(self) -> None:
        self.system.variables = {}
        self.system.ui_components = {}
        self.system.operations = {}

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass

    def __repr__(self) -> str:
        return f"<ResetSystemOperation operation_id={self.operation_id}>"
