from src.constants import *
from src.cores import System
from src.operations.system_call import *
from src.interfaces import (
    IPublisher,
)

from .observer_op_base import ObserverOpBase


class TransformVariableToValue(ObserverOpBase):
    def __init__(self,
                 operation_id: str = None,
                 trigger_id: str = None):
        super().__init__(operation_id, trigger_id)
        self.__operation_id = operation_id
        self.__observe_image_variable = None

    def _update_impl(self, publisher: 'IPublisher', data: dict) -> None:
        image_variable_name = self._get_params_value(SRC_VARIABLE)
        self._params[IMAGE_SRC] = image_variable_name

        if image_variable_name is not None:
            AddVariableObserverOperation(
                variable_id=image_variable_name,
                observer_id=self.__operation_id,
                update=False,
            ).run()
            image = self._get_params_value(IMAGE_SRC)
            ChangeVariableValueOperation(
                variable_id=self._params[RESULT_VARIABLE],
                new_value=image,
            ).run()

    def _verify_variable(self, param_key: str, variable_id: str) -> None:
        return True

    @property
    def default_params(self) -> dict:
        return {}
