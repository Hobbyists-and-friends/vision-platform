from enum import Enum
import numpy as np


class VariableType(Enum):
    NUMBER = 'number'
    STRING = 'string'
    BUTTON = 'button'
    IMAGE = 'image'
    OPERATION = 'operation'
    OPERATION_FLOW = 'operation_flow'
    NULL = 'null'

    def get_type_from_value(value: 'object') -> 'VariableType':
        if isinstance(value, int) or isinstance(value, float):
            return VariableType.NUMBER
        elif isinstance(value, str):
            return VariableType.STRING
        elif isinstance(value, np.ndarray):
            return VariableType.IMAGE
        else:
            return VariableType.NULL
