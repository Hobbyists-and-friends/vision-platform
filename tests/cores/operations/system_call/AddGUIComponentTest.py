import unittest
from unittest.mock import (
    Mock,
)

from src.interfaces import (
    IObserver,
)
from src.constants import (
    ComponentType,
)
from src.interfaces.ui import (
    IUIComponent,
    IWindow,
)
from src.operations.system_call import (
    CreateGUIComponentOperation,
    AddGUIComponentOperation,
)
from src.cores import (
    System,
)

from tests.constants import *


class AddGUIComponentTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.error_observer = Mock(spec=IObserver)
        self.system.error.add_observer(self.error_observer)

        self.app = Mock(spec=IWindow)
        self.system.add_application(self.app)

        CreateGUIComponentOperation(
            component_id=TEST_UI_COMPONENT_NAME,
            component_type=ComponentType.BUTTON.value,
        ).run()

    def test_add_valid_component(self):
        operation = AddGUIComponentOperation(
            component_id=TEST_UI_COMPONENT_NAME,
            layout=TEST_COMPONENT_LAYOUT,
        )

        operation.run()

        self.app.add_component.assert_called_once()

    def test_add_non_existed_component(self):
        operation = AddGUIComponentOperation(
            component_id=TEST_NON_EXISTED_UI_COMPONENT_NAME,
            layout=TEST_COMPONENT_LAYOUT,
        )

        operation.run()

        self.assertEqual(self.error_observer.update.call_count,
                         CALL_OBSERVER_COUNT)
