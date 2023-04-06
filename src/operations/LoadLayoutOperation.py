import os

from src.interfaces import (
    IOperation,
    IPublisher,
)
from .OperationBase import OperationBase


class LoadLayoutOperation(OperationBase):
    def __init__(self, system, operation_id: str, layout_name: str):
        super().__init__(system, operation_id)
        self.__layout_name = layout_name

    def export(self):
        pass

    def load(self, data):
        pass

    def _run(self):
        if os.path.exists(self.__layout_name):
            self.system.application.load_layout(self.__layout_name)

    def update(self, publisher: 'IPublisher', data: dict):
        pass
