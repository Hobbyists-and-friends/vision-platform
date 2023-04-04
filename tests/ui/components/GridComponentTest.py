import unittest
import sys
from PyQt5.QtWidgets import QApplication

from src.gui.customs import GridComponent


TEST_NUMBER_OF_COLUMNS = 5
TEST_NUMBER_OF_ROWS = 5


class GridComponentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication(sys.argv)

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()

    def setUp(self):
        # self.grid_widget = GridComponent(
        #     columns=TEST_NUMBER_OF_COLUMNS,
        #     rows=TEST_NUMBER_OF_ROWS,
        # )
        pass

    def test_grid_component_initialization(self):
        pass
