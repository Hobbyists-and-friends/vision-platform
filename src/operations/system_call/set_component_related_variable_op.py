from src.cores import (
    System,
)
from src.constants import *

from .system_call_base import SystemCallBase
from .create_variable_op import CreateVariableOperation
from .raise_error_op import RaiseErrorOperation


class SetComponentRelatedVariableOperation(SystemCallBase):
    def __init__(
        self,
        component_id: str,
        src_params: dict,
        res_params: dict,
        auto_mode: bool = False,
        trigger_id: str = None,
    ):
        super().__init__(trigger_id)
        self.__component_id = component_id
        self.__src_params = src_params
        self.__res_params = res_params
        self.__auto_mode = auto_mode

    def load(self, data: dict) -> None:
        pass

    def export(self) -> dict:
        pass

    def __auto_create_variable(self, variable_id: str) -> None:
        if self.__auto_mode and variable_id not in System.system.variables.keys():
            CreateVariableOperation(variable_id=variable_id).run()

    def _run_impl(self) -> None:
        for key, variable_id in self.__res_params.items():
            self.__auto_create_variable(variable_id)
            if variable_id not in System.system.variables:
                RaiseErrorOperation(
                    error_message=f"Variable {variable_id} does not exist"
                ).run()
            else:
                System.system.ui_components[self.__component_id].set_res_variable(
                    param_key=key, variable_id=variable_id
                )
                System.system.variables[variable_id].data[
                    RELATED_COMPONENT
                ] = self.__component_id

        for key, variable_id in self.__src_params.items():
            self.__auto_create_variable(variable_id)
            if variable_id not in System.system.variables:
                RaiseErrorOperation(
                    error_message=f"Variable {variable_id} does not exist"
                ).run()
            else:
                System.system.ui_components[self.__component_id].set_src_variable(
                    param_key=key, variable_id=variable_id
                )
                System.system.variables[variable_id].data[
                    RELATED_COMPONENT
                ] = self.__component_id

            System.system.ui_components[self.__component_id].observer_all_src()
