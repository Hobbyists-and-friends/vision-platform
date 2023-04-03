import unittest
from unittest.mock import Mock

from src.cores import (
    System,
    Variable,
)
from src.utils import PublisherBase
from src.constants import (
    VALUE_KEY,
    NAME_KEY,
    OPERATION_KEY,
    VARIABLES_KEY,
    APPLICATION_KEY,
    EMPTY_STRING,
)
from src.interfaces import (
    IOperation,
)


TEST_VARIABLE_NAME = 'test_variable'
TEST_VARIABLE_VALUE = 3


class SystemTest(unittest.TestCase):
    def setUp(self):
        self.system = System()
        self.operation = Mock(spec=IOperation)

    def test_system_has_no_error_at_the_beginning(self):
        self.assertEqual(self.system.error.data[VALUE_KEY], EMPTY_STRING)

    def test_system_has_no_variables_at_the_beginning(self):
        self.assertEqual(len(self.system.variables.keys()), 0)

    def test_system_is_subclass_of_publisher_base(self):
        self.assertTrue(isinstance(self.system, PublisherBase))

    def test_system_call_the_run_method_of_an_operation(self):
        # self.system.run_operation
        pass

    def test_system_add_variables_to_the_system(self):
        variable = Variable(self.system, **{
            VALUE_KEY: TEST_VARIABLE_VALUE,
            NAME_KEY: TEST_VARIABLE_NAME,
        })
        self.system.add_variable(variable)
        self.assertEqual(
            self.system.variables[TEST_VARIABLE_NAME].data[NAME_KEY], TEST_VARIABLE_NAME)
        self.assertEqual(
            self.system.variables[TEST_VARIABLE_NAME].data[VALUE_KEY], TEST_VARIABLE_VALUE)

    def test_system_run_operation(self):
        self.system.run_operation(self.operation)

        self.operation.run.assert_called_once_with(self.system, {
            OPERATION_KEY: {},
            VARIABLES_KEY: {},
            APPLICATION_KEY: None,
        })
