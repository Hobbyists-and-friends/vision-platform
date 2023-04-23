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
