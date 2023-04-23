import sys
import unittest
from unittest.mock import (
    Mock,
)

from src.cores import (
    System,
    SystemController,
)
from src.constants import (
    VALUE_KEY,
)
from src.operations.system_call import (
    CreateVariableOperation,
)
from src.interfaces.ui import (
    IWindow,
)
from tests.constants import (
    TEST_CREATE_VARIABLE_OPERATION_NAME,
    TEST_VARIABLE_NAME,
    TEST_VARIABLE_VALUE,
)


class SystemControllerTest(unittest.TestCase):
    def test_call_event_as_operation(self):
        system = System()
        window = Mock(spec=IWindow)
        system_controller = SystemController(system, window)

        operation = CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        )

        system_controller.dispatch_operation(operation)

        self.assertEqual(
            system.variables[TEST_VARIABLE_NAME].data[VALUE_KEY], TEST_VARIABLE_VALUE)
