from enum import Enum


class OperationType(Enum):
    """Operation type enum."""

    # Observer operations
    LOG_VARIABLE = "Log Variable"

    # System call operations
    PRINT_VARIABLE = "Print Variable"
    RAISE_ERROR = "Raise Error"

    CREATE_VARIABLE = "Create Variable"
    CREATE_GUI_COMPONENT = "Create GUI Component"
    CREATE_OPERATION = "Create Operation"

    CHANGE_VARIABLE = "Change Variable"

    SET_DISPATCH = "Set Dispatch"
    ADD_VARIABLE_OBSERVER = "Add Variable Observer"
    ADD_GUI_COMPONENT = "Add GUI Component Observer"

    GET_PARAMS_FROM_OBSERVER = "Get Params From Observer"

    # Image operations
    CONVERT_IMAGE_TO_GRAY = "Convert Image to Gray"
    CONVERT_IMAGE_TO_BINARY = "Convert Image to Binary"

    # Transform operations
    TRANSFORM_VARIABLE_TO_VALUE = "Transform Variable to Value"
    GET_PARAM_FROM_MULTI_OBSERVER = "Get Param From Multi Observer"
    GET_ALL_COMPONENTS = "Get All Componentts"
