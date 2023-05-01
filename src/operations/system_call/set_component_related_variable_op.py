from src.cores import (
    System,
)

from .system_call_base import SystemCallBase


class SetComponentRelatedVariableOperation(SystemCallBase):
    def __init__(self,
                 component_id: str,
                 src_params: dict,
                 res_params: dict,
                 trigger_id: str = None):
        super().__init__(trigger_id)
        self.__component_id = component_id
        self.__src_params = src_params
        self.__res_params = res_params

    def load(self, data: dict) -> None:
        pass

    def export(self) -> dict:
        pass

    def _run_impl(self) -> None:
        for key, variable_id in self.__res_params.items():
            System.system.ui_components[self.__component_id].set_res_variable(
                param_key=key,
                variable_id=variable_id
            )

        for key, variable_id in self.__src_params.items():
            System.system.ui_components[self.__component_id].set_src_variable(
                param_key=key,
                variable_id=variable_id
            )

        System.system.ui_components[self.__component_id].observer_all_src()
