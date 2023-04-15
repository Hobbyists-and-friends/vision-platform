from src.interfaces import (
    ISystem,
    IPublisher,
)
from src.constants import (
    VALUE_KEY,
)
import cv2
from src.operations import (
    ChangeVariableValueOperation,
    AddVariableObserverOperation,
)

from .OperationBase import OperationBase


class ConvertImageToBinaryOperation(OperationBase):
    def __init__(self,
                 system: 'ISystem',
                 operation_id: str,
                 source_variable_id: str,
                 result_variable_id: str,
                 threshold_variable_id: str,
                 store: bool = False,
                 run_at_first: bool = True):
        super().__init__(system, operation_id, store, run_at_first)
        self.__source_variable_id = source_variable_id
        self.__result_variable_id = result_variable_id
        self.__threshold_variable_id = threshold_variable_id

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _run(self) -> None:
        img = self.system.variables[self.__source_variable_id].data[VALUE_KEY]
        threshold = self.system.variables[self.__threshold_variable_id].data[VALUE_KEY]

        ret, bin_img = cv2.threshold(img, thresh=threshold,
                                     maxval=255, type=cv2.THRESH_BINARY)

        ChangeVariableValueOperation(
            self.system,
            operation_id=self.operation_id + '1',
            variable_id=self.__result_variable_id,
            new_value=bin_img,
        ).run()

    def update(self, publisher: 'IPublisher', data: dict) -> None:
        self._run()
