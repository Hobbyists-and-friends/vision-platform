import unittest
from unittest.mock import (
    patch,
)

from src.cores import (
    System,
)
from src.operations import (
    CreateVariableOperation,
    ConvertImageToGrayOperation,
)

from tests.constants import (
    TEST_CREATE_VARIABLE_OPERATION_NAME,
    TEST_IMAGE_SOURCE_NAME,
    TEST_IMAGE_RESULT_NAME,
    TEST_CONVERT_IMAGE_TO_GRAY_OPERATION_ID,
    TEST_EMPTY_VARIABLE_NAME,
)
from tests.tools import (
    load_test_image,
)


class ConvertImageToGrayTest(unittest.TestCase):
    def setUp(self):
        self.system = System()

        CreateVariableOperation(
            self.system,
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME,
            variable_name=TEST_IMAGE_SOURCE_NAME,
            variable_value=load_test_image(),
        ).run()

        CreateVariableOperation(
            self.system,
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME + "1",
            variable_name=TEST_EMPTY_VARIABLE_NAME,
        ).run()

        CreateVariableOperation(
            self.system,
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME + "2",
            variable_name=TEST_IMAGE_RESULT_NAME,
        ).run()

    def test_convert_image_to_gray(self):
        operation = ConvertImageToGrayOperation(
            self.system,
            operation_id=TEST_CONVERT_IMAGE_TO_GRAY_OPERATION_ID,
            source_variable_id=TEST_IMAGE_SOURCE_NAME,
            result_variable_id=TEST_IMAGE_RESULT_NAME,
        )

        with patch('cv2.cvtColor') as mock_cvtColor:
            operation.run()
            operation.update(None, None)

            self.assertEqual(
                mock_cvtColor.call_count, 2)

    def test_convert_none_variable(self):
        operation = ConvertImageToGrayOperation(
            self.system,
            operation_id=TEST_CONVERT_IMAGE_TO_GRAY_OPERATION_ID,
            source_variable_id=TEST_EMPTY_VARIABLE_NAME,
            result_variable_id=TEST_IMAGE_RESULT_NAME,
        )

        with patch('cv2.cvtColor') as mock_cvtColor:
            operation.run()
            operation.update(None, None)

            self.assertEqual(
                mock_cvtColor.call_count, 0)
