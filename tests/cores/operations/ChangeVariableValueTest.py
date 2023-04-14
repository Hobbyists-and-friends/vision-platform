import unittest
from unittest.mock import (
    Mock,
)

from src.cores import (
    System,
)
from src.interfaces import (
    IObserver,
)
from src.constants import (
    VALUE_KEY,
)
from src.operations import (
    CreateVariableOperation,
    ChangeVariableValueOperation,
    AddVariableObserverOperation,
)

from tests.constants import (
    TEST_OPERATION_NAME,
    TEST_ADD_OBSERVER_OPERATION_NAME,
    TEST_VARIABLE_NAME,
    TEST_VARIABLE_VALUE,
    TEST_VARIABLE_SECOND_VALUE,
    TEST_UI_COMPONENT_NAME,
)


TEST_NON_EXISTED_VARIABLE_NAME = "test_non_existed_variable_name"


class ChangeVariableValueTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.test_observer = Mock(spec=IObserver)
        self.system.ui_components[TEST_UI_COMPONENT_NAME] = self.test_observer

        CreateVariableOperation(
            system=self.system,
            operation_id=TEST_OPERATION_NAME,
            variable_name=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

        AddVariableObserverOperation(
            system=self.system,
            operation_id=TEST_ADD_OBSERVER_OPERATION_NAME,
            variable_id=TEST_VARIABLE_NAME,
            observer_id=TEST_UI_COMPONENT_NAME,
        ).run()

    def test_change_variable_value(self):
        operation = ChangeVariableValueOperation(
            system=self.system,
            operation_id=TEST_OPERATION_NAME,
            variable_id=TEST_VARIABLE_NAME,
            new_value=TEST_VARIABLE_SECOND_VALUE,
        )

        operation.run()

        self.assertEqual(
            self.system.variables[TEST_VARIABLE_NAME].data[VALUE_KEY],
            TEST_VARIABLE_SECOND_VALUE
        )
        self.assertEqual(
            self.test_observer.update.call_count,
            2
        )

    def test_change_value_of_non_existed_operation(self):
        operation = ChangeVariableValueOperation(
            system=self.system,
            operation_id=TEST_OPERATION_NAME,
            variable_id=TEST_NON_EXISTED_VARIABLE_NAME,
            new_value=TEST_VARIABLE_SECOND_VALUE,
        )

        operation.run()

        self.test_observer.assert_not_called()
