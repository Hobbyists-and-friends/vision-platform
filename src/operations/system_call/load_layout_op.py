import os

from src.interfaces import (
    IPublisher,
)
from src.cores import (
    System,
)
from .system_call_base import SystemCallBase
from .raise_error_op import RaiseErrorOperation


class LoadLayoutOperation(SystemCallBase):
    def __init__(self, layout_name: str,
                 trigger_id: str = None):
        super().__init__(trigger_id)
        self.__layout_name = layout_name

    def export(self):
        pass

    def load(self, data):
        pass

    def _run_impl(self):
        if os.path.exists(self.__layout_name):
            System.system.application.load_layout(self.__layout_name)
        else:
            RaiseErrorOperation(
                error_message=f"File {self.__layout_name} does not exist."
            ).run()
