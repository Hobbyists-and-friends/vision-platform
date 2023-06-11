import sys
from src.operations.system_call import *
from src.cores import *
from src.gui import *
from src.gui.customs import *
from src.constants import *
from src.utils.Logging import Logging

Logging.setup()
Logging.get_src_path(__file__)
print(Logging.src_folder_path)
# Logging.get_info_level()


# The code below is used for testing purpose only.
import cv2 as cv

# The code above is used for testing purpose only.


# Home Screen constants
HOME_APPLICATION_NAME = "Home Application"

HOME_APPLICATION_RUN_TEST_APPLICATIN_BUTTON = "Run Test Application Button"
RUN_TEST_APPLICATION_OPERATION_ID = "Run Test Application"

HOME_APPLICATION_VARIABLE_NAME = "Home Variable"
HOME_APPLICATION_VARIABLE_VALUE = 30

LOG_HOME_VARIABLE_OPERATION_ID = "Log Home Variable"

# Test Application constants
TEST_APPLICATION_NAME = "Test Application"

TEST_APPLICATION_LOG_VARIABLE_BUTTON = "Log Variable Button"
TEST_APPLICATION_RUN_HOME_APPLICATION_BUTTON = "Run Home Application Button"

TEST_APPLICATION_RUN_HOME_APPLICATION_ID = "Run Home Application"

TEST_APPLICATION_LOG_VARIABLE_OPERATION_ID = "Log Variable Operation"
TEST_APPLICATION_VARIABLE_NAME = "Test Variable"
TEST_APPLICATION_VARIABLE_VALUE = 3

TEST_APPLICATION_IMAGE_PATH_VARIABLE_NAME = "Test Image Path Variable"
TEST_APPLICATION_IMAGE_PATH_VARIABLE_VALUE = "src/assets/images/test_image.jpg"

TEST_IMAGE_VARIABLE_NAME = "Test Image Variable"

TEST_IMAGE_DISPLAY_COMPONENT_ID = "Test Image Display Component"

TEST_APPLICATION_RESULT_IMAGE_VARIABLE_NAME = "Test Result Image Variable"
TEST_RESULT_IMAGE_VARIABLE_NAME = "Test Result Image Variable"

TEST_RESULT_IMAGE_DISPLAY_COMPONENT_ID = "Test Result Image Display Component"

TEST_APPLICATION_BINARY_IMAGE_VARIABLE_NAME = "Test Binary Image Variable"
TEST_APPLICATION_BINARY_IMAGE_DISPLAY_COMPONENT_ID = (
    "Test Binary Image Display Component"
)
TEST_APPLICATION_CONVERT_IMAGE_TO_BINARY_OPERATION_ID = (
    "Convert Image To Binary Operation"
)

SLIDER_COMPONENT_ID = "Test Slider Component"

TEST_APPLICATION_CONVERT_IMAGE_TO_BINARY_OPERATION_ID = (
    "Convert Image To Binary Operation"
)


def main():
    system = System()
    window = PyQtWindow("src/assets/layouts/test_layout.ui", sys.argv)

    SOURCE_IMAGE_VARAIBLE_NAME = "Image Source Variable"
    GRAY_IMAGE_VARIABLE_NAME = "Gray Image Variable"
    BINARY_IMAGE_VARIABLE_NAME = "Binary Image Variable Name"
    IMAGE_PATH_NAME = "Image Path"

    CONVERT_IMAGE_TO_GRAY_OPERATION = "Convert Image To Gray Operation"

    BINARY_TYPE_VARIABLE_NAME = "Binary Type Variable"
    BINARY_TYPE_COMBO_BOX_NAME = "Binary Type ComboBox Name"

    THRESHOLD_VARIABLE_NAME = "Threshold Variable"
    THRESHOLD_SLIDER_COMPONENT_NAME = "Threshold Slider Component name"

    CONVERT_IMAGE_TO_BINARY_OPERATION = "Convert Image To Binary Operation"

    IMAGE_DISPLAY_COMPONENT_NAME = "Image Display"

    OPERATION_LIST_VARIABLE_NAME = "Operations List Variable"
    OPERATION_LIST_COMPONENT_NAME = "Operations List Component"

    OPERATIONA_PARAM_LIST_COMPONENT_NAME = "Operation Param List Component Name"
    OPERATION_COMPONENTS_VARIABLE_NAME = "Operation Component Variable Name"
    GET_OPERATION_COMPONENTS_OPERATION = "Get operation components operations"

    OPERATION_LIST_COMPONENT_RESULT = "Operation List Component result"

    COMPONENT_LIST_NAME = "Component List Name"
    LOG_OPERATION_BUTTON_LIST_NAME = "Log Operation Button List Result"

    load_image_source = [
        CreateVariableOperation(variable_id=SOURCE_IMAGE_VARAIBLE_NAME),
        CreateVariableOperation(
            variable_id=IMAGE_PATH_NAME,
            variable_value="src/assets/images/test_image.jpg",
        ),
        LoadImageOperation(
            variable_id=SOURCE_IMAGE_VARAIBLE_NAME,
            image_path_variable_id=IMAGE_PATH_NAME,
        ),
    ]

    convert_image_to_gray = [
        CreateOperationOperation(
            operation_id=CONVERT_IMAGE_TO_GRAY_OPERATION,
            operation_type=OperationType.CONVERT_IMAGE_TO_GRAY.value,
        ),
        SetOperationRelatedVariableOperation(
            operation_id=CONVERT_IMAGE_TO_GRAY_OPERATION,
            src_params_dict={
                SRC_VARIABLE: SOURCE_IMAGE_VARAIBLE_NAME,
            },
            res_params_dict={
                RESULT_VARIABLE: GRAY_IMAGE_VARIABLE_NAME,
            },
            auto_mode=True,
        ),
    ]

    convert_image_to_binary = [
        CreateOperationOperation(
            operation_id=CONVERT_IMAGE_TO_BINARY_OPERATION,
            operation_type=OperationType.CONVERT_IMAGE_TO_BINARY.value,
        ),
        SetOperationRelatedVariableOperation(
            operation_id=CONVERT_IMAGE_TO_BINARY_OPERATION,
            src_params_dict={
                SRC_VARIABLE: GRAY_IMAGE_VARIABLE_NAME,
                TYPE_VARIABLE: BINARY_TYPE_VARIABLE_NAME,
                THRESHOLD_VARIABLE: THRESHOLD_VARIABLE_NAME,
            },
            res_params_dict={
                RESULT_VARIABLE: BINARY_IMAGE_VARIABLE_NAME,
            },
            auto_mode=True,
        ),
    ]

    binary_threshold_display = [
        CreateGUIComponentOperation(
            component_id=THRESHOLD_SLIDER_COMPONENT_NAME,
            component_type=ComponentType.SLIDER.value,
            label="Threshold",
            max=255,
        ),
        SetComponentRelatedVariableOperation(
            component_id=THRESHOLD_SLIDER_COMPONENT_NAME,
            src_params={
                SRC_VARIABLE: THRESHOLD_VARIABLE_NAME,
            },
            res_params={},
        ),
    ]

    binary_type_display = [
        CreateGUIComponentOperation(
            component_id=BINARY_TYPE_COMBO_BOX_NAME,
            component_type=ComponentType.COMBO_BOX.value,
            values=[
                cv.THRESH_BINARY,
                cv.THRESH_BINARY_INV,
                cv.THRESH_TOZERO,
                cv.THRESH_TOZERO_INV,
            ],
            alias=[
                "THRESH_BINARY",
                "THRESH_BINARY_INV",
                "THRESH_TOZERO",
                "THRESH_TOZERO_INV",
            ],
            label="Binary Type",
        ),
        SetComponentRelatedVariableOperation(
            component_id=BINARY_TYPE_COMBO_BOX_NAME,
            src_params={
                SRC_VARIABLE: BINARY_TYPE_VARIABLE_NAME,
            },
            res_params={},
        ),
    ]

    operation_list_display = [
        CreateVariableOperation(
            variable_id=OPERATION_LIST_VARIABLE_NAME,
            variable_value=[
                CONVERT_IMAGE_TO_GRAY_OPERATION,
                CONVERT_IMAGE_TO_BINARY_OPERATION,
            ],
        ),
        CreateGUIComponentOperation(
            component_id=OPERATION_LIST_COMPONENT_NAME,
            component_type=ComponentType.BUTTON_LIST.value,
        ),
        AddGUIComponentOperation(
            component_id=OPERATION_LIST_COMPONENT_NAME, layout="test_layout"
        ),
        SetComponentRelatedVariableOperation(
            component_id=OPERATION_LIST_COMPONENT_NAME,
            src_params={
                SRC_VARIABLE: OPERATION_LIST_VARIABLE_NAME,
            },
            res_params={
                RESULT_VARIABLE: OPERATION_LIST_COMPONENT_RESULT,
            },
            auto_mode=True,
        ),
        CreateOperationOperation(
            operation_id=LOG_OPERATION_BUTTON_LIST_NAME,
            operation_type=OperationType.LOG_VARIABLE.value,
        ),
        SetOperationRelatedVariableOperation(
            operation_id=LOG_OPERATION_BUTTON_LIST_NAME,
            src_params_dict={
                SRC_VARIABLE: OPERATION_LIST_COMPONENT_RESULT,
            },
            res_params_dict={},
        ),
    ]

    get_operation_components = [
        CreateVariableOperation(
            variable_id=OPERATION_COMPONENTS_VARIABLE_NAME,
        ),
        CreateOperationOperation(
            operation_id=GET_OPERATION_COMPONENTS_OPERATION,
            operation_type=OperationType.GET_ALL_COMPONENTS.value,
        ),
        SetOperationRelatedVariableOperation(
            operation_id=GET_OPERATION_COMPONENTS_OPERATION,
            src_params_dict={
                OPERATION_REF: OPERATION_LIST_COMPONENT_RESULT,
            },
            res_params_dict={
                RESULT_VARIABLE: OPERATION_COMPONENTS_VARIABLE_NAME,
            },
        ),
        CreateGUIComponentOperation(
            component_id=COMPONENT_LIST_NAME,
            component_type=ComponentType.COMPONENT_LIST.value,
        ),
        AddGUIComponentOperation(
            component_id=COMPONENT_LIST_NAME, layout="operation_layout"
        ),
        SetComponentRelatedVariableOperation(
            component_id=COMPONENT_LIST_NAME,
            src_params={
                SRC_VARIABLE: OPERATION_COMPONENTS_VARIABLE_NAME,
            },
            res_params={},
        ),
    ]

    create_image_display = [
        CreateGUIComponentOperation(
            component_id=IMAGE_DISPLAY_COMPONENT_NAME,
            component_type=ComponentType.IMAGE_DISPLAY.value,
        ),
        AddGUIComponentOperation(
            component_id=IMAGE_DISPLAY_COMPONENT_NAME,
            layout="image_layout",
        ),
        SetComponentRelatedVariableOperation(
            component_id=IMAGE_DISPLAY_COMPONENT_NAME,
            src_params={
                SRC_VARIABLE: BINARY_IMAGE_VARIABLE_NAME,
            },
            res_params={},
        ),
    ]

    operations = (
        load_image_source
        + convert_image_to_gray
        + convert_image_to_binary
        + binary_threshold_display
        + binary_type_display
        + operation_list_display
        + create_image_display
        + get_operation_components
    )

    # operations = [
    #     CreateVariableOperation(
    #         variable_id=HOME_APPLICATION_VARIABLE_NAME,
    #         variable_value=HOME_APPLICATION_VARIABLE_VALUE,
    #     ),
    #     CreateGUIComponentOperation(
    #         component_id=HOME_APPLICATION_RUN_TEST_APPLICATIN_BUTTON,
    #         component_type=ComponentType.BUTTON.value,
    #     ),
    #     AddGUIComponentOperation(
    #         component_id=HOME_APPLICATION_RUN_TEST_APPLICATIN_BUTTON,
    #         layout='test_layout'
    #     ),
    #     CreateOperationOperation(
    #         operation_id=LOG_HOME_VARIABLE_OPERATION_ID,
    #         operation_type=OperationType.PRINT_VARIABLE.value,
    #         variable_id=HOME_APPLICATION_VARIABLE_NAME,
    #     ),
    #     CreateOperationOperation(
    #         operation_id="Log Variable",
    #         operation_type=OperationType.LOG_VARIABLE.value,
    #     ),
    #     AddVariableObserverOperation(
    #         variable_id=HOME_APPLICATION_VARIABLE_NAME,
    #         observer_id="Log Variable",
    #     ),
    #     SetDispatchOperation(
    #         operation_id=LOG_HOME_VARIABLE_OPERATION_ID,
    #         component_id=HOME_APPLICATION_RUN_TEST_APPLICATIN_BUTTON,
    #     ),
    #     CreateGUIComponentOperation(
    #         component_id="Slider",
    #         component_type=ComponentType.SLIDER.value,
    #         max=255,
    #         step=10,
    #         label="Threshold Value"
    #     ),
    #     AddGUIComponentOperation(
    #         component_id="Slider",
    #         layout='test_layout',
    #     ),
    #     SetComponentRelatedVariableOperation(
    #         component_id="Slider",
    #         src_params={
    #             SRC_VARIABLE: HOME_APPLICATION_VARIABLE_NAME,
    #         },
    #         res_params={},
    #     ),
    #     CreateVariableOperation(
    #         variable_id="ComboBox Variable",
    #         variable_value=cv.THRESH_BINARY,
    #     ),
    #     CreateOperationOperation(
    #         operation_id="Log ComboBox Variable",
    #         operation_type=OperationType.LOG_VARIABLE.value,
    #     ),
    #     AddVariableObserverOperation(
    #         variable_id="ComboBox Variable",
    #         observer_id="Log ComboBox Variable",
    #     ),
    #     CreateGUIComponentOperation(
    #         component_id="ComboBox",
    #         component_type=ComponentType.COMBO_BOX.value,
    #         values=[
    #             cv.THRESH_BINARY,
    #             cv.THRESH_BINARY_INV,
    #             cv.THRESH_TRUNC,
    #             cv.THRESH_TOZERO,
    #         ],
    #         alias=[
    #             "THR_BINARY",
    #             "THR_BINARY_INV",
    #             "THR_TRUNC",
    #             "THR_TOZERO",
    #         ],
    #         label="Threshold Type",
    #     ),
    #     # AddGUIComponentOperation(
    #     #     component_id="ComboBox",
    #     #     layout='test_layout',
    #     # ),
    #     SetComponentRelatedVariableOperation(
    #         component_id="ComboBox",
    #         src_params={
    #             SRC_VARIABLE: "ComboBox Variable",
    #         },
    #         res_params={},
    #     ),
    #     CreateVariableOperation(
    #         variable_id="Image Variable",
    #     ),

    #     LoadImageOperation(
    #         variable_id="Image Variable",
    #         image_path_variable_id="Image Path",
    #     ),
    #     CreateVariableOperation(
    #         variable_id="Gray Image Variable"
    #     ),
    #     CreateVariableOperation(
    #         variable_id="Result Image Variable",
    #     ),
    #     CreateOperationOperation(
    #         operation_id="Convert Image To Gray Operation",
    #         operation_type=OperationType.CONVERT_IMAGE_TO_GRAY.value,
    #     ),
    #     SetOperationRelatedVariableOperation(
    #         operation_id="Convert Image To Gray Operation",
    #         src_params_dict={
    #             SRC_VARIABLE: "Image Variable",
    #         },
    #         res_params_dict={
    #             RESULT_VARIABLE: "Gray Image Variable",
    #         },
    #     ),
    #     CreateVariableOperation(
    #         variable_id="Binary Image Variable",
    #     ),
    #     CreateOperationOperation(
    #         operation_id="Convert Image To Binary Operation",
    #         operation_type=OperationType.CONVERT_IMAGE_TO_BINARY.value,
    #     ),
    #     SetOperationRelatedVariableOperation(
    #         operation_id="Convert Image To Binary Operation",
    #         src_params_dict={
    #             SRC_VARIABLE: "Gray Image Variable",
    #             THRESHOLD_VARIABLE: HOME_APPLICATION_VARIABLE_NAME,
    #             TYPE_VARIABLE: "ComboBox Variable",
    #         },
    #         res_params_dict={
    #             RESULT_VARIABLE: "Binary Image Variable",
    #         },
    #     ),
    #     CreateVariableOperation(
    #         variable_id="Button's Name List",
    #         variable_value=[
    #             "Convert Image To Gray Operation",
    #             "Convert Image To Binary Operation",
    #         ],
    #     ),
    #     CreateVariableOperation(
    #         variable_id="Button List Result",
    #     ),
    #     CreateGUIComponentOperation(
    #         component_id="Button List",
    #         component_type=ComponentType.BUTTON_LIST.value,
    #     ),
    #     AddGUIComponentOperation(
    #         component_id="Button List",
    #         layout='test_layout',
    #     ),
    #     SetComponentRelatedVariableOperation(
    #         component_id="Button List",
    #         src_params={
    #             SRC_VARIABLE: "Button's Name List",
    #         },
    #         res_params={
    #             RESULT_VARIABLE: "Button List Result",
    #         },
    #     ),
    #     CreateOperationOperation(
    #         operation_id="Get Result Image Operation",
    #         operation_type=OperationType.GET_PARAM_FROM_MULTI_OBSERVER.value,
    #     ),
    #     CreateVariableOperation(
    #         variable_id="Operation Params List Result",
    #         variable_value=[
    #             RESULT_VARIABLE,
    #         ]
    #     ),
    #     SetOperationRelatedVariableOperation(
    #         operation_id="Get Result Image Operation",
    #         src_params_dict={
    #             SRC_OPERATION: "Button List Result",
    #             PARAM_VALUE: "Operation Params List Result",
    #         },
    #         res_params_dict={
    #             RESULT_VARIABLE: "Result Image Variable",
    #         },
    #     ),
    #     CreateOperationOperation(
    #         operation_id="Log Button List Result",
    #         operation_type=OperationType.LOG_VARIABLE.value,
    #     ),
    #     AddVariableObserverOperation(
    #         variable_id="Button List Result",
    #         observer_id="Log Button List Result",
    #     ),
    #     CreateOperationOperation(
    #         operation_id="Log Result Image Variable",
    #         operation_type=OperationType.LOG_VARIABLE.value,
    #     ),
    #     AddVariableObserverOperation(
    #         variable_id="Result Image Variable",
    #         observer_id="Log Result Image Variable",
    #     ),
    #     CreateGUIComponentOperation(
    #         component_id="Image Display",
    #         component_type=ComponentType.IMAGE_DISPLAY.value,
    #     ),
    #     AddGUIComponentOperation(
    #         component_id="Image Display",
    #         layout='image_layout',
    #     ),
    #     SetComponentRelatedVariableOperation(
    #         component_id="Image Display",
    #         src_params={
    #             SRC_VARIABLE: "Result Image Variable",
    #             # SRC_VARIABLE: "Binary Image Variable",
    #             # 'Binary': "Binary Image Variable",
    #             # 'Gray': "Gray Image Variable",
    #         },
    #         res_params={},
    #     ),
    #     CreateVariableOperation(
    #         variable_id="Operation Params List"
    #     ),
    #     GetAllParamsComponentOperation(
    #         operation_id='Convert Image To Binary Operation',
    #         variable_id='Operation Params List',
    #     ),
    #     CreateGUIComponentOperation(
    #         component_id="Operation Display",
    #         component_type=ComponentType.COMPONENT_LIST.value,
    #         label="Component List"
    #     ),
    #     AddGUIComponentOperation(
    #         component_id="Operation Display",
    #         layout='operation_layout',
    #         dock=True,
    #     ),
    #     SetComponentRelatedVariableOperation(
    #         component_id="Operation Display",
    #         src_params={
    #             SRC_VARIABLE: "Operation Params List",
    #         },
    #         res_params={},
    #     ),
    # ]
    system.add_application(window)
    window.init()
    for operation in operations:
        operation.run()
    window.update()
    window.exit()


def test():
    from src.utils.Logging import Logging

    Logging.setup()
    Logging.get_info_level()

    print(Logging.logger)
    Logging.debug(msg="Hello")
    Logging.info(msg="Start Program")


if __name__ == "__main__":
    # test()
    main()
