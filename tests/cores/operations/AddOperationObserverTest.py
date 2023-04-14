import unittest
from unittest.mock import (
    Mock,
    patch,
)

from src.interfaces import (
    ISystem,
    IOperation,
    IApplicationGUI,
)
from src.cores import (
    System,
)
from tests.constants import (
    TEST_OPERATION_NAME,
    TEST_VARIABLE_NAME,
    TEST_CREATE_VARIABLE_OPERATION_NAME,
    TEST_VARIABLE_VALUE,
    TEST_UI_COMPONENT_NAME,
    TEST_ADD_OBSERVER_OPERATION_NAME,
    TEST_CREATE_UI_COMPONENT_OPERATION_ID,
    TEST_UI_COMPONENT_NAME,
)
from src.operations import (
    AddOperationObserverOperation,
    CreateIconButtonOpeartion,
    LogVariableOperation,
    CreateVariableOperation,
)


class AddOpeartionObserverTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.system.operations[TEST_OPERATION_NAME] = Mock(spec=IOperation)

        CreateIconButtonOpeartion(
            system=self.system,
            operation_id=TEST_CREATE_UI_COMPONENT_OPERATION_ID,
            component_id=TEST_UI_COMPONENT_NAME,
            text=TEST_UI_COMPONENT_NAME,
        ).run()

    def test_the_operation_should_update_when_the_ui_component_notify(self):
        operation = AddOperationObserverOperation(
            self.system,
            TEST_ADD_OBSERVER_OPERATION_NAME,
            TEST_OPERATION_NAME,
            TEST_UI_COMPONENT_NAME,
        )

        operation.run()
        self.system.ui_components[TEST_UI_COMPONENT_NAME].notify()

        self.system.operations[TEST_OPERATION_NAME].update.assert_called_once()
