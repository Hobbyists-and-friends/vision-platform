import unittest
from unittest.mock import (
    Mock,
)

from src.cores import (
    System,
)
from src.constants import (
    VALUE_KEY,
)
from src.interfaces import (
    IOperation,
)
from src.operations import (
    CreateVariableOperation,
    CreateApplicationOperation,
    ResetSystemOperation,
)

from tests.constants import (
    TEST_FIRST_APPLICATION_NAME,
    TEST_CREATE_VARIABLE_OPERATION_NAME,
    TEST_VARIABLE_NAME,
    TEST_VARIABLE_VALUE,
)


CREATE_APPLICATION_OPERATION_ID = 'create_application_operation_id'


class CreateApplicationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()

        CreateVariableOperation(
            system=self.system,
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME,
            variable_name=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

        self.test_operation = Mock(spec=IOperation)

    def test_create_application_and_run_it_automatically_at_the_first_time(self):
        operation = CreateApplicationOperation(
            system=self.system,
            operation_id=CREATE_APPLICATION_OPERATION_ID,
            application_name=TEST_FIRST_APPLICATION_NAME,
        )

        operation.run()

        self.assertIsNotNone(
            self.system.applications[TEST_FIRST_APPLICATION_NAME])
        self.assertEqual(
            self.system.applications[TEST_FIRST_APPLICATION_NAME].data[VALUE_KEY][0].__class__,
            ResetSystemOperation
        )

    def test_create_application_with_some_operation(self):
        operation = CreateApplicationOperation(
            system=self.system,
            operation_id=CREATE_APPLICATION_OPERATION_ID,
            application_name=TEST_FIRST_APPLICATION_NAME,
            operations=[
                self.test_operation,
            ],
        )

        operation.run()

        self.assertEqual(
            len(self.system.applications[TEST_FIRST_APPLICATION_NAME].data[VALUE_KEY]),
            2
        )
