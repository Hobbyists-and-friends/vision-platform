import unittest
from unittest.mock import (
    Mock,
)


from src.interfaces import IObserver
from src.constants import *
from src.cores import System
from src.operations.system_call import *

from tests.constants import *
from tests.tools import *


class ConvertImageToBinaryTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.error = Mock(spec=IObserver)
        self.system.error.add_observer(self.error)

        CreateVariableOperation(
            variable_id=TEST_IMAGE_VARIABLE_NAME,
            variable_value=load_test_image()
        ).run()
        CreateVariableOperation(
            variable_id=TEST_GRAY_IMAGE_VARIABLE_NAME,
        ).run()
        CreateVariableOperation(
            variable_id=TEST_IMAGE_RESULT_NAME,
        ).run()
        CreateOperationOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_GRAY_OPERATION_ID,
            operation_type=OperationType.CONVERT_IMAGE_TO_GRAY.value,
        ).run()
        SetOperationRelatedVariableOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_GRAY_OPERATION_ID,
            src_params_dict={
                SRC_VARIABLE: TEST_IMAGE_VARIABLE_NAME,
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_GRAY_IMAGE_VARIABLE_NAME,
            },
        ).run()
        CreateVariableOperation(
            variable_id=TEST_THRESHOLD_VARIABLE_NAME,
            variable_value=TEST_THRESHOLD_VARIABLE_VALUE,
        ).run()

    def test_convert_image_to_gray(self):
        CreateOperationOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
            operation_type=OperationType.CONVERT_IMAGE_TO_BINARY.value,
        ).run()

        SetOperationRelatedVariableOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
            src_params_dict={
                SRC_VARIABLE: TEST_GRAY_IMAGE_VARIABLE_NAME,
                THRESHOLD_VARIABLE: TEST_THRESHOLD_VARIABLE_NAME,
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_IMAGE_RESULT_NAME,
            }
        ).run()

        self.assertEqual(
            self.system.variables[TEST_IMAGE_RESULT_NAME].type,
            VariableType.IMAGE
        )
        self.assertEqual(
            len(self.system.variables[TEST_IMAGE_RESULT_NAME].data[VALUE_KEY].shape),
            2
        )
