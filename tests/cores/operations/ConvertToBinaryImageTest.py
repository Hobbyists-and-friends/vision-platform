import unittest
from unittest.mock import (
    patch,
)
import cv2

from src.cores import (
    System,
)
from src.operations import (
    CreateVariableOperation,
    ConvertImageToGrayOperation,
    ConvertImageToBinaryOperation,
    ChangeVariableValueOperation,
)
from tests.constants import (
    TEST_CREATE_VARIABLE_OPERATION_NAME,
    TEST_IMAGE_VARIABLE_NAME,
    TEST_GRAY_IMAGE_VARIABLE_NAME,
    TEST_CONVERT_IMAGE_TO_GRAY_OPERATION_ID,
    TEST_BINARY_IMAGE_VARIABLE_NAME,
    TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
    TEST_VARIABLE_NAME,
    TEST_VARIABLE_VALUE,
    TEST_VARIABLE_SECOND_VALUE,
)
from tests.tools import (
    load_test_image,
)


class ConvertToBinaryImageTest(unittest.TestCase):
    def setUp(self):
        self.system = System()

        CreateVariableOperation(
            self.system,
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME,
            variable_name=TEST_IMAGE_VARIABLE_NAME,
            variable_value=load_test_image(),
        ).run()

        CreateVariableOperation(
            self.system,
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME + '1',
            variable_name=TEST_GRAY_IMAGE_VARIABLE_NAME,
        ).run()

        CreateVariableOperation(
            self.system,
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME + '2',
            variable_name=TEST_BINARY_IMAGE_VARIABLE_NAME,
        ).run()

        CreateVariableOperation(
            self.system,
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME + '3',
            variable_name=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

        ConvertImageToGrayOperation(
            self.system,
            operation_id=TEST_CONVERT_IMAGE_TO_GRAY_OPERATION_ID,
            source_variable_id=TEST_IMAGE_VARIABLE_NAME,
            result_variable_id=TEST_GRAY_IMAGE_VARIABLE_NAME,
        ).run()

    def test_convert_to_binary_image(self):
        operation = ConvertImageToBinaryOperation(
            self.system,
            operation_id=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
            source_variable_id=TEST_GRAY_IMAGE_VARIABLE_NAME,
            result_variable_id=TEST_BINARY_IMAGE_VARIABLE_NAME,
            threshold_variable_id=TEST_VARIABLE_NAME,
        )

        with patch('cv2.threshold') as binary_conversion_mock:
            operation.run()
            operation.update(
                self.system.variables[TEST_VARIABLE_NAME],
                self.system.variables[TEST_VARIABLE_NAME].data)

            binary_conversion_mock.assert_called()
            self.assertEqual(
                binary_conversion_mock.call_count,
                2
            )
