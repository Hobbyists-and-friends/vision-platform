import cv2

from src.constants import *
from src.cores import System
from src.interfaces import IPublisher
from src.operations.system_call import *

from .observer_op_base import ObserverOpBase


class ConvertImageToBinary(ObserverOpBase):
    def __init__(self,
                 operation_id: str,
                 trigger_id: str = None):
        super().__init__(operation_id, trigger_id)

    def _update_impl(self, publisher: 'IPublisher', data: dict) -> None:
        src_image = System.system.variables[self._params[SRC_VARIABLE]
                                            ].data[VALUE_KEY]
        threshold = System.system.variables[self._params[THRESHOLD_VARIABLE]
                                            ].data[VALUE_KEY]

        ret, binary_image = cv2.threshold(
            src_image, threshold, 255, cv2.THRESH_BINARY)

        ChangeVariableValueOperation(
            variable_id=self._params[RESULT_VARIABLE],
            new_value=binary_image
        ).run()

    def _verify_variable(self, param_key: str, variable_id: str) -> bool:
        return True
