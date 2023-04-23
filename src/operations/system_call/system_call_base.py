from abc import abstractmethod

from src.interfaces.operation import (
    ISystemCall,
)
from src.cores import (
    System,
)


class SystemCallBase(ISystemCall):
    def __init__(self, trigger_id: str):
        self.__trigger_id = trigger_id

    def run(self) -> None:
        if self.__trigger_id is None:
            self._run_impl()
        else:
            trigger = System.system.triggers[self.__trigger_id]
            if trigger.is_trigger():
                self._run_impl()

    def set_trigger(self, trigger_id: str) -> None:
        self.__trigger_id = trigger_id

    @abstractmethod
    def _run_impl(self) -> None:
        pass
