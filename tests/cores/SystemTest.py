import unittest
from unittest.mock import (
    Mock,
    PropertyMock,
)

from src.cores import (
    System,
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
    IVariable,
    IGUIComponent,
)


TEST_VARIABLE_NAME = 'test_variable'
TEST_VARIABLE_VALUE = 3

TEST_OPERATION_NAME = 'test_operation'

TEST_UI_COMPONENT_NAME = 'test_ui_component'


class SystemTest(unittest.TestCase):
    def setUp(self):
        self.system = System()

        self.variable = Mock(spec=IVariable)
        self._define_variable()

        self.operation = Mock(spec=IOperation)
        self._define_operation()

        self.ui_component = Mock(spec=IGUIComponent)
        self._define_gui_component()

    def _define_gui_component(self):
        component_id = PropertyMock(return_value=TEST_UI_COMPONENT_NAME)
        type(self.ui_component).component_id = component_id

    def _define_operation(self):
        operation_id = PropertyMock(return_value=TEST_OPERATION_NAME)

        type(self.operation).operation_id = operation_id

    def _define_variable(self):
        data = PropertyMock(return_value={
            VALUE_KEY: TEST_VARIABLE_VALUE,
            NAME_KEY: TEST_VARIABLE_NAME
        })
        type(self.variable).data = data

        variable_id = PropertyMock(return_value=TEST_VARIABLE_NAME)
        type(self.variable).variable_id = variable_id

    def test_system_has_no_error_at_the_beginning(self):
        self.assertEqual(self.system.error.data[VALUE_KEY], EMPTY_STRING)

    def test_system_has_no_variables_at_the_beginning(self):
        self.assertEqual(len(self.system.variables.keys()), 0)

    def test_system_is_subclass_of_publisher_base(self):
        self.assertTrue(isinstance(self.system, PublisherBase))

    def test_system_add_variables_to_the_system(self):
        self.system.add_variable(self.variable)
        print(self.system.variables)
        self.assertEqual(
            self.system.variables[TEST_VARIABLE_NAME].data[NAME_KEY], TEST_VARIABLE_NAME)
        self.assertEqual(
            self.system.variables[TEST_VARIABLE_NAME].data[VALUE_KEY], TEST_VARIABLE_VALUE)

    def test_system_add_operation_to_the_system(self):
        self.system.add_operation(self.operation)

        self.assertEqual(
            self.system.operations[TEST_OPERATION_NAME], self.operation)

    def test_system_add_ui_component_to_the_system(self):
        self.system.add_ui_component(self.ui_component)

        self.assertEqual(
            self.system.ui_components[TEST_UI_COMPONENT_NAME], self.ui_component)
