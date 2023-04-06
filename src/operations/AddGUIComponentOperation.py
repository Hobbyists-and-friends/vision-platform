from src.interfaces import (
    ISystem,
    IOperation,
    IVariable,
    IGUIComponent,
    IPublisher,
)
from .OperationBase import OperationBase


class AddGUIComponentOperation(OperationBase):
    def __init__(self, system: 'ISystem',
                 component_id: str,
                 ui_component_id: str,
                 layout: str,
                 store: bool = False) -> None:
        super().__init__(system, component_id, store=store)
        self.__layout = layout
        self.__ui_component_id = ui_component_id

    def load(self, data: dict) -> None:
        pass

    def export(self) -> dict:
        pass

    def _run(self) -> None:
        self.system.application.add_component(
            self.system.ui_components[self.__ui_component_id], self.__layout)

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass
