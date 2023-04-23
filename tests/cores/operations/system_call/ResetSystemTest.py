import unittest


from src.cores import (
    System,
)
from src.constants import (
    ComponentType,
)
from src.operations.system_call import *
from tests.constants import *


class ResetSystemTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()

        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

        CreateGUIComponentOperation(
            component_id=TEST_UI_COMPONENT_NAME,
            component_type=ComponentType.BUTTON.value
        ).run()

    def test_reset_all_system(self):
        operation = ResetSystemOperation()

        operation.run()

        self.assertDictEqual(self.system.variables, {})
        self.assertDictEqual(self.system.ui_components, {})
        self.assertDictEqual(self.system.operations, {})
