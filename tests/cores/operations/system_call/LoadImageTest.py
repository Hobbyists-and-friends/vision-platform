import unittest
from unittest.mock import (
    Mock,
)

from src.cores import (
    System,
)
from src.constants import (
    VariableType,
)
from src.interfaces import IObserver
from src.operations.system_call import *

from tests.constants import *


class LoadImageTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.error_observer = Mock(spec=IObserver)
        self.system.error.add_observer(self.error_observer)

        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
        ).run()

        CreateVariableOperation(
            variable_id=TEST_IMAGE_PATH_VARIABLE_NAME,
            variable_value=TEST_LOAD_IMAGE_PATH,
        ).run()

        CreateVariableOperation(
            variable_id=TEST_NON_EXISTED_IMAGE_PATH_VARIABLE_NAME,
            variable_value=TEST_NON_EXISTED_IMAGE_PATH,
        ).run()

    def test_load_image(self):
        operation = LoadImageOperation(
            variable_id=TEST_VARIABLE_NAME,
            image_path_variable_id=TEST_IMAGE_PATH_VARIABLE_NAME,
        )

        operation.run()

        self.assertEqual(
            self.system.variables[TEST_VARIABLE_NAME].type, VariableType.IMAGE)

    def test_load_non_existed_image(self):
        operation = LoadImageOperation(
            variable_id=TEST_VARIABLE_NAME,
            image_path_variable_id=TEST_NON_EXISTED_IMAGE_PATH_VARIABLE_NAME
        )

        operation.run()

        self.assertEqual(self.error_observer.update.call_count,
                         CALL_OBSERVER_COUNT)
