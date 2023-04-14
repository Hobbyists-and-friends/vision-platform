from src.interfaces import (
    IPublisher,
    IObserver,
    ISystem,
)

from .OperationBase import OperationBase


class AddVariableObserverOperation(OperationBase):
    def __init__(self,
                 system: 'ISystem',
                 operation_id: str,
                 variable_id: str,
                 observer_id: str,
                 store: bool = False):
        super().__init__(system, operation_id, store)
        self.__variable_id = variable_id
        self.__observer_id = observer_id

    def load(self, data: dict) -> None:
        pass

    def export(self) -> dict:
        pass

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass

    def _run(self) -> None:
        variable = self.system.variables[self.__variable_id]
        variable.add_observer(self.system.ui_components[self.__observer_id])
        variable.notify()
