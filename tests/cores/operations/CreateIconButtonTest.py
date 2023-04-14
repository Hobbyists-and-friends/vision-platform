import unittest
from unittest.mock import (
    Mock,
    PropertyMock,
)

from src.operations import (
    CreateIconButtonOpeartion,
)
from src.interfaces import (
    ISystem,
)
from src.cores import (
    System,
)


from tests.constants import (
    TEST_OPERATION_NAME,
)

TEST_NAME = 'test_name'
TEST_LAYOUT = 'test_layout'
TEST_BUTTON_TEXT = 'test_button_text'


class CreateIconButtonTest(unittest.TestCase):
    def setUp(self):
        self.system = System()

    def test_create_icon_button(self):
        operation = CreateIconButtonOpeartion(system=self.system,
                                              operation_id=TEST_OPERATION_NAME,
                                              component_id=TEST_NAME,
                                              text=TEST_BUTTON_TEXT)

        operation.run()

        self.assertEqual(
            self.system.ui_components[TEST_NAME].component_id, TEST_NAME)
