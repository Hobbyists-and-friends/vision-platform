from src.interfaces.operation import (
    ITrigger,
)


class TriggerBase(ITrigger):
    def __init__(self, trigger_id: str):
        self.__trigger_id = trigger_id

    @property
    def trigger_id(self) -> str:
        return self.__trigger_id
