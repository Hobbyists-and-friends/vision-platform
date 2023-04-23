import unittest
from unittest.mock import (
    Mock,
)

from src.cores import (
    System,
)
from src.operations.system_call import (
    CreateVariableOperation,
)
from src.operations.trigger import (
    CompareVariable,
)
from tests.constants import (
    TEST_VARIABLE_NAME,
    TEST_THRESHOLD_VARIABLE_NAME,
    TEST_VARIABLE_VALUE,
    TEST_TRIGGER_ID,
)


class CompareVariableTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()

        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

        CreateVariableOperation(
            variable_id=TEST_THRESHOLD_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE + 1,
        ).run()

    def test_compare_variable(self):
        trigger = CompareVariable(
            trigger_id=TEST_TRIGGER_ID,
            small_variable_id=TEST_VARIABLE_NAME,
            big_variable_id=TEST_THRESHOLD_VARIABLE_NAME,
        )

        self.assertTrue(trigger.is_trigger())

    def test_compare_variable_false(self):
        trigger = CompareVariable(
            trigger_id=TEST_TRIGGER_ID,
            small_variable_id=TEST_THRESHOLD_VARIABLE_NAME,
            big_variable_id=TEST_VARIABLE_NAME,
        )

        self.assertFalse(trigger.is_trigger())
