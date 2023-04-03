import unittest
from unittest.mock import (
    Mock,
    PropertyMock,
    patch,
)

from src.interfaces import (
    ISystem,
    IApplicationGUI,
)
from src.operations import (
    LoadLayoutOperation,
)


TEST_LAYOUT_NAME = 'test_layout_name'
TEST_LAYOUT_PATH = 'test_layout_path'


class LoadLayoutTest(unittest.TestCase):
    def setUp(self):
        self.system = Mock(spec=ISystem)
        self.application = Mock(spec=IApplicationGUI)
        applications = PropertyMock(return_value=self.application)
        type(self.system).application = applications

    def test_load_layout(self):
        with patch('os.path.exists', return_value=True) as mock_exists:
            operation = LoadLayoutOperation(
                self.system, TEST_LAYOUT_NAME, TEST_LAYOUT_PATH)

            operation.run()

            self.application.load_layout.assert_called_once_with(
                TEST_LAYOUT_PATH)

    def test_load_layout_with_non_existed_operation(self):
        with patch('os.path.exists', return_value=False) as mock_exists:
            mock_exists.return_value = False
            operation = LoadLayoutOperation(
                self.system, TEST_LAYOUT_NAME, TEST_LAYOUT_PATH)

            operation.run()

            self.application.load_layout.assert_not_called()
