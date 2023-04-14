import cv2 as cv

from src.cores import (
    System,
)
from src.interfaces import (
    ISystem,
    IPublisher,
)
from src.constants import (
    VALUE_KEY,
)

from src.operations import (
    ChangeVariableValueOperation,
)

from .OperationBase import OperationBase


class LoadImageOperation(OperationBase):
    def __init__(self,
                 system: 'ISystem',
                 operation_id: str,
                 variable_id: str,
                 image_path_variable_id: str,
                 store: bool = False):
        super().__init__(system, operation_id, store)
        self.__variable_id = variable_id
        self.__image_path_variable_id = image_path_variable_id

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        pass

    def _run(self) -> None:
        image = cv.imread(
            self.system.variables[self.__image_path_variable_id].data[VALUE_KEY])
        image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

        ChangeVariableValueOperation(
            system=self.system,
            operation_id="ChangeVariableValueOperation for {self.operation_id}}",
            variable_id=self.__variable_id,
            new_value=image,
        ).run()
