from src.cores import (
    System,
)
from src.constants import (
    VALUE_KEY,
)

from .trigger_base import TriggerBase


class CompareVariable(TriggerBase):
    def __init__(self,
                 trigger_id: str,
                 small_variable_id: str,
                 big_variable_id: str):
        super().__init__(trigger_id)
        self.__small_variable_id = small_variable_id
        self.__big_variable_id = big_variable_id

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass

    def is_trigger(self) -> bool:
        small_variable_value = System.system.variables[self.__small_variable_id].data[VALUE_KEY]
        big_variable_value = System.system.variables[self.__big_variable_id].data[VALUE_KEY]

        return small_variable_value < big_variable_value
