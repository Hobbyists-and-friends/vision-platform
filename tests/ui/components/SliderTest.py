import unittest
import sys
from unittest.mock import (
    patch,
)
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QSlider,
)
from PyQt5.QtCore import (
    Qt,
    QPoint,
)
from PyQt5.QtTest import (
    QTest,
)
from operations.system_call import ChangeVariableValueOperation

from src.cores import (
    System,
)
from src.gui import (
    ApplicationGUI,
)
from src.constants import (
    VALUE_KEY,
)
from src.operations import (
    CreateVariableOperation,
)
from gui.customs import (
    PyQtSlider,
)

from tests.constants import (
    TEST_CREATE_VARIABLE_OPERATION_NAME,
    TEST_VARIABLE_NAME,
    TEST_VARIABLE_VALUE,
    TEST_VARIABLE_SECOND_VALUE,
    TEST_SLIDER_COMPONENT_ID,
)


class TestWindow(QMainWindow):
    def __init__(self, slider):
        super().__init__()
        self.setCentralWidget(slider)


class SliderTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        cls.app.exit()

    def setUp(self):
        self.system = System()
        self.slider = PyQtSlider(
            system=self.system,
            component_id=TEST_SLIDER_COMPONENT_ID,
            update_tool=ChangeVariableValueOperation,
            min=0,
            max=100,
            step=1,
        )
        self.application = TestWindow(self.slider)

        CreateVariableOperation(
            system=self.system,
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME,
            variable_name=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

    @unittest.skip("Not implemented yet")
    def test_slider(self):
        self.slider.set_variable_id(TEST_VARIABLE_NAME)

        QTest.mouseMove(self.slider, pos=self.slider.rect().center())
        QTest.mousePress(self.slider, Qt.MouseButton.LeftButton)
        QTest.mouseMove(self.slider,
                        pos=self.slider.rect().center() + QPoint(TEST_VARIABLE_SECOND_VALUE, 0))
        QTest.mouseRelease(self.slider, Qt.MouseButton.LeftButton)

        self.assertEqual(
            self.system.variables[TEST_VARIABLE_NAME].data[VALUE_KEY],
            TEST_VARIABLE_SECOND_VALUE + TEST_VARIABLE_VALUE + 1,
        )
