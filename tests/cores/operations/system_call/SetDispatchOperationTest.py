import unittest
from unittest.mock import (
    Mock,
)

from src.interfaces.ui import (
    IWindow,
)
from src.interfaces.operation import (
    IObserverOp,
    ISystemCall,
)
from src.interfaces import (
    IObserver,
)
from src.constants import *
from src.cores import *
from src.operations.system_call import *

from tests.constants import *


class SetDispatchOperationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.operation_observer = Mock(spec=IObserverOp)
        self.system_call = Mock(spec=ISystemCall)
        self.error_observer = Mock(spec=IObserver)
        self.system.error.add_observer(self.error_observer)

        self.app = Mock(spec=IWindow)
        self.system.add_application(self.app)

        self.system.operations[TEST_OPERATION_NAME] = self.operation_observer
        self.system.operations[TEST_SYSTEM_CALL_OPERATION_NAME] = self.system_call

        CreateGUIComponentOperation(
            component_id=TEST_UI_COMPONENT_NAME,
            component_type=ComponentType.BUTTON.value,
        ).run()

    def test_set_valid_operation_with_valid_component(self):
        operation = SetDispatchOperation(
            operation_id=TEST_SYSTEM_CALL_OPERATION_NAME,
            component_id=TEST_UI_COMPONENT_NAME,
        )

        operation.run()

        self.system.ui_components[TEST_UI_COMPONENT_NAME].button.click()
        self.assertEqual(self.system_call.run.call_count,
                         CALL_OBSERVER_COUNT)

    def test_set_invalid_operation_with_valid_component(self):
        operation = SetDispatchOperation(
            operation_id=TEST_OPERATION_NAME,
            component_id=TEST_UI_COMPONENT_NAME,
        )

        operation.run()
        self.assertEqual(self.error_observer.update.call_count,
                         CALL_OBSERVER_COUNT)

    @unittest.skip('Not implemented yet.')
    def test_set_valid_operation_with_invalid_component(self):
        operation = SetDispatchOperation(
            operation_id=TEST_SYSTEM_CALL_OPERATION_NAME,
            component_id=TEST_NON_EXISTED_UI_COMPONENT_NAME,
        )

        operation.run()

        self.assertEqual(self.error_observer.update.call_count,
                         CALL_OBSERVER_COUNT)

    def test_set_non_existed_operation(self):
        operation = SetDispatchOperation(
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME,
            component_id=TEST_UI_COMPONENT_NAME,
        )

        operation.run()

        self.assertEqual(self.error_observer.update.call_count,
                         CALL_OBSERVER_COUNT)

    def test_set_operation_with_non_existed_component(self):
        operation = SetDispatchOperation(
            operation_id=TEST_SYSTEM_CALL_OPERATION_NAME,
            component_id=TEST_NON_EXISTED_UI_COMPONENT_NAME,
        )

        operation.run()

        self.assertEqual(self.error_observer.update.call_count,
                         CALL_OBSERVER_COUNT)
