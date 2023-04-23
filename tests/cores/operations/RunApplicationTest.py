import unittest

from src.cores import (
    System,
)
from src.operations import (
    RunApplicationOperation,
    CreateVariableOperation,
    CreateApplicationOperation,
)
from tests.constants import (
    TEST_FIRST_APPLICATION_NAME,
    TEST_RUN_APPLICATION_OPERATION_ID,
    TEST_CREATE_APPLICATION_OPERATION_ID,
    TEST_CREATE_VARIABLE_OPERATION_NAME,
    TEST_VARIABLE_NAME,
    TEST_VARIABLE_VALUE,
)


class RunApplicationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()

        CreateVariableOperation(
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME,
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

    def test_run_application_then_all_variables_are_deleted(self):
        CreateApplicationOperation(
            operation_id=TEST_CREATE_APPLICATION_OPERATION_ID,
            application_name=TEST_FIRST_APPLICATION_NAME,
        ).run()

        operation = RunApplicationOperation(
            operation_id=TEST_RUN_APPLICATION_OPERATION_ID,
            application_name=TEST_FIRST_APPLICATION_NAME,
        )

        operation.run()

        self.assertDictEqual(self.system.variables, {})
