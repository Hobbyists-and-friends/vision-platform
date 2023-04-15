import unittest

from src.cores import (
    System,
)
from src.operations import (
    CreateSliderOperation,
)

from tests.constants import (
    TEST_CREATE_SLIDER_OPERATION_ID,
    TEST_SLIDER_COMPONENT_ID,
)


class CreateSliderTest(unittest.TestCase):
    def setUp(self):
        self.system = System()

    def test_create_slider(self):
        operation = CreateSliderOperation(
            system=self.system,
            operation_id=TEST_CREATE_SLIDER_OPERATION_ID,
            component_id=TEST_SLIDER_COMPONENT_ID,
        )

        operation.run()

        self.assertTrue(TEST_SLIDER_COMPONENT_ID in self.system.ui_components)