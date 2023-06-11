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
from src.utils.MultiObserverBase import MultiObserverBase

from tests.constants import *


class SetComponentRelatedVariableTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.error_observer = Mock(spec=IObserver)
        self.system.error.add_observer(self.error_observer)
        self.related_variable_component = Mock(spec=MultiObserverBase)

        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

        self.system.ui_components[
            TEST_UI_COMPONENT_NAME
        ] = self.related_variable_component

    def test_set_component_related_valid_variable(self):
        SetComponentRelatedVariableOperation(
            component_id=TEST_UI_COMPONENT_NAME,
            src_params={
                SRC_VARIABLE: TEST_VARIABLE_NAME,
            },
            res_params={},
        ).run()

        self.assertEqual(
            self.system.variables[TEST_VARIABLE_NAME].data[RELATED_COMPONENT],
            TEST_UI_COMPONENT_NAME,
        )

    def test_set_component_related_non_existed_variable(self):
        SetComponentRelatedVariableOperation(
            component_id=TEST_UI_COMPONENT_NAME,
            src_params={
                SRC_VARIABLE: TEST_NON_EXISTED_VARIABLE_NAME,
            },
            res_params={},
        ).run()

        self.assertEqual(self.error_observer.update.call_count, CALL_OBSERVER_COUNT)

    def test_set_component_related_non_existed_variable_auto_mode(self):
        SetComponentRelatedVariableOperation(
            component_id=TEST_UI_COMPONENT_NAME,
            src_params={
                SRC_VARIABLE: TEST_NON_EXISTED_VARIABLE_NAME,
            },
            res_params={},
            auto_mode=True,
        ).run()

        self.assertTrue(TEST_NON_EXISTED_VARIABLE_NAME in self.system.variables.keys())
