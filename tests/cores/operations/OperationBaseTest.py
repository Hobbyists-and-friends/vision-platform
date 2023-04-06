import unittest
from unittest.mock import (
    Mock,
)

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
    AddGUIComponentOperation,
)
from tests.constants import (
    TEST_OPERATION_NAME,
    TEST_UI_COMPONENT_NAME,
    TEST_COMPONENT_LAYOUT,
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
        self.operation = AddGUIComponentOperation(
            self.system,
            TEST_OPERATION_NAME,
            TEST_UI_COMPONENT_NAME,
            TEST_COMPONENT_LAYOUT,
            store=False
        )
        self.operation.run()

        self.assertTrue(TEST_OPERATION_NAME not in self.system.operations)

    def test_store_operation(self):
        self.operation = AddGUIComponentOperation(
            self.system,
            TEST_OPERATION_NAME,
            TEST_UI_COMPONENT_NAME,
            TEST_COMPONENT_LAYOUT,
            store=True
        )

        self.operation.run()

        self.assertTrue(TEST_OPERATION_NAME in self.system.operations)
