import unittest

from src.cores import (
    System,
)
from src.operations import (
    AssignVariableWithUIComponentOperation,
    CreateVariableOperation,
    CreateSliderOperation,
)

from tests.constants import (
    TEST_CREATE_SLIDER_OPERATION_ID,
    TEST_SLIDER_COMPONENT_ID,
    TEST_CREATE_VARIABLE_OPERATION_NAME,
    TEST_VARIABLE_NAME,
    TEST_VARIABLE_VALUE,
    TEST_ASSIGN_VARIABLE_WITH_UI_COMPONENT_OPERATION_ID,
)


class AssignVariableWithUIComponentTest(unittest.TestCase):
    def setUp(self):
        self.system = System()

        CreateSliderOperation(
            system=self.system,
            operation_id=TEST_CREATE_SLIDER_OPERATION_ID,
            component_id=TEST_SLIDER_COMPONENT_ID,
        ).run()

        CreateVariableOperation(
            system=self.system,
            operation_id=TEST_CREATE_VARIABLE_OPERATION_NAME,
            variable_name=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

    def test_assign_variable_with_ui_component(self):
        operation = AssignVariableWithUIComponentOperation(
            system=self.system,
            operation_id=TEST_ASSIGN_VARIABLE_WITH_UI_COMPONENT_OPERATION_ID,
            variable_id=TEST_VARIABLE_NAME,
            component_id=TEST_SLIDER_COMPONENT_ID,
        )

        operation.run()
