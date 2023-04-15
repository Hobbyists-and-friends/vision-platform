from src.interfaces import (
    ISystem,
    IPublisher,
)
from src.gui.customs import (
    ImageDisplay,
)

from .OperationBase import OperationBase


class CreateImageDisplayOperation(OperationBase):
    def __init__(self,
                 system: 'ISystem',
                 operation_id: str,
                 component_id: str,
                 variable_id: str,
                 store: bool = False,
                 run_at_first: bool = True):
        super().__init__(system, operation_id, store, run_at_first)
        self.__variable_id = variable_id
        self.__component_id = component_id

    def load(self, data: dict) -> None:
        pass

    def export(self) -> dict:
        pass

    def _run(self) -> None:
        image_display = ImageDisplay(
            system=self.system,
            component_id=self.__component_id,
            variable_id=self.__variable_id,
        )
        self.system.ui_components[self.__component_id] = image_display

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass
