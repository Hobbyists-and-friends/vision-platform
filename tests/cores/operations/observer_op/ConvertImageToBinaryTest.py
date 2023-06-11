import cv2 as cv
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
            variable_id=TEST_IMAGE_VARIABLE_NAME, variable_value=load_test_image()
        ).run()
        CreateVariableOperation(
            variable_id=TEST_GRAY_IMAGE_VARIABLE_NAME,
        ).run()
        CreateVariableOperation(
            variable_id=TEST_IMAGE_RESULT_NAME,
        ).run()
        CreateVariableOperation(
            variable_id=TEST_BINARY_IMAGE_TYPE,
            variable_value=cv.THRESH_BINARY,
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

        self.result_image_observer = Mock(spec=IObserver)
        self.system.variables[TEST_IMAGE_RESULT_NAME].add_observer(
            self.result_image_observer
        )

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
            },
        ).run()

        self.assertEqual(
            self.system.variables[TEST_IMAGE_RESULT_NAME].type, VariableType.IMAGE
        )
        self.assertEqual(
            len(self.system.variables[TEST_IMAGE_RESULT_NAME].data[VALUE_KEY].shape), 2
        )

    def test_convert_image_to_binary_with_new_option(self):
        CreateOperationOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
            operation_type=OperationType.CONVERT_IMAGE_TO_BINARY.value,
        ).run()

        SetOperationRelatedVariableOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
            src_params_dict={
                SRC_VARIABLE: TEST_GRAY_IMAGE_VARIABLE_NAME,
                THRESHOLD_VARIABLE: TEST_THRESHOLD_VARIABLE_NAME,
                TYPE_VARIABLE: TEST_BINARY_IMAGE_TYPE,
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_IMAGE_RESULT_NAME,
            },
        ).run()

        ChangeVariableValueOperation(
            variable_id=TEST_BINARY_IMAGE_TYPE,
            new_value=cv.THRESH_BINARY_INV,
        ).run()

        self.assertEqual(
            self.system.variables[TEST_IMAGE_RESULT_NAME].type, VariableType.IMAGE
        )
        self.assertEqual(
            len(self.system.variables[TEST_IMAGE_RESULT_NAME].data[VALUE_KEY].shape), 2
        )

        self.assertEqual(self.result_image_observer.update.call_count, 5)

    def test_the_threshold_variable_should_be_the_default_params_of_the_observer(self):
        CreateOperationOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
            operation_type=OperationType.CONVERT_IMAGE_TO_BINARY.value,
        ).run()

        SetOperationRelatedVariableOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
            src_params_dict={
                SRC_VARIABLE: TEST_GRAY_IMAGE_VARIABLE_NAME,
                THRESHOLD_VARIABLE: TEST_THRESHOLD_VARIABLE_NAME,
                TYPE_VARIABLE: TEST_BINARY_IMAGE_TYPE,
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_IMAGE_RESULT_NAME,
            },
        ).run()

        self.assertEqual(
            self.system.variables[TEST_THRESHOLD_VARIABLE_NAME].data[VALUE_KEY],
            self.system.operations[
                TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID
            ].default_params[THRESHOLD_VARIABLE],
        )

    def test_convert_without_res_params(self):
        CreateOperationOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
            operation_type=OperationType.CONVERT_IMAGE_TO_BINARY.value,
        ).run()

        SetOperationRelatedVariableOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
            src_params_dict={
                SRC_VARIABLE: TEST_GRAY_IMAGE_VARIABLE_NAME,
                THRESHOLD_VARIABLE: TEST_THRESHOLD_VARIABLE_NAME,
                TYPE_VARIABLE: TEST_BINARY_IMAGE_TYPE,
            },
            res_params_dict={},
        ).run()

        self.assertEqual(self.error.update.call_count, NOT_CALL_OBSERVER_COUNT)

    def test_convert_with_non_existed_result_variable(self):
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
                RESULT_VARIABLE: TEST_NON_EXISTED_VARIABLE_NAME,
            },
            auto_mode=True,
        ).run()

        self.assertEqual(
            self.system.variables[TEST_NON_EXISTED_VARIABLE_NAME].type,
            VariableType.IMAGE,
        )
        self.assertEqual(
            len(
                self.system.variables[TEST_NON_EXISTED_VARIABLE_NAME]
                .data[VALUE_KEY]
                .shape
            ),
            2,
        )

    def test_convert_image_to_binary_with_non_existed_src_variable(self):
        CreateOperationOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
            operation_type=OperationType.CONVERT_IMAGE_TO_BINARY.value,
        ).run()

        SetOperationRelatedVariableOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
            src_params_dict={
                SRC_VARIABLE: TEST_NON_EXISTED_VARIABLE_NAME,
                THRESHOLD_VARIABLE: TEST_NON_EXISTED_PARAM,
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_BINARY_IMAGE_VARIABLE_NAME,
            },
            auto_mode=True,
        ).run()

        self.assertTrue(TEST_NON_EXISTED_VARIABLE_NAME in self.system.variables.keys())
        self.assertTrue(TEST_NON_EXISTED_PARAM in self.system.variables.keys())
