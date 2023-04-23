import unittest
from unittest.mock import (
    Mock,
)

from src.cores import (
    System,
)
from src.interfaces import (
    IObserver,
)
from src.operations.system_call import (
    CreateGUIComponentOperation,
)
from src.constants import (
    ComponentType,
)

from tests.constants import (
    TEST_UI_COMPONENT_NAME,
    TEST_COMPONENT_LAYOUT,
)


class CreateGUIComponentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.error_observer = Mock(spec=IObserver)
        self.system.error.add_observer(self.error_observer)

    def test_create_valid_component(self):
        operation = CreateGUIComponentOperation(
            component_id=TEST_UI_COMPONENT_NAME,
            component_type=ComponentType.BUTTON.value,
        )

        operation.run()

        self.assertTrue(
            TEST_UI_COMPONENT_NAME in self.system.ui_components
        )

    def test_create_existed_component(self):
        operation = CreateGUIComponentOperation(
            component_id=TEST_UI_COMPONENT_NAME,
            component_type=ComponentType.BUTTON.value,
        )
        operation.run()

        operation.run()

        self.assertEqual(self.error_observer.update.call_count, 2)
