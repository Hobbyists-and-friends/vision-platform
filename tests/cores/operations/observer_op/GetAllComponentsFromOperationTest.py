import unittest

from src.constants import *
from src.cores import System
from src.utils.Logging import Logging
from tests.constants import *

from src.operations.system_call import *
from tests.tools import load_test_image


class GetAllComponentsFromOperationTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()

        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=[
                TEST_CONVERT_IMAGE_TO_GRAY_OPERATION_ID,
                TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
            ],
        ).run()

        CreateVariableOperation(
            variable_id=TEST_IMAGE_SOURCE_NAME, variable_value=load_test_image()
        ).run()

        CreateVariableOperation(
            variable_id=TEST_GRAY_IMAGE_VARIABLE_NAME,
        ).run()

        CreateVariableOperation(
            variable_id=TEST_BINARY_IMAGE_VARIABLE_NAME,
        ).run()

        CreateVariableOperation(
            variable_id=TEST_THRESHOLD_VARIABLE_NAME,
            variable_value=TEST_THRESHOLD_VARIABLE_VALUE,
        ).run()

        CreateGUIComponentOperation(
            component_id=TEST_SLIDER_COMPONENT_ID,
            component_type=ComponentType.SLIDER.value,
        ).run()

        SetComponentRelatedVariableOperation(
            component_id=TEST_SLIDER_COMPONENT_ID,
            src_params={
                SRC_VARIABLE: TEST_THRESHOLD_VARIABLE_NAME,
            },
            res_params={},
        ).run()

        CreateOperationOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_GRAY_OPERATION_ID,
            operation_type=OperationType.CONVERT_IMAGE_TO_GRAY.value,
        ).run()

        SetOperationRelatedVariableOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_GRAY_OPERATION_ID,
            src_params_dict={SRC_VARIABLE: TEST_IMAGE_SOURCE_NAME},
            res_params_dict={RESULT_VARIABLE: TEST_GRAY_IMAGE_VARIABLE_NAME},
        ).run()

        CreateOperationOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
            operation_type=OperationType.CONVERT_IMAGE_TO_BINARY.value,
        ).run()

        SetOperationRelatedVariableOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
            src_params_dict={
                SRC_VARIABLE: TEST_GRAY_IMAGE_VARIABLE_NAME,
                THRESHOLD_VARIABLE: TEST_THRESHOLD_VARIABLE_NAME,
            },
            res_params_dict={RESULT_VARIABLE: TEST_BINARY_IMAGE_VARIABLE_NAME},
        ).run()

        CreateVariableOperation(
            variable_id=TEST_LIST_COMPONENTS_TEST, variable_value=[]
        ).run()

    def test_get_all_components_from_operation(self):
        CreateOperationOperation(
            operation_id=TEST_GET_ALL_COMPONENTS_FROM_OPERATION,
            operation_type=OperationType.GET_ALL_COMPONENTS.value,
        ).run()

        CreateVariableOperation(
            variable_id=TEST_OPERATION_NAME,
            variable_value=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
        ).run()

        SetOperationRelatedVariableOperation(
            operation_id=TEST_GET_ALL_COMPONENTS_FROM_OPERATION,
            src_params_dict={
                OPERATION_REF: TEST_OPERATION_NAME,
            },
            res_params_dict={RESULT_VARIABLE: TEST_LIST_COMPONENTS_TEST},
        ).run()

        list_components_values = self.system.variables[TEST_LIST_COMPONENTS_TEST].data[
            VALUE_KEY
        ]

        self.assertListEqual(list_components_values, [TEST_SLIDER_COMPONENT_ID])
