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


TEST_OPERATION_NAME = 'test_operation_name'
TEST_VARIABLE_NAME = 'test_variable'
TEST_VARIABLE_VALUE = 3


class CreateVariableTest(unittest.TestCase):
    def setUp(self):
        self.no_var_system = Mock(spec=ISystem)
        no_vars = PropertyMock(return_value={})
        type(self.no_var_system).variables = no_vars

        self.one_var_system = Mock(spec=ISystem)
        self.variable = Mock(spec=IVariable)
        variable_name = PropertyMock(return_value=TEST_VARIABLE_NAME)
        type(self.variable).name = variable_name

        mock_variables = PropertyMock(
            return_value={TEST_VARIABLE_NAME: self.variable})
        type(self.one_var_system).variables = mock_variables

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
