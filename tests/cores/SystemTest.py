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

from tests.constants import (
    TEST_OPERATION_NAME,
    TEST_VARIABLE_NAME,
    TEST_UI_COMPONENT_NAME,
    TEST_VARIABLE_VALUE,
)
from tests.tools import (
    create_mocked_int_variable,
    creat_mocked_operation,
    create_mocked_ui_component,
)


class SystemTest(unittest.TestCase):
    def setUp(self):
        self.system = System()

        self.variable = Mock(spec=IVariable)
        create_mocked_int_variable(self.variable)

        self.operation = Mock(spec=IOperation)
        creat_mocked_operation(self.operation)

        self.ui_component = Mock(spec=IGUIComponent)
        create_mocked_ui_component(self.ui_component)

    def test_system_has_no_error_at_the_beginning(self):
        self.assertEqual(self.system.error.data[VALUE_KEY], EMPTY_STRING)

    def test_system_has_no_variables_at_the_beginning(self):
        self.assertEqual(len(self.system.variables.keys()), 0)
