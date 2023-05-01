import unittest
from unittest.mock import (
    Mock,
)

from src.interfaces.ui import (
    IVariableRelatedComponent,
)
from src.interfaces import (
    IObserver,
)
from src.cores import (
    System,
)
from src.constants import *
from src.operations.system_call import *
from src.gui.customs import *

from tests.constants import *


class SetComponentRelatedVariableTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.error_observer = Mock(spec=IObserver)
        self.system.error.add_observer(self.error_observer)
        self.related_variable_component = Mock(spec=IVariableRelatedComponent)

        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

        self.system.ui_components[TEST_UI_COMPONENT_NAME] = self.related_variable_component

    @unittest.skip("Not implemented")
    def test_set_component_related_valid_variable(self):
        SetComponentRelatedVariableOperation(
            component_id=TEST_UI_COMPONENT_NAME,
            src_params={
                SRC_VARIABLE: TEST_VARIABLE_NAME,
            },
            res_params={
            },
        ).run()

        self.related_variable_component.set_variable.assert_called_once_with(
            {
                SRC_VARIABLE: TEST_VARIABLE_NAME,
            }, {})
