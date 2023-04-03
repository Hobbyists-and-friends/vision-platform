import os

from src.interfaces import (
    IOperation,
    IPublisher,
)


class LoadLayoutOperation(IOperation):
    def __init__(self, system, operation_id: str, layout_name: str):
        self.system = system
        self.__operation_id = operation_id
        self.__layout_name = layout_name

    @property
    def operation_id(self) -> str:
        return self.__operation_id

    def export(self):
        pass

    def load(self, data):
        pass

    def run(self, publisher: 'IPublisher' = None, data: dict = None):
        print(os.path.exists(self.__layout_name), self.__layout_name)
        if os.path.exists(self.__layout_name):
            self.system.application.load_layout(self.__layout_name)

    def update(self, publisher: 'IPublisher', data: dict):
        pass
