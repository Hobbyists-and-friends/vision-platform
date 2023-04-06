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


from tests.constants import (
    TEST_OPERATION_NAME,
)

TEST_NAME = 'test_name'
TEST_LAYOUT = 'test_layout'


class CreateIconButtonTest(unittest.TestCase):
    def setUp(self):
        self.system = Mock(spec=ISystem)

    def test_create_icon_button(self):
        operation = CreateIconButtonOpeartion(self.system,
                                              TEST_OPERATION_NAME,
                                              TEST_NAME)

        operation.run()

        self.system.add_ui_component.assert_called_once()
