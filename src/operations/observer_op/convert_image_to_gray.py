import cv2

from src.constants import *
from src.interfaces import IPublisher
from src.cores import System
from src.operations.system_call import *

from .observer_op_base import ObserverOpBase


class ConvertImageToGray(ObserverOpBase):
    def __init__(self, operation_id: str,
                 trigger_id: str = None):
        super().__init__(operation_id, trigger_id)

    def _update_impl(self, publisher: IPublisher, data: dict) -> None:
        src_image = System.system.variables[self._params[SRC_VARIABLE]
                                            ].data[VALUE_KEY]
        gray_image = cv2.cvtColor(src_image, cv2.COLOR_BGR2GRAY)

        if RESULT_VARIABLE in self._params:
            ChangeVariableValueOperation(
                variable_id=self._params[RESULT_VARIABLE],
                new_value=gray_image).run()

    def _verify_variable(self, param_key: str, variable_id: str) -> bool:
        if param_key == SRC_VARIABLE:
            return self.__is_image(variable_id)

        return True

    def __is_image(self, variable_id: str) -> bool:
        return System.system.variables[variable_id].type == VariableType.IMAGE or \
            System.system.variables[variable_id].type == VariableType.NULL

    @property
    def default_params(self) -> dict:
        return {}
