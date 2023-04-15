import cv2

from src.interfaces import (
    ISystem,
    IPublisher,
)
from src.constants import (
    VALUE_KEY,
)
from .ChangeVariableValueOperation import ChangeVariableValueOperation
from .OperationBase import OperationBase


class ConvertImageToGrayOperation(OperationBase):
    def __init__(self,
                 system: 'ISystem',
                 operation_id: str,
                 source_variable_id: str,
                 result_variable_id: str,
                 store: bool = False,
                 run_at_first: bool = True):
        super().__init__(system, operation_id, store, run_at_first)
        self.__source_variable_id = source_variable_id
        self.__result_variable_id = result_variable_id

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _run(self) -> None:
        image = self.system.variables[self.__source_variable_id].data[VALUE_KEY]

        if image is not None:
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            ChangeVariableValueOperation(
                self.system,
                operation_id=self.operation_id + "_change_result",
                variable_id=self.__result_variable_id,
                new_value=gray_image,
            ).run()

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        self._run()
