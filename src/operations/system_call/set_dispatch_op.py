from src.cores import *
from src.interfaces.ui import IOperationDispatcherComponent
from src.interfaces.operation import ISystemCall

from .system_call_base import SystemCallBase
from .raise_error_op import RaiseErrorOperation


class SetDispatchOperation(SystemCallBase):
    def __init__(self, operation_id: str,
                 component_id: str,
                 trigger_id: str = None):
        super().__init__(trigger_id)
        self.__operation_id = operation_id
        self.__component_id = component_id

    def load(self, data: dict) -> None:
        pass

    def export(self) -> dict:
        pass

    def _run_impl(self) -> None:
        if self.__operation_id not in System.system.operations:
            RaiseErrorOperation(
                error_message=f'Operation "{self.__operation_id}" does not exist.'
            ).run()
        elif self.__component_id not in System.system.system.ui_components:
            RaiseErrorOperation(
                error_message=f'UI component "{self.__component_id}" does not exist.'
            ).run()
        else:
            ui_component = System.system.system.ui_components[self.__component_id]
            operation = System.system.operations[self.__operation_id]

            if not isinstance(operation, ISystemCall):
                RaiseErrorOperation(
                    error_message=f'Operation "{self.__operation_id}" is not a system call.'
                ).run()
            else:
                ui_component.set_operation_id(
                    self.__operation_id
                )
