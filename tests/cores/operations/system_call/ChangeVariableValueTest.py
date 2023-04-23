import unittest
from unittest.mock import (
    Mock,
)

from src.cores import (
    System,
)
from src.interfaces import (
    IObserver,
)
from src.constants import (
    VALUE_KEY,
)
from src.operations.system_call import (
    CreateVariableOperation,
    ChangeVariableValueOperation,
)

from tests.constants import *
TEST_NON_EXISTED_VARIABLE_NAME = "test_non_existed_variable_name"


class ChangeVariableValueTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.test_observer = Mock(spec=IObserver)
        self.error_observer = Mock(spec=IObserver)
        self.system.error.add_observer(self.error_observer)

        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

        self.system.variables[TEST_VARIABLE_NAME].add_observer(
            self.test_observer)

    def test_change_variable_value(self):
        operation = ChangeVariableValueOperation(
            variable_id=TEST_VARIABLE_NAME,
            new_value=TEST_VARIABLE_SECOND_VALUE,
        )

        operation.run()

        self.assertEqual(
            self.system.variables[TEST_VARIABLE_NAME].data[VALUE_KEY],
            TEST_VARIABLE_SECOND_VALUE
        )
        self.assertEqual(
            self.test_observer.update.call_count,
            2,
        )

    def test_change_value_of_non_existed_operation(self):
        operation = ChangeVariableValueOperation(
            variable_id=TEST_NON_EXISTED_VARIABLE_NAME,
            new_value=TEST_VARIABLE_SECOND_VALUE,
        )

        operation.run()

        self.assertEqual(self.test_observer.update.call_count, 1)
        self.assertEqual(self.error_observer.update.call_count, 2)
