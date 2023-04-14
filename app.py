import sys
from PyQt5.QtWidgets import QApplication

from src.gui import (
    ApplicationGUI,
)
from src.gui.customs import (
    IconButton,
    ImageDisplay,
)
from src.operations import (
    LoadLayoutOperation,
    CreateIconButtonOpeartion,
    AddGUIComponentOperation,
    LogVariableOperation,
    AddOperationObserverOperation,
    CreateVariableOperation,
    AddVariableObserverOperation,
    CreateApplicationOperation,
    RunApplicationOperation,
    ChangeVariableValueOperation,
)
# from src.gui.customs import (

# )
from src.cores import System


# The code below is used for testing purpose only.
import cv2 as cv
# The code above is used for testing purpose only.


# Home Screen constants
HOME_APPLICATION_NAME = 'Home Application'

HOME_APPLICATION_RUN_TEST_APPLICATIN_BUTTON = 'Run Test Application Button'
RUN_TEST_APPLICATION_OPERATION_ID = 'Run Test Application'

HOME_APPLICATION_VARIABLE_NAME = 'Home Variable'
HOME_APPLICATION_VARIABLE_VALUE = 'Home Value'

LOG_HOME_VARIABLE_OPERATION_ID = 'Log Home Variable'

# Test Application constants
TEST_APPLICATION_NAME = 'Test Application'

TEST_APPLICATION_LOG_VARIABLE_BUTTON = 'Log Variable Button'
TEST_APPLICATION_RUN_HOME_APPLICATION_BUTTON = 'Run Home Application Button'

TEST_APPLICATION_RUN_HOME_APPLICATION_ID = 'Run Home Application'

TEST_APPLICATION_LOG_VARIABLE_OPERATION_ID = 'Log Variable Operation'
TEST_APPLICATION_VARIABLE_NAME = 'Test Variable'
TEST_APPLICATION_VARIABLE_VALUE = 'Test Value'


def main():
    app = QApplication(sys.argv)
    system = System()

    operations = [
        CreateApplicationOperation(
            system=system,
            operation_id='Create Home Application',
            application_name=HOME_APPLICATION_NAME,
            operations=[
                LoadLayoutOperation(
                    system=system,
                    operation_id='Load Home Screen Layout',
                    layout_name='src/assets/layouts/test_layout.ui',
                ),
                CreateVariableOperation(
                    system=system,
                    operation_id='Create Test Variable',
                    variable_name=HOME_APPLICATION_VARIABLE_NAME,
                    variable_value=HOME_APPLICATION_VARIABLE_VALUE,
                ),
                CreateIconButtonOpeartion(
                    system=system,
                    operation_id='Create Test Button',
                    component_id=HOME_APPLICATION_RUN_TEST_APPLICATIN_BUTTON,
                    text='Test Button',
                ),
                AddGUIComponentOperation(
                    system=system,
                    operation_id='Add Test Button',
                    component_id=HOME_APPLICATION_RUN_TEST_APPLICATIN_BUTTON,
                    layout='test_layout',
                ),
                RunApplicationOperation(
                    system=system,
                    operation_id=RUN_TEST_APPLICATION_OPERATION_ID,
                    application_name=TEST_APPLICATION_NAME,
                    store=True,
                    run_at_first=False,
                ),
                LogVariableOperation(
                    system=system,
                    operation_id=LOG_HOME_VARIABLE_OPERATION_ID,
                    variable_id=HOME_APPLICATION_VARIABLE_NAME,
                    store=True,
                ),
                AddOperationObserverOperation(
                    system=system,
                    operation_id='Add Test Application Button Observer',
                    observer_operation_id=RUN_TEST_APPLICATION_OPERATION_ID,
                    observer_ui_component_id=HOME_APPLICATION_RUN_TEST_APPLICATIN_BUTTON,
                ),
                # AddOperationObserverOperation(
                #     system=system,
                #     operation_id='Add Home Variable Observer',
                #     observer_operation_id=LOG_HOME_VARIABLE_OPERATION_ID,
                #     observer_ui_component_id=HOME_APPLICATION_RUN_TEST_APPLICATIN_BUTTON,
                # ),
            ],
        ),
        CreateApplicationOperation(
            system=system,
            operation_id='Create Test Application',
            application_name=TEST_APPLICATION_NAME,
            operations=[
                LoadLayoutOperation(
                    system=system,
                    operation_id='Load Test Application Layout',
                    layout_name='src/assets/layouts/test_layout.ui',
                ),
                CreateVariableOperation(
                    system=system,
                    operation_id='Create Test Variable',
                    variable_name=TEST_APPLICATION_VARIABLE_NAME,
                    variable_value=TEST_APPLICATION_VARIABLE_VALUE,
                ),
                CreateIconButtonOpeartion(
                    system=system,
                    operation_id='Create Log Variable Button',
                    component_id=TEST_APPLICATION_LOG_VARIABLE_BUTTON,
                    text='Log Variable',
                ),
                LogVariableOperation(
                    system=system,
                    operation_id=TEST_APPLICATION_LOG_VARIABLE_OPERATION_ID,
                    variable_id=TEST_APPLICATION_VARIABLE_NAME,
                    store=True,
                ),
                AddGUIComponentOperation(
                    system=system,
                    operation_id='Add Log Variable Button',
                    component_id=TEST_APPLICATION_LOG_VARIABLE_BUTTON,
                    layout='test_layout',
                ),
                CreateIconButtonOpeartion(
                    system=system,
                    operation_id='Create Run Home Application Button',
                    component_id=TEST_APPLICATION_RUN_HOME_APPLICATION_BUTTON,
                    text='Run Home Application',
                ),
                AddGUIComponentOperation(
                    system=system,
                    operation_id='Add Run Home Application Button',
                    component_id=TEST_APPLICATION_RUN_HOME_APPLICATION_BUTTON,
                    layout='test_layout',
                ),
                RunApplicationOperation(
                    system=system,
                    operation_id=TEST_APPLICATION_RUN_HOME_APPLICATION_ID,
                    application_name=HOME_APPLICATION_NAME,
                    store=True,
                    run_at_first=False,
                ),
                AddOperationObserverOperation(
                    system=system,
                    operation_id='Add run home application button observer',
                    observer_operation_id=TEST_APPLICATION_RUN_HOME_APPLICATION_ID,
                    observer_ui_component_id=TEST_APPLICATION_RUN_HOME_APPLICATION_BUTTON,
                ),
                AddOperationObserverOperation(
                    system=system,
                    operation_id='Add log variable button observer',
                    observer_operation_id=TEST_APPLICATION_LOG_VARIABLE_OPERATION_ID,
                    observer_ui_component_id=TEST_APPLICATION_LOG_VARIABLE_BUTTON,
                ),
            ]
        ),
        RunApplicationOperation(
            system=system,
            operation_id='Run Home Application',
            application_name=HOME_APPLICATION_NAME,
        )
    ]

    win = ApplicationGUI(system)
    system.add_application(win)

    for operation in operations:
        operation.run()

    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
