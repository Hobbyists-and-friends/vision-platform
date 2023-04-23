from src.cores import System

from src.operations.system_call import *
from .system_call_base import SystemCallBase


class SetOperationRelatedVariableOperation(SystemCallBase):
    def __init__(self, operation_id: str,
                 src_params_dict: dict,
                 res_params_dict: dict,
                 trigger_id: str = None):
        super().__init__(trigger_id)

        self.__operation_id = operation_id
        self.__src_params_dict = src_params_dict
        self.__res_params_dict = res_params_dict

    def load(self, data: dict) -> None:
        pass

    def export(self) -> dict:
        pass

    def _run_impl(self) -> None:
        for key, variable_id in self.__res_params_dict.items():
            System.system.operations[self.__operation_id].set_res_variable(
                param_key=key,
                variable_id=variable_id
            )

        for key, variable_id in self.__src_params_dict.items():
            System.system.operations[self.__operation_id].set_src_variable(
                param_key=key,
                variable_id=variable_id
            )

        System.system.operations[self.__operation_id].observer_all_src()
