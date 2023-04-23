import unittest
from unittest.mock import (
    Mock,
)

from src.interfaces import (
    IPublisher,
)
from src.cores import (
    System,
)
from src.constants import (
    VALUE_KEY,
)
from src.operations.system_call import (
    CreateVariableOperation,
    ChangeVariableValueOperation,
)
from src.operations.observer_op import (
    ObserverOpBase,
)
from tests.constants import (
    TEST_VARIABLE_NAME,
    TEST_VARIABLE_VALUE,
    TEST_VARIABLE_SECOND_VALUE,
)


class TestObserverOp(ObserverOpBase):
    def __init__(self, operation_id: str, data: int = 2) -> None:
        super().__init__(operation_id=operation_id, trigger_id=None)
        self.data = data

    def _update_impl(self, publisher: 'IPublisher', data: dict) -> None:
        print("Here")
        self.data = data[VALUE_KEY]


class ObserverOpBaseTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.test_observer_op = TestObserverOp(TEST_VARIABLE_NAME)

        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

        self.system.variables[TEST_VARIABLE_NAME].add_observer(
            self.test_observer_op
        )

    def test_observer_base_test_with_changed_variable(self):
        ChangeVariableValueOperation(
            variable_id=TEST_VARIABLE_NAME,
            new_value=TEST_VARIABLE_SECOND_VALUE,
        ).run()

        self.assertEqual(self.test_observer_op.data,
                         TEST_VARIABLE_SECOND_VALUE)
