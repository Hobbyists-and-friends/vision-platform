from src.interfaces import (
    IPublisher,
)
from src.cores import (
    System,
)

from .system_call_base import SystemCallBase


class ResetSystemOperation(SystemCallBase):
    def __init__(self, trigger_id: str = None):
        super().__init__(trigger_id)

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _run_impl(self) -> None:
        System.system.variables = {}
        System.system.ui_components = {}
        System.system.operations = {}

    def __repr__(self) -> str:
        return f"<ResetSystemOperation operation_id={self.operation_id}>"
