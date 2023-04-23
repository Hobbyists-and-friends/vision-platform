import unittest
from unittest.mock import (
    Mock,
    patch,
)

from src.cores import *
from src.interfaces import IObserver
from src.operations.system_call import *
from tests.constants import *


class PrintValueTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.error_observer = Mock(spec=IObserver)
        self.system.error.add_observer(self.error_observer)

        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

    def test_print_value(self):
        operation = PrintValueOperation(
            variable_id=TEST_VARIABLE_NAME,
        )

        with patch('builtins.print') as mock_print:
            operation.run()

        mock_print.assert_called_once_with(TEST_VARIABLE_VALUE)

    def test_print_non_existed_value(self):
        operation = PrintValueOperation(
            variable_id=TEST_NON_EXISTED_VARIABLE_NAME,
        )

        with patch('builtins.print') as mock_print:
            operation.run()

        mock_print.assert_not_called()
        self.assertEqual(self.error_observer.update.call_count, 2)
