import unittest
from unittest.mock import (
    patch,
    MagicMock,
)
from PyQt5.QtGui import (
    QPixmap,
)

from src.cores import (
    System,
)
from src.operations import (
    CreateVariableOperation,
    ConvertImageToGrayOperation,
    AddVariableObserverOperation,
)
from gui.customs import (
    pyqt_image_display,
)
from tests.constants import (
    TEST_IMAGE_DISPLAY_COMPONENT_ID,
    TEST_VARIABLE_NAME,
    TEST_CREATE_VARIABLE_OPERATION_NAME,
    TEST_IMAGE_VARIABLE_NAME,
    TEST_IMAGE_RESULT_NAME,
    TEST_ADD_OBSERVER_OPERATION_NAME,
)
from tests.tools import (
    load_test_image,
)


class ImageDisplayTest(unittest.TestCase):
    def setUp(self):
        self.system = System()
        self.image_display = pyqt_image_display(
            component_id=TEST_IMAGE_DISPLAY_COMPONENT_ID,
        )

        CreateVariableOperation(
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME,
            variable_id=TEST_VARIABLE_NAME,
        ).run()

        CreateVariableOperation(
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME + "1",
            variable_id=TEST_IMAGE_VARIABLE_NAME,
            variable_value=load_test_image(),
        ).run()

        AddVariableObserverOperation(
            operation_id=TEST_ADD_OBSERVER_OPERATION_NAME,
            variable_id=TEST_IMAGE_VARIABLE_NAME,
            observer_id=TEST_IMAGE_DISPLAY_COMPONENT_ID,
        )

        CreateVariableOperation(
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME + "2",
            variable_id=TEST_IMAGE_RESULT_NAME,
        ).run()

        # ConvertImageToGrayOperation(
        #     operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME + "3",
        #     source_variable_id=TEST_IMAGE_VARIABLE_NAME,
        #     result_variable_id=TEST_IMAGE_RESULT_NAME,
        # ).run()

    def test_run_or_update_with_variable(self):
        variable = self.system.variables[TEST_IMAGE_VARIABLE_NAME]
        mock_from_image = MagicMock()
        mock_from_image.return_value = QPixmap()
        with patch('PyQt5.QtGui.QPixmap.fromImage', mock_from_image):
            self.image_display.update(variable, variable.data)

            mock_from_image.assert_called_once()

    def test_run_or_update_with_non_variable(self):
        variable = self.system.variables[TEST_VARIABLE_NAME]
        with patch('PyQt5.QtGui.QPixmap.fromImage') as setPixmap_mock:
            self.image_display.update(variable, variable.data)

            setPixmap_mock.assert_not_called()

    @unittest.skip("Not implemented yet.")
    def test_run_with_3d_image(self):
        variable = self.system.variables[TEST_IMAGE_VARIABLE_NAME]
        self.image_display.update(variable, variable.data)

    @unittest.skip("Not implemented yet.")
    def test_run_gray_image(self):
        variable = self.system.variables[TEST_IMAGE_RESULT_NAME]
        self.image_display.update(variable, variable.data)
