from src.interfaces import (
    IOperation,
    IPublisher,
    ISystem,
)
from src.gui.customs import (
    IconButton,
)


class CreateIconButtonOpeartion(IOperation):
    def __init__(self, system: 'ISystem',
                 operation_id: str,
                 name: str):
        self.__operation_id = operation_id
        self.system = system
        self.__name = name

    @property
    def operation_id(self) -> str:
        return self.__operation_id

    def run(self, publisher: 'IPublisher' = None, data: dict = None) -> None:
        component = IconButton(self.__name, self.system)
        self.system.add_ui_component(component)

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        self.run(publisher, data)

    def load(self, data: dict) -> None:
        pass

    def export(self) -> dict:
        pass
