from src.cores import System
from src.utils.Logging import Logging
from src.operations.system_call import *
from .system_call_base import SystemCallBase


class SetOperationRelatedVariableOperation(SystemCallBase):
    def __init__(
        self,
        operation_id: str,
        src_params_dict: dict,
        res_params_dict: dict,
        auto_mode: bool = False,
        trigger_id: str = None,
    ):
        super().__init__(trigger_id)

        self.__operation_id = operation_id
        self.__src_params_dict = src_params_dict
        self.__res_params_dict = res_params_dict
        self.__auto_mode = auto_mode

        Logging.debug(
            f"""
                      Setup Related Variables: 
                        Operation Id: {self.__operation_id}
                        Src Params: {self.__src_params_dict}
                        Res Params: {self.__res_params_dict}
        """
        )

    def load(self, data: dict) -> None:
        pass

    def export(self) -> dict:
        pass

    def __auto_create_variable(self, variable_id: str) -> None:
        if variable_id not in System.system.variables.keys() and self.__auto_mode:
            CreateVariableOperation(variable_id=variable_id).run()

    def _run_impl(self) -> None:
        Logging.debug(
            msg=f"""
                    Operation Id: {self.__operation_id} 
                    Src Params: {self.__src_params_dict}
                    Res Params: {self.__res_params_dict}
                      """
        )

        for key, variable_id in self.__res_params_dict.items():
            self.__auto_create_variable(variable_id)
            System.system.operations[self.__operation_id].set_res_variable(
                param_key=key, variable_id=variable_id
            )

        for key, variable_id in self.__src_params_dict.items():
            self.__auto_create_variable(variable_id)
            System.system.operations[self.__operation_id].set_src_variable(
                param_key=key, variable_id=variable_id
            )

        System.system.operations[self.__operation_id].observer_all_src()
