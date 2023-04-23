import unittest
from unittest.mock import (
    Mock,
    PropertyMock,
    patch,
)

from src.interfaces.ui import (
    IWindow,
)
from src.interfaces import IObserver
from src.cores import (
    System,
)
from src.operations.system_call import *
from tests.constants import *
from tests.tools import (
    create_test_ui_path,
    delete_test_ui_path,
)


class LoadLayoutTest(unittest.TestCase):
    def setUp(self):
        self.system = System()
        self.error_observer = Mock(spec=IObserver)
        self.system.error.add_observer(self.error_observer)

        self.application = Mock(spec=IWindow)
        self.system.add_application(self.application)

    def test_load_layout(self):
        create_test_ui_path()
        operation = LoadLayoutOperation(
            layout_name=TEST_LAYOUT_PATH
        )

        operation.run()

        self.application.load_layout.assert_called_once_with(
            TEST_LAYOUT_PATH)

    def test_load_layout_with_non_existed_operation(self):
        delete_test_ui_path()
        operation = LoadLayoutOperation(
            layout_name=TEST_LAYOUT_PATH
        )

        operation.run()

        self.application.load_layout.assert_not_called()
        self.error_observer.update.assert_called()
        self.assertEqual(self.error_observer.update.call_count, 2)
