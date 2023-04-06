import unittest
from unittest.mock import (
    Mock,
    patch,
)

from src.interfaces import (
    ISystem,
    IOperation,
    IApplicationGUI,
    IGUIComponent,
)
from src.utils import (
    PublisherBase,
)

from tests.constants import (
    TEST_OPERATION_NAME,
    TEST_UI_COMPONENT_NAME,
    TEST_ADD_OBSERVER_OPERATION_NAME,
)
from tests.tools import (
    create_mocked_int_variable,
    create_mocked_system,
    create_mocked_ui_component,
    creat_mocked_operation,
    add_operation_system,
)

from src.operations import (
    AddOperationObserverOperation,
)


class AddOpeartionObserverTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = Mock(spec=ISystem)
        self.application = Mock(spec=IApplicationGUI)
        self.ui_component = PublisherBase()
        self.operation = Mock(spec=IOperation)

        create_mocked_system(self.system, self.ui_component, self.application)
        create_mocked_ui_component(self.ui_component)
        creat_mocked_operation(self.operation)
        add_operation_system(self.system, self.operation)

    def test_the_operation_should_update_when_the_ui_component_notify(self):
        operation = AddOperationObserverOperation(
            self.system,
            TEST_ADD_OBSERVER_OPERATION_NAME,
            TEST_OPERATION_NAME,
            TEST_UI_COMPONENT_NAME,
        )

        operation.run()

        self.ui_component.notify()
        self.operation.update.assert_called_once()
