import unittest


from src.cores import (
    System,
)
from src.operations import (
    CreateVariableOperation,
    ResetSystemOperation,
    CreateIconButtonOpeartion,
)
from tests.constants import (
    TEST_CREATE_VARIABLE_OPERATION_NAME,
    TEST_CREATE_UI_COMPONENT_OPERATION_ID,
    TEST_VARIABLE_NAME,
    TEST_VARIABLE_VALUE,
)


class ResetSystemTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        print(self.system.ui_components)

        CreateVariableOperation(
            system=self.system,
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME,
            variable_name=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()
        CreateIconButtonOpeartion(
            system=self.system,
            operation_id=TEST_CREATE_UI_COMPONENT_OPERATION_ID,
            component_id=None,
            text=None,
            store=True,
        )

    def test_reset_all_system(self):
        operation = ResetSystemOperation(
            system=self.system,
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME,
        )

        operation.run()

        self.assertDictEqual(self.system.variables, {})
        # self.assertDictEqual(self.system.ui_components, {})
        self.assertDictEqual(self.system.operations, {})