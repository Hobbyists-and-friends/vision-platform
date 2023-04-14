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
                 component_id: str,
                 text: str,
                 store=False):
        super().__init__(system, operation_id, store=store)
        self.__component_id = component_id
        self.__text = text

    def _run(self) -> None:
        component = IconButton(self.system, self.__component_id, self.__text)
        self.system.ui_components[component.component_id] = component

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass

    def load(self, data: dict) -> None:
        pass

    def export(self) -> dict:
        pass
