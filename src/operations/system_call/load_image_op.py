import cv2 as cv
import os

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

from .system_call_base import SystemCallBase
from .change_variable_value_op import ChangeVariableValueOperation
from .raise_error_op import RaiseErrorOperation


class LoadImageOperation(SystemCallBase):
    def __init__(self,
                 variable_id: str,
                 image_path_variable_id: str,
                 trigger_id: str = None):
        super().__init__(trigger_id)
        self.__variable_id = variable_id
        self.__image_path_variable_id = image_path_variable_id

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _run_impl(self) -> None:
        file_name = System.system.variables[self.__image_path_variable_id].data[VALUE_KEY]
        if os.path.isfile(file_name):
            image = cv.imread(
                System.system.variables[self.__image_path_variable_id].data[VALUE_KEY])
            image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

            ChangeVariableValueOperation(
                variable_id=self.__variable_id,
                new_value=image,
            ).run()
        else:
            RaiseErrorOperation(
                error_message=f"File {file_name} does not exist."
            ).run()
