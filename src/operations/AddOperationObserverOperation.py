from src.interfaces import (
    ISystem,
    IPublisher,
)

from .OperationBase import OperationBase


class AddOperationObserverOperation(OperationBase):
    def __init__(self,
                 system: 'ISystem',
                 operation_id: str,
                 observer_opertion_id: str,
                 observer_ui_component_id: str,
                 store: bool = False):
        super().__init__(system, operation_id, store)
        self.__observer_opertion_id = observer_opertion_id
        self.__observer_ui_component_id = observer_ui_component_id

    def _run(self) -> None:
        self.system.ui_components[self.__observer_ui_component_id].add_observer(
            self.system.operations[self.__observer_opertion_id]
        )

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass
