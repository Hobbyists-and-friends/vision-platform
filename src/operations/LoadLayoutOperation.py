import os

from src.interfaces import (
    IOperation,
    IPublisher,
    ISystem,
)
from .OperationBase import OperationBase


class LoadLayoutOperation(OperationBase):
    def __init__(self,
                 system: 'ISystem',
                 operation_id: str,
                 layout_name: str,
                 store=False):
        super().__init__(system, operation_id, store=store)
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
