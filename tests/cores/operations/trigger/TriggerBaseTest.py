import unittest
from unittest.mock import (
    Mock,
)

from src.operations.trigger import (
    TriggerBase,
)

from tests.constants import (
    TEST_TRIGGER_ID,
)


class TriggerBaseTrue(TriggerBase):
    def __init__(self, trigger_id: str, value: bool):
        super().__init__(trigger_id)
        self._value = value

    def is_trigger(self) -> bool:
        return self._value

    def export(self) -> dict:
        pass

    def load(self, data: dict) -> None:
        pass


class TriggerBaseTest(unittest.TestCase):
    def test_trigger_base_return_right_value(self):
        trigger = TriggerBaseTrue(TEST_TRIGGER_ID, True)

        self.assertTrue(trigger.is_trigger())
