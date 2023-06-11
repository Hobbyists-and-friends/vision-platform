import unittest
from unittest.mock import (
    Mock,
    MagicMock,
)

from src.interfaces import (
    IObserver,
)
from src.constants import *
from src.operations.system_call import *
from src.cores import (
    System,
)
from src.utils.Logging import Logging
from tests.constants import *


class CreateOperationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.info_logging = MagicMock()
        self.error_observer = Mock(spec=IObserver)
        self.system.error.add_observer(self.error_observer)

        Logging.info = self.info_logging

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

        self.assertTrue(TEST_OPERATION_NAME in self.system.operations)

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

        self.assertEqual(self.error_observer.update.call_count, CALL_OBSERVER_COUNT)

    def test_create_valid_operation_with_observer_operation(self):
        CreateOperationOperation(
            operation_id=TEST_OPERATION_NAME,
            operation_type=OperationType.LOG_VARIABLE.value,
        ).run()

        SetOperationRelatedVariableOperation(
            operation_id=TEST_OPERATION_NAME,
            src_params_dict={
                SRC_VARIABLE: TEST_VARIABLE_NAME,
            },
            res_params_dict={},
        ).run()

        ChangeVariableValueOperation(
            variable_id=TEST_VARIABLE_NAME, new_value=TEST_VARIABLE_SECOND_VALUE
        ).run()
