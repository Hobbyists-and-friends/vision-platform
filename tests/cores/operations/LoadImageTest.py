import unittest
from unittest.mock import (
    Mock,
)

from src.cores import (
    System,
)
from src.constants import (
    VariableType,
)
from src.operations import (
    LoadImageOperation,
    CreateVariableOperation,
)

from tests.constants import (
    TEST_LOAD_IMAGE_OPERATION_ID,
    TEST_LOAD_IMAGE_PATH,
    TEST_VARIABLE_NAME,
    TEST_CREATE_VARIABLE_OPERATION_NAME,
    TEST_CREATE_IMAGE_PATH_VARIABLE_OPERATION_ID,
    TEST_IMAGE_PATH_VARIABLE_NAME,
)


class LoadImageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()

        CreateVariableOperation(
            system=self.system,
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME,
            variable_name=TEST_VARIABLE_NAME,
        ).run()

        CreateVariableOperation(
            system=self.system,
            operation_id=TEST_CREATE_IMAGE_PATH_VARIABLE_OPERATION_ID,
            variable_name=TEST_IMAGE_PATH_VARIABLE_NAME,
            variable_value=TEST_LOAD_IMAGE_PATH,
        ).run()

    def test_load_image(self):
        operation = LoadImageOperation(
            system=self.system,
            operation_id=TEST_LOAD_IMAGE_OPERATION_ID,
            variable_id=TEST_VARIABLE_NAME,
            image_path_variable_id=TEST_IMAGE_PATH_VARIABLE_NAME,
        )

        operation.run()

        self.assertEqual(
            self.system.variables[TEST_VARIABLE_NAME].type, VariableType.IMAGE)
