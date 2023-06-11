import unittest
from unittest.mock import (
    Mock,
    MagicMock,
)
from src.interfaces import (
    ISystem,
)
from src.cores import (
    System,
)
from src.utils.Logging import Logging
from src.operations.system_call import *
from src.operations.observer_op import (
    LogVariable,
)
from src.constants import *

from tests.constants import *


class LogVariableTest(unittest.TestCase):
    def setUp(self):
        self.system = System()
        self.info_logging = MagicMock()

        Logging.info = self.info_logging

        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

        CreateOperationOperation(
            operation_id=TEST_LOG_VARIABLE_ID,
            operation_type=OperationType.LOG_VARIABLE.value,
        ).run()

        SetOperationRelatedVariableOperation(
            operation_id=TEST_LOG_VARIABLE_ID,
            src_params_dict={
                SRC_VARIABLE: TEST_VARIABLE_NAME,
            },
            res_params_dict={},
        ).run()

        # self.system.variables[TEST_VARIABLE_NAME].add_observer(
        #     self.system.operations[TEST_OPERATION_NAME],
        # )

    def test_console_log_variable_value(self):
        ChangeVariableValueOperation(
            variable_id=TEST_VARIABLE_NAME,
            new_value=TEST_VARIABLE_SECOND_VALUE,
        ).run()

        self.assertEqual(
            self.info_logging.call_count,
            2,
        )
