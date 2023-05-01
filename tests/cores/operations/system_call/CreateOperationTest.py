import unittest
from unittest.mock import (
    Mock,
    patch,
)

from src.interfaces import (
    IObserver,
)
from src.constants import (
    OperationType,
)
from src.operations.system_call import *
from src.cores import (
    System,
)
from tests.constants import *


class CreateOperationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.error_observer = Mock(spec=IObserver)
        self.system.error.add_observer(self.error_observer)

        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

    def test_create_valid_operation(self):
        CreateOperationOperation(
            operation_id=TEST_OPERATION_NAME,
            operation_type=OperationType.PRINT_VARIABLE.value,
            variable_id=TEST_VARIABLE_NAME,
        ).run()

        self.assertTrue(
            TEST_OPERATION_NAME in self.system.operations
        )

    def test_create_existed_operation(self):
        CreateOperationOperation(
            operation_id=TEST_OPERATION_NAME,
            operation_type=OperationType.PRINT_VARIABLE.value,
            variable_id=TEST_VARIABLE_NAME,
        ).run()

        CreateOperationOperation(
            operation_id=TEST_OPERATION_NAME,
            operation_type=OperationType.PRINT_VARIABLE.value,
            variable_id=TEST_VARIABLE_NAME,
        ).run()

        self.assertEqual(self.error_observer.update.call_count,
                         CALL_OBSERVER_COUNT)

    def test_create_valid_operation_with_observer_operation(self):
        CreateOperationOperation(
            operation_id=TEST_OPERATION_NAME,
            operation_type=OperationType.LOG_VARIABLE.value,
        ).run()

        AddVariableObserverOperation(
            variable_id=TEST_VARIABLE_NAME,
            observer_id=TEST_OPERATION_NAME,
        ).run()

        with patch('builtins.print') as mock_print:
            ChangeVariableValueOperation(
                variable_id=TEST_VARIABLE_NAME,
                new_value=TEST_VARIABLE_SECOND_VALUE
            ).run()

            mock_print.assert_called_once_with(TEST_VARIABLE_SECOND_VALUE)
