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
)
from src.gui.customs import (
    ImageDisplay,
)
from tests.constants import (
    TEST_IMAGE_DISPLAY_COMPONENT_ID,
    TEST_VARIABLE_NAME,
    TEST_CREATE_VARIABLE_OPERATION_NAME,
    TEST_IMAGE_VARIABLE_NAME,
    TEST_IMAGE_RESULT_NAME,
)
from tests.tools import (
    load_test_image,
)


class ImageDisplayTest(unittest.TestCase):
    def setUp(self):
        self.system = System()
        self.image_display = ImageDisplay(
            system=self.system,
            component_id=TEST_IMAGE_DISPLAY_COMPONENT_ID,
            variable_id=TEST_VARIABLE_NAME,
        )

        CreateVariableOperation(
            system=self.system,
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME,
            variable_name=TEST_VARIABLE_NAME,
        ).run()

        CreateVariableOperation(
            system=self.system,
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME + "1",
            variable_name=TEST_IMAGE_VARIABLE_NAME,
            variable_value=load_test_image(),
        ).run()

        CreateVariableOperation(
            system=self.system,
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME + "2",
            variable_name=TEST_IMAGE_RESULT_NAME,
        ).run()

        ConvertImageToGrayOperation(
            system=self.system,
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME + "3",
            source_variable_id=TEST_IMAGE_VARIABLE_NAME,
            result_variable_id=TEST_IMAGE_RESULT_NAME,
        ).run()

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

    def test_run_with_3d_image(self):
        variable = self.system.variables[TEST_IMAGE_VARIABLE_NAME]
        self.image_display.update(variable, variable.data)

    def test_run_gray_image(self):
        variable = self.system.variables[TEST_IMAGE_RESULT_NAME]
        self.image_display.update(variable, variable.data)
