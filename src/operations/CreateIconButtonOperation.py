from src.interfaces import (
    IOperation,
    IPublisher,
    ISystem,
)
from src.gui.customs import (
    IconButton,
)
from .OperationBase import OperationBase


class CreateIconButtonOpeartion(OperationBase):
    def __init__(self, system: 'ISystem',
                 operation_id: str,
                 name: str,
                 store=False):
        super().__init__(system, operation_id, store=store)
        self.__name = name

    def _run(self) -> None:
        component = IconButton(self.__name, self.system)
        self.system.add_ui_component(component)

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass

    def load(self, data: dict) -> None:
        pass

    def export(self) -> dict:
        pass
