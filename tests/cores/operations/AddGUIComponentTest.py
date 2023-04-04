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


TEST_COMPONENT_ID = 'test_component_id'
TEST_COMPONENT_LAYOUT = 'test_component_layout'


class AddGUIComponentTest(unittest.TestCase):
    def setUp(self):
        self.system = Mock(spec=ISystem)
        self.gui_component = Mock(spec=IGUIComponent)
        self.application = Mock(spec=IApplicationGUI)
        type(self.system).application = PropertyMock(
            return_value=self.application)

        type(self.gui_component).component_id = PropertyMock(
            return_value=TEST_COMPONENT_ID)

        ui_components = PropertyMock(return_value={
            TEST_COMPONENT_ID: self.gui_component
        })
        type(self.system).ui_components = ui_components

    def test_add_gui_component(self):
        operation = AddGUIComponentOperation(
            self.system, TEST_COMPONENT_ID, TEST_COMPONENT_LAYOUT)

        operation.run()

        self.application.add_component.assert_called_once_with(
            self.gui_component, TEST_COMPONENT_LAYOUT
        )
