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
    CreateImageDisplayOperation,
    LoadImageOperation,
    ConvertImageToGrayOperation,
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

TEST_APPLICATION_IMAGE_PATH_VARIABLE_NAME = 'Test Image Path Variable'
TEST_APPLICATION_IMAGE_PATH_VARIABLE_VALUE = 'src/assets/images/test_image.jpg'

TEST_IMAGE_VARIABLE_NAME = 'Test Image Variable'

TEST_IMAGE_DISPLAY_COMPONENT_ID = 'Test Image Display Component'

TEST_APPLICATION_RESULT_IMAGE_VARIABLE_NAME = 'Test Result Image Variable'
TEST_RESULT_IMAGE_VARIABLE_NAME = 'Test Result Image Variable'

TEST_RESULT_IMAGE_DISPLAY_COMPONENT_ID = 'Test Result Image Display Component'


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
                    layout_name='src/assets/layouts/test_application_layout.ui',
                ),
                CreateVariableOperation(
                    system=system,
                    operation_id='Create Image Path Variable',
                    variable_name=TEST_APPLICATION_IMAGE_PATH_VARIABLE_NAME,
                    variable_value=TEST_APPLICATION_IMAGE_PATH_VARIABLE_VALUE,
                ),
                CreateVariableOperation(
                    system=system,
                    operation_id='Create Image Variable',
                    variable_name=TEST_IMAGE_VARIABLE_NAME,
                ),
                LoadImageOperation(
                    system=system,
                    operation_id='Load Image',
                    variable_id=TEST_IMAGE_VARIABLE_NAME,
                    image_path_variable_id=TEST_APPLICATION_IMAGE_PATH_VARIABLE_NAME,
                ),
                CreateVariableOperation(
                    system=system,
                    operation_id='Create Result Image Variable',
                    variable_name=TEST_APPLICATION_RESULT_IMAGE_VARIABLE_NAME,
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
                    layout='button_layout',
                ),
                CreateIconButtonOpeartion(
                    system=system,
                    operation_id='Create Run Home Application Button',
                    component_id=TEST_APPLICATION_RUN_HOME_APPLICATION_BUTTON,
                    text='Run Home Application',
                ),
                CreateImageDisplayOperation(
                    system=system,
                    operation_id='Create Image Display',
                    component_id=TEST_IMAGE_DISPLAY_COMPONENT_ID,
                    variable_id=TEST_IMAGE_VARIABLE_NAME,
                ),
                CreateImageDisplayOperation(
                    system=system,
                    operation_id='Create Result Image Display',
                    component_id=TEST_RESULT_IMAGE_DISPLAY_COMPONENT_ID,
                    variable_id=TEST_APPLICATION_RESULT_IMAGE_VARIABLE_NAME,
                ),
                AddGUIComponentOperation(
                    system=system,
                    operation_id='Add Image Display',
                    component_id=TEST_IMAGE_DISPLAY_COMPONENT_ID,
                    layout='source_image_layout',
                ),
                AddGUIComponentOperation(
                    system=system,
                    operation_id='Add Result Image Display',
                    component_id=TEST_RESULT_IMAGE_DISPLAY_COMPONENT_ID,
                    layout='result_image_layout',
                ),
                AddVariableObserverOperation(
                    system=system,
                    operation_id='Add Image display observer',
                    variable_id=TEST_IMAGE_VARIABLE_NAME,
                    observer_id=TEST_IMAGE_DISPLAY_COMPONENT_ID,
                ),
                AddVariableObserverOperation(
                    system=system,
                    operation_id='Add Result Image display observer',
                    variable_id=TEST_APPLICATION_RESULT_IMAGE_VARIABLE_NAME,
                    observer_id=TEST_RESULT_IMAGE_DISPLAY_COMPONENT_ID,
                ),
                AddGUIComponentOperation(
                    system=system,
                    operation_id='Add Run Home Application Button',
                    component_id=TEST_APPLICATION_RUN_HOME_APPLICATION_BUTTON,
                    layout='button_layout',
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
                ConvertImageToGrayOperation(
                    system=system,
                    operation_id='Convert Image to Gray',
                    source_variable_id=TEST_IMAGE_VARIABLE_NAME,
                    result_variable_id=TEST_APPLICATION_RESULT_IMAGE_VARIABLE_NAME,
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

    win.showMaximized()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
