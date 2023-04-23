import sys
from src.operations.system_call import *
from src.cores import *
from src.gui import *
from src.gui.customs import *
from src.constants import *


# The code below is used for testing purpose only.
import cv2 as cv
# The code above is used for testing purpose only.


# Home Screen constants
HOME_APPLICATION_NAME = 'Home Application'

HOME_APPLICATION_RUN_TEST_APPLICATIN_BUTTON = 'Run Test Application Button'
RUN_TEST_APPLICATION_OPERATION_ID = 'Run Test Application'

HOME_APPLICATION_VARIABLE_NAME = 'Home Variable'
HOME_APPLICATION_VARIABLE_VALUE = 30

LOG_HOME_VARIABLE_OPERATION_ID = 'Log Home Variable'

# Test Application constants
TEST_APPLICATION_NAME = 'Test Application'

TEST_APPLICATION_LOG_VARIABLE_BUTTON = 'Log Variable Button'
TEST_APPLICATION_RUN_HOME_APPLICATION_BUTTON = 'Run Home Application Button'

TEST_APPLICATION_RUN_HOME_APPLICATION_ID = 'Run Home Application'

TEST_APPLICATION_LOG_VARIABLE_OPERATION_ID = 'Log Variable Operation'
TEST_APPLICATION_VARIABLE_NAME = 'Test Variable'
TEST_APPLICATION_VARIABLE_VALUE = 3

TEST_APPLICATION_IMAGE_PATH_VARIABLE_NAME = 'Test Image Path Variable'
TEST_APPLICATION_IMAGE_PATH_VARIABLE_VALUE = 'src/assets/images/test_image.jpg'

TEST_IMAGE_VARIABLE_NAME = 'Test Image Variable'

TEST_IMAGE_DISPLAY_COMPONENT_ID = 'Test Image Display Component'

TEST_APPLICATION_RESULT_IMAGE_VARIABLE_NAME = 'Test Result Image Variable'
TEST_RESULT_IMAGE_VARIABLE_NAME = 'Test Result Image Variable'

TEST_RESULT_IMAGE_DISPLAY_COMPONENT_ID = 'Test Result Image Display Component'

TEST_APPLICATION_BINARY_IMAGE_VARIABLE_NAME = 'Test Binary Image Variable'
TEST_APPLICATION_BINARY_IMAGE_DISPLAY_COMPONENT_ID = 'Test Binary Image Display Component'
TEST_APPLICATION_CONVERT_IMAGE_TO_BINARY_OPERATION_ID = 'Convert Image To Binary Operation'

SLIDER_COMPONENT_ID = 'Test Slider Component'

TEST_APPLICATION_CONVERT_IMAGE_TO_BINARY_OPERATION_ID = 'Convert Image To Binary Operation'


def main():
    system = System()
    window = PyQtWindow("src/assets/layouts/test_layout.ui", sys.argv)

    operations = [
        CreateVariableOperation(
            variable_id=HOME_APPLICATION_VARIABLE_NAME,
            variable_value=HOME_APPLICATION_VARIABLE_VALUE,
        ),
        CreateGUIComponentOperation(
            component_id=HOME_APPLICATION_RUN_TEST_APPLICATIN_BUTTON,
            component_type=ComponentType.BUTTON.value,
        ),
        AddGUIComponentOperation(
            component_id=HOME_APPLICATION_RUN_TEST_APPLICATIN_BUTTON,
            layout='test_layout'
        ),
        CreateOperationOperation(
            operation_id=LOG_HOME_VARIABLE_OPERATION_ID,
            operation_type=OperationType.PRINT_VARIABLE.value,
            variable_id=HOME_APPLICATION_VARIABLE_NAME,
        ),
        CreateOperationOperation(
            operation_id="Log Variable",
            operation_type=OperationType.LOG_VARIABLE.value,
        ),
        AddVariableObserverOperation(
            variable_id=HOME_APPLICATION_VARIABLE_NAME,
            observer_id="Log Variable",
        ),
        SetDispatchOperation(
            operation_id=LOG_HOME_VARIABLE_OPERATION_ID,
            component_id=HOME_APPLICATION_RUN_TEST_APPLICATIN_BUTTON,
        ),
        CreateGUIComponentOperation(
            component_id="Slider",
            component_type=ComponentType.SLIDER.value,
            max=255,
        ),
        AddGUIComponentOperation(
            component_id="Slider",
            layout='test_layout',
        ),
        SetComponentRelatedVariableOperation(
            component_id="Slider",
            variable_id=HOME_APPLICATION_VARIABLE_NAME,
        ),
        CreateVariableOperation(
            variable_id="ComboBox Variable",
            variable_value="Testing"
        ),
        CreateOperationOperation(
            operation_id="Log ComboBox Variable",
            operation_type=OperationType.LOG_VARIABLE.value,
        ),
        AddVariableObserverOperation(
            variable_id="ComboBox Variable",
            observer_id="Log ComboBox Variable",
        ),
        CreateGUIComponentOperation(
            component_id="ComboBox",
            component_type=ComponentType.COMBO_BOX.value,
            values=[
                "Hello",
                "Testing"
            ],
        ),
        AddGUIComponentOperation(
            component_id="ComboBox",
            layout='test_layout',
        ),
        SetComponentRelatedVariableOperation(
            component_id="ComboBox",
            variable_id="ComboBox Variable",
        ),
        CreateVariableOperation(
            variable_id="Image Variable",
        ),
        CreateVariableOperation(
            variable_id="Image Path",
            variable_value="src/assets/images/test_image.jpg",
        ),
        LoadImageOperation(
            variable_id="Image Variable",
            image_path_variable_id="Image Path",
        ),
        CreateVariableOperation(
            variable_id="Gray Image Variable"
        ),
        CreateVariableOperation(
            variable_id="Result Image Variable",
        ),
        CreateGUIComponentOperation(
            component_id="Image Display",
            component_type=ComponentType.IMAGE_DISPLAY.value,
        ),
        AddGUIComponentOperation(
            component_id="Image Display",
            layout='test_layout',
        ),
        SetComponentRelatedVariableOperation(
            component_id="Image Display",
            variable_id="Result Image Variable",
        ),
        CreateOperationOperation(
            operation_id="Convert Image To Gray Operation",
            operation_type=OperationType.CONVERT_IMAGE_TO_GRAY.value,
        ),
        SetOperationRelatedVariableOperation(
            operation_id="Convert Image To Gray Operation",
            src_params_dict={
                SRC_VARIABLE: "Image Variable",
            },
            res_params_dict={
                RESULT_VARIABLE: "Gray Image Variable",
            },
        ),
        CreateOperationOperation(
            operation_id="Convert Image To Binary Operation",
            operation_type=OperationType.CONVERT_IMAGE_TO_BINARY.value,
        ),
        SetOperationRelatedVariableOperation(
            operation_id="Convert Image To Binary Operation",
            src_params_dict={
                SRC_VARIABLE: "Gray Image Variable",
                THRESHOLD_VARIABLE: HOME_APPLICATION_VARIABLE_NAME,
            },
            res_params_dict={
                RESULT_VARIABLE: "Result Image Variable",
            },
        ),
    ]
    system.add_application(window)
    window.init()
    for operation in operations:
        operation.run()
    window.update()
    window.exit()


if __name__ == '__main__':
    main()
