import unittest
from unittest.mock import (
    Mock,
    PropertyMock,
)

from src.interfaces import (
    ISystem,
    IGUIComponent,
    IApplicationGUI,
)
from src.operations import (
    AddGUIComponentOperation,
)

from tests.constants import (
    TEST_OPERATION_NAME,
    TEST_UI_COMPONENT_NAME,
    TEST_COMPONENT_LAYOUT,
)

from tests.tools import (
    create_mocked_ui_component,
    create_mocked_system,
)


class AddGUIComponentTest(unittest.TestCase):
    def setUp(self):
        self.system = Mock(spec=ISystem)
        self.gui_component = Mock(spec=IGUIComponent)
        self.application = Mock(spec=IApplicationGUI)

        create_mocked_system(self.system, self.gui_component, self.application)
        create_mocked_ui_component(self.gui_component)

    def test_add_gui_component(self):
        operation = AddGUIComponentOperation(
            self.system,
            TEST_OPERATION_NAME,
            TEST_UI_COMPONENT_NAME,
            TEST_COMPONENT_LAYOUT)

        operation.run()

        self.application.add_component.assert_called_once_with(
            self.gui_component, TEST_COMPONENT_LAYOUT
        )

    def test_add_existed_gui_component(self):
        pass
