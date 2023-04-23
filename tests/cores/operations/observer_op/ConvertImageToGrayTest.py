import unittest
from unittest.mock import Mock


from src.cores import *
from src.constants import *
from src.interfaces import IObserver
from src.operations.system_call import *
from tests.constants import *
from tests.tools import *


class ConvertImageToGrayTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.error_observer = Mock(spec=IObserver)
        self.system.error.add_observer(self.error_observer)

        CreateVariableOperation(
            variable_id=TEST_IMAGE_VARIABLE_NAME,
            variable_value=load_test_image()
        ).run()

        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

        CreateVariableOperation(
            variable_id=TEST_IMAGE_RESULT_NAME,
        ).run()

        CreateOperationOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_GRAY_OPERATION_ID,
            operation_type=OperationType.CONVERT_IMAGE_TO_GRAY.value,
        ).run()

    def test_convert_image_to_gray(self):
        SetOperationRelatedVariableOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_GRAY_OPERATION_ID,
            src_params_dict={
                SRC_VARIABLE: TEST_IMAGE_VARIABLE_NAME,
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_IMAGE_RESULT_NAME
            },
        ).run()

        self.assertEqual(
            self.system.variables[TEST_IMAGE_RESULT_NAME].type,
            VariableType.IMAGE
        )

    def test_convert_image_to_gray_with_not_image_variable(self):
        SetOperationRelatedVariableOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_GRAY_OPERATION_ID,
            src_params_dict={
                SRC_VARIABLE: TEST_VARIABLE_NAME,
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_IMAGE_RESULT_NAME
            },
        ).run()

        self.assertEqual(self.error_observer.update.call_count, 2)
