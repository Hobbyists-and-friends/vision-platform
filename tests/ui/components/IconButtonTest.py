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

TEST_COMPONENT_ID = 'TestComponentId'
TEST_APPLICATION_NAME = 'Test Application'
TEST_OPERATION_ID = 'TestOperationId'
TEST_TEXT = 'Test Text'


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
        button = IconButton(system=self.system,
                            component_id=TEST_COMPONENT_ID,
                            text=TEST_TEXT)
