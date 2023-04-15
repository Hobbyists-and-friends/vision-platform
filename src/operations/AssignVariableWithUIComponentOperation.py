from src.interfaces import (
    ISystem,
    IPublisher,
)

from .OperationBase import OperationBase
from .AddVariableObserverOperation import AddVariableObserverOperation


class AssignVariableWithUIComponentOperation(OperationBase):
    def __init__(self,
                 system: 'ISystem',
                 operation_id: str,
                 variable_id: str,
                 component_id: str,
                 store: bool = False,
                 run_at_first: bool = True):
        super().__init__(system, operation_id, store, run_at_first)
        self.__variable_id = variable_id
        self.__component_id = component_id

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _run(self) -> None:
        AddVariableObserverOperation(
            system=self.system,
            operation_id="Add Observer for variable",
            variable_id=self.__variable_id,
            observer_id=self.__component_id,
        )

        self.system.ui_components[self.__component_id].set_variable_id(
            self.__variable_id)

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass
