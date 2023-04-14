import unittest
from unittest.mock import (
    Mock,
)

from src.interfaces import (
    IObserver,
)

from src.cores import (
    Variable,
    System,
)
from src.constants import (
    VariableType,
)
from src.operations import (
    CreateVariableOperation,
    AddVariableObserverOperation,
)

from tests.constants import (
    TEST_IMAGE_VARIABLE_NAME,
    TEST_CREATE_VARIABLE_OPERATION_NAME,
    TEST_UI_COMPONENT_NAME,
)
from tests.tools import (
    load_test_image,
)


ADD_VARIABLE_OBSERVER_TEST_NAME = 'add_variable_observer_test_name'


class AddVariableObserverTest(unittest.TestCase):
    def setUp(self):
        self.system = System()
        self.observer = Mock(spec=IObserver)

        self._setup_image()
        self._setup_component()

    def _setup_image(self):
        CreateVariableOperation(
            self.system,
            TEST_CREATE_VARIABLE_OPERATION_NAME,
            TEST_IMAGE_VARIABLE_NAME,
            load_test_image()).run()

    def _setup_component(self):
        self.system.ui_components[TEST_UI_COMPONENT_NAME] = self.observer

    def test_call_when_the_variable_notify(self):
        AddVariableObserverOperation(
            self.system,
            operation_id=ADD_VARIABLE_OBSERVER_TEST_NAME,
            variable_id=TEST_IMAGE_VARIABLE_NAME,
            observer_id=TEST_UI_COMPONENT_NAME,
        ).run()

        self.system.variables[TEST_IMAGE_VARIABLE_NAME].notify()

        self.assertEqual(
            self.observer.update.call_count,
            2
        )
