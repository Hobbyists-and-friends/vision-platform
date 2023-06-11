from src.cores import (
    System,
)
from src.constants import (
    OperationType,
)
from src.utils.Logging import Logging
from .system_call_base import SystemCallBase
from .raise_error_op import RaiseErrorOperation
from .print_value_op import PrintValueOperation
from .get_all_params_component_op import GetAllParamsComponentOperation

from src.operations.observer_op import *


class CreateOperationOperation(SystemCallBase):
    def __init__(
        self, operation_id: str, operation_type: str, trigger_id: str = None, **kwargs
    ):
        super().__init__(trigger_id)

        self.__operation_id = operation_id
        self.__operation_type = operation_type
        self.__kwargs = kwargs

    def load(self, data: dict) -> None:
        pass

    def export(self) -> dict:
        pass

    def _run_impl(self) -> None:
        if self.__operation_id in System.system.operations:
            RaiseErrorOperation(
                error_message=f"Operation {self.__operation_id} already exists",
            ).run()
            return

        if self.__operation_type == OperationType.PRINT_VARIABLE.value:
            System.system.operations[self.__operation_id] = PrintValueOperation(
                variable_id=self.__kwargs["variable_id"],
            ).run()
        if self.__operation_type == OperationType.GET_PARAMS_FROM_OBSERVER.value:
            System.system.operations[
                self.__operation_id
            ] = GetAllParamsComponentOperation(
                variable_id=self.__kwargs["variable_id"],
                operation_id=self.__kwargs["operation_target"],
            )
            System.system.operations[self.__operation_id].run()
            Logging.debug(
                msg=f"""
                    Operation Id: {self.__operation_id}, 
                    Variable Id: {self.__kwargs['variable_id']},
                    Operation Target: {self.__kwargs['operation_target']}
                    Operations: {System.system.operations.keys()}
                """
            )
        elif self.__operation_type == OperationType.LOG_VARIABLE.value:
            System.system.operations[self.__operation_id] = LogVariable(
                operation_id=self.__operation_id,
            )
        elif self.__operation_type == OperationType.CONVERT_IMAGE_TO_GRAY.value:
            System.system.operations[self.__operation_id] = ConvertImageToGray(
                operation_id=self.__operation_id,
            )
        elif self.__operation_type == OperationType.CONVERT_IMAGE_TO_BINARY.value:
            System.system.operations[self.__operation_id] = ConvertImageToBinary(
                operation_id=self.__operation_id
            )
        elif self.__operation_type == OperationType.TRANSFORM_VARIABLE_TO_VALUE.value:
            System.system.operations[self.__operation_id] = TransformVariableToValue(
                operation_id=self.__operation_id,
            )
        elif self.__operation_type == OperationType.GET_PARAM_FROM_MULTI_OBSERVER.value:
            System.system.operations[self.__operation_id] = GetParamFromMultiObserver(
                operation_id=self.__operation_id,
            )

        elif self.__operation_type == OperationType.GET_ALL_COMPONENTS.value:
            System.system.operations[
                self.__operation_id
            ] = GetAllComponentsFromOperationOperation(
                operation_id=self.__operation_id,
            )
