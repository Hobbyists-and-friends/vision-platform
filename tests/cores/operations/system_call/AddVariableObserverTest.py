import unittest
from unittest.mock import (
    Mock,
)

from src.interfaces.operation import (
    IObserverOp,
)
from src.interfaces import (
    IObserver,
)
from src.cores import (
    System,
)
from src.operations.system_call import *
from tests.constants import *


class AddVariableObserverTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.error_observer = Mock()
        self.system.error.add_observer(self.error_observer)

        self.observer = Mock(spec=IObserverOp)
        self.ui_component = Mock(spec=IObserver)

        self.system.operations[TEST_OPERATION_NAME] = self.observer
        self.system.ui_components[TEST_UI_COMPONENT_NAME] = self.ui_component

        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

    def test_add_observer(self):
        AddVariableObserverOperation(
            variable_id=TEST_VARIABLE_NAME,
            observer_id=TEST_OPERATION_NAME,
        ).run()

        ChangeVariableValueOperation(
            variable_id=TEST_VARIABLE_NAME,
            new_value=TEST_VARIABLE_SECOND_VALUE,
        ).run()

        self.assertEqual(self.observer.update.call_count, 2)

    def test_add_ui_observer(self):
        AddVariableObserverOperation(
            variable_id=TEST_VARIABLE_NAME,
            observer_id=TEST_UI_COMPONENT_NAME,
        ).run()

        ChangeVariableValueOperation(
            variable_id=TEST_VARIABLE_NAME,
            new_value=TEST_VARIABLE_SECOND_VALUE,
        ).run()

        self.assertEqual(self.ui_component.update.call_count, 2)
