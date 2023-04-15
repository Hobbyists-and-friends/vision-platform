import unittest
from unittest.mock import (
    Mock,
)

from src.interfaces import (
    IApplicationGUI,
)
from src.cores import (
    System,
)
from src.operations import (
    CreateImageDisplayOperation,
)

from tests.constants import (
    TEST_CREATE_IMAGE_DISPLAY_OPERATION_ID,
    TEST_IMAGE_DISPLAY_COMPONENT_ID,
    TEST_VARIABLE_NAME,
)


class CreateImageDisplayTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()

    def test_create_image_display(self):
        operation = CreateImageDisplayOperation(
            system=self.system,
            operation_id=TEST_CREATE_IMAGE_DISPLAY_OPERATION_ID,
            component_id=TEST_IMAGE_DISPLAY_COMPONENT_ID,
            variable_id=TEST_VARIABLE_NAME,
        )

        operation.run()

        self.assertIsNotNone(
            self.system.ui_components[TEST_IMAGE_DISPLAY_COMPONENT_ID])
