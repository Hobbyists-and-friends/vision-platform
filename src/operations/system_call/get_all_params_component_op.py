from src.cores import System
from src.constants import *
from src.utils.Logging import Logging

from .system_call_base import SystemCallBase
from .change_variable_value_op import ChangeVariableValueOperation
from .raise_error_op import RaiseErrorOperation


class GetAllParamsComponentOperation(SystemCallBase):
    def __init__(
        self,
        variable_id: str,
        operation_ref: str = None,
        operation_id: str = None,
        trigger_id: str = None,
    ):
        super().__init__(trigger_id)
        self.__variable_id = variable_id
        self.__operation_id = self.__get_operation(
            operation_id=operation_id, operation_ref=operation_ref
        )

    def __get_operation(self, operation_id: str, operation_ref: str) -> str:
        if operation_id is not None:
            return operation_id
        else:
            if operation_ref is not None:
                return System.system.variables[operation_ref].data[VALUE_KEY]
            else:
                RaiseErrorOperation(
                    error_message="Need the operation Id or ref for getting all params of the operation."
                ).run()

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def _is_validate(self) -> bool:
        return self.__operation_id is not None

    def _run_impl(self) -> None:
        variable_names = System.system.operations[
            self.__operation_id
        ].src_params.values()
        components = []

        for variable_name in variable_names:
            variable = System.system.variables[variable_name]

            if RELATED_COMPONENT in variable.data:
                components.append(variable.data[RELATED_COMPONENT])

        Logging.debug(
            msg=f"""
                        Component: {components}
                      """
        )

        ChangeVariableValueOperation(
            variable_id=self.__variable_id, new_value=components
        ).run()
