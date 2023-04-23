import unittest
from unittest.mock import (
    Mock,
)
from operations.system_call import add_gui_component

from src.interfaces import (
    IOperation,
    ISystem,
    IGUIComponent,
    IApplicationGUI,
)
from src.cores import (
    System,
)
from src.operations import (
    CreateVariableOperation,
)
from tests.constants import (
    TEST_OPERATION_NAME,
    TEST_UI_COMPONENT_NAME,
    TEST_COMPONENT_LAYOUT,
    TEST_CREATE_VARIABLE_OPERATION_NAME,
    TEST_VARIABLE_NAME,
    TEST_VARIABLE_VALUE,
)
from tests.tools import (
    create_mocked_system,
    creat_mocked_operation,
)


class OperationBaseTest(unittest.TestCase):
    def setUp(self):
        self.system = System()
        self.ui_component = Mock(spec=IGUIComponent)
        self.application = Mock(spec=IApplicationGUI)

        create_mocked_system(self.system, self.ui_component, self.application)

    def test_not_store_operation(self):
        self.operation = add_gui_component(
            operation_id=TEST_OPERATION_NAME,
            component_id=TEST_UI_COMPONENT_NAME,
            layout=TEST_COMPONENT_LAYOUT,
            store=False
        )
        self.operation.run()

        self.assertTrue(TEST_OPERATION_NAME not in self.system.operations)

    def test_store_operation(self):
        self.operation = add_gui_component(
            operation_id=TEST_OPERATION_NAME,
            component_id=TEST_UI_COMPONENT_NAME,
            layout=TEST_COMPONENT_LAYOUT,
            store=True
        )

        self.operation.run()

        self.assertTrue(TEST_OPERATION_NAME in self.system.operations)

    def test_run_operation_but_not_be_run(self):
        self.operation = CreateVariableOperation(
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME,
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
            run_at_first=False,
        )

        self.operation.run()

        self.assertDictEqual(self.system.variables, {})
