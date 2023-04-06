import unittest
from unittest.mock import (
    Mock,
    PropertyMock,
)

from src.interfaces import (
    ISystem,
    IVariable,
)
from src.constants import (
    VALUE_KEY,
)
from src.cores import (
    System,
)
from src.operations import (
    CreateVariableOperation,
)

from tests.constants import (
    TEST_OPERATION_NAME,
    TEST_VARIABLE_NAME,
    TEST_VARIABLE_VALUE,
)

from tests.tools import (
    create_mocked_system,
    create_mocked_int_variable,
    add_vars_system,
    add_no_vars_system,
)


class CreateVariableTest(unittest.TestCase):
    def setUp(self):
        self.variable = Mock(spec=IVariable)
        create_mocked_int_variable(self.variable)

        self.no_var_system = Mock(spec=ISystem)
        add_no_vars_system(self.no_var_system)

        self.one_var_system = Mock(spec=ISystem)
        add_vars_system(self.one_var_system, self.variable)

    def test_create_variable(self):
        operation = CreateVariableOperation(
            self.no_var_system, TEST_OPERATION_NAME, TEST_VARIABLE_NAME, TEST_VARIABLE_VALUE)

        operation.run()

        self.no_var_system.add_variable.assert_called_once()

    def test_create_variable_with_existed_name(self):
        operation = CreateVariableOperation(
            self.one_var_system, TEST_OPERATION_NAME, TEST_VARIABLE_NAME, TEST_VARIABLE_VALUE)

        operation.run()

        self.one_var_system.add_variable.assert_not_called()
