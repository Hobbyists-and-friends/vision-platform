import unittest
from unittest.mock import (
    Mock,
)

from src.interfaces import (
    IObserver,
)
from src.cores import (
    System,
)
from src.operations.system_call import (
    RaiseErrorOperation,
)
from tests.constants import (
    TEST_ERROR_MESSAGE,
)


class RaiseErrorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.error_observer = Mock(spec=IObserver)
        self.system.error.add_observer(self.error_observer)

    def test_raise_error(self):
        operation = RaiseErrorOperation(
            error_message=TEST_ERROR_MESSAGE,
        )

        operation.run()

        self.assertEqual(self.error_observer.update.call_count, 2)
