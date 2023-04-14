import unittest
from unittest.mock import (
    Mock,
    patch,
)
from src.interfaces import (
    IOperation,
    ISystem,
    IGUIComponent,
    IVariable,
    IApplicationGUI,
)
from src.cores import (
    System,
)
from src.operations import (
    LogVariableOperation,
    CreateVariableOperation,
)

from tests.constants import (
    TEST_OPERATION_NAME,
    TEST_VARIABLE_NAME,
    TEST_VARIABLE_VALUE,
)
from tests.tools import (
    create_mocked_system,
    add_vars_system,
    create_mocked_int_variable,
)


class LogVariableTest(unittest.TestCase):
    def setUp(self):
        self.system = Mock(spec=ISystem)
        self.ui_component = Mock(spec=IGUIComponent)
        self.variable = Mock(spec=IVariable)
        self.application = Mock(spec=IApplicationGUI)

        create_mocked_int_variable(self.variable)
        create_mocked_system(self.system, self.ui_component, self.application)
        add_vars_system(self.system, self.variable)

    def test_console_log_variable_value(self):
        with patch('builtins.print') as mocked_print:
            operation = LogVariableOperation(
                self.system,
                TEST_OPERATION_NAME,
                TEST_VARIABLE_NAME,
            )

            operation.run()

            operation.update(self.system, {})

            mocked_print.assert_called_with(TEST_VARIABLE_VALUE)
