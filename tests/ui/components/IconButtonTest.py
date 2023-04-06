import unittest
from unittest.mock import Mock
import sys
from PyQt5.QtWidgets import QApplication

from src.gui import ApplicationGUI
from src.gui.customs import (
    IconButton,
)
from src.interfaces import (
    ISystem,
)
from src.constants import (
    ICON_BUTTON_DEFAULT_OPERATION,
)


TEST_APPLICATION_NAME = 'Test Application'
TEST_OPERATION_ID = 'TestOperationId'


class IconButtonTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    def setUp(self):
        self.system = Mock(spec=ISystem)
        self.win = ApplicationGUI(self.system)
        self.win.load_layout('src/assets/layouts/test_layout.ui')
        self.icon_button = IconButton(
            TEST_APPLICATION_NAME, system=self.system)
        self.win.add_component(self.icon_button, 'test_layout')

    @classmethod
    def tearDownClass(cls):
        cls.app.exit()

    def setUp(self) -> None:
        self.system = Mock(spec=ISystem)

    def test_icon_button_initialization(self):
        pass

    @unittest.skip('Not implemented yet')
    def test_icon_button_click(self):
        self.icon_button.clicked.emit(True)
        self.system.run_operation.assert_called_once_with(
            ICON_BUTTON_DEFAULT_OPERATION, [], {})

    @unittest.skip('Not implemented yet')
    def test_icon_button_change_operation(self):
        self.icon_button.assign_operation(TEST_OPERATION_ID)
        self.icon_button.clicked.emit(True)
        self.system.run_operation.assert_called_once_with(
            TEST_OPERATION, [], {})
