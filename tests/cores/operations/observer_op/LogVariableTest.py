import unittest
from unittest.mock import (
    Mock,
    patch,
)
from src.interfaces import (
    ISystem,
)
from src.cores import (
    System,
)
from src.operations.system_call import (
    CreateVariableOperation,
    ChangeVariableValueOperation,
)
from src.operations.observer_op import (
    LogVariable,
)

from tests.constants import (
    TEST_OPERATION_NAME,
    TEST_VARIABLE_NAME,
    TEST_VARIABLE_VALUE,
    TEST_VARIABLE_SECOND_VALUE,
)


class LogVariableTest(unittest.TestCase):
    def setUp(self):
        self.system = System()

        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

        self.system.operations[TEST_OPERATION_NAME] = LogVariable()

        self.system.variables[TEST_VARIABLE_NAME].add_observer(
            self.system.operations[TEST_OPERATION_NAME],
        )

    def test_console_log_variable_value(self):
        with patch('builtins.print') as mocked_print:
            ChangeVariableValueOperation(
                variable_id=TEST_VARIABLE_NAME,
                new_value=TEST_VARIABLE_SECOND_VALUE,
            ).run()

            mocked_print.assert_called_with(TEST_VARIABLE_SECOND_VALUE)
