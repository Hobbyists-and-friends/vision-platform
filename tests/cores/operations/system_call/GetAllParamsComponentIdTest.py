import unittest
from unittest.mock import (
    Mock,
)

from src.cores import System
from src.interfaces import (
    IObserver,
)
from src.constants import *
from src.operations.system_call import *
from tests.constants import *
from tests.tools import *


class GetAllParamsComponentIdTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.error_obsever = Mock(spec=IObserver)
        self.system.error.add_observer(self.error_obsever)

        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

        CreateGUIComponentOperation(
            component_id=TEST_SLIDER_COMPONENT_ID,
            component_type=ComponentType.SLIDER.value,
            label=TEST_SLIDER_COMPONENT_ID,
        ).run()

        SetComponentRelatedVariableOperation(
            component_id=TEST_SLIDER_COMPONENT_ID,
            src_params={
                SRC_VARIABLE: TEST_VARIABLE_NAME,
            },
            res_params={},
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

        CreateOperationOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_GRAY_OPERATION_ID,
            operation_type=OperationType.CONVERT_IMAGE_TO_GRAY.value,
        ).run()

        CreateVariableOperation(
            variable_id=TEST_OPERATION_VARAIABLE_REF_VARIABLE,
            variable_value=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
        ).run()

        CreateOperationOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
            operation_type=OperationType.CONVERT_IMAGE_TO_BINARY.value,
        ).run()

        SetOperationRelatedVariableOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_GRAY_OPERATION_ID,
            src_params_dict={
                SRC_VARIABLE: TEST_IMAGE_SOURCE_NAME,
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_GRAY_IMAGE_VARIABLE_NAME,
            },
        ).run()

        SetOperationRelatedVariableOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
            src_params_dict={
                SRC_VARIABLE: TEST_GRAY_IMAGE_VARIABLE_NAME,
                THRESHOLD_VARIABLE: TEST_VARIABLE_NAME,
            },
            res_params_dict={},
        ).run()

        CreateVariableOperation(
            variable_id=TEST_RELATED_COMPONENT_LIST_VARIABLE_NAME,
        ).run()

    def test_get_all_params_components(self):
        GetAllParamsComponentOperation(
            operation_id=TEST_CONVERT_IMAGE_TO_BINARY_OPREATEION_ID,
            variable_id=TEST_RELATED_COMPONENT_LIST_VARIABLE_NAME,
        ).run()

        self.assertListEqual(
            self.system.variables[TEST_RELATED_COMPONENT_LIST_VARIABLE_NAME].data[
                VALUE_KEY
            ],
            [TEST_SLIDER_COMPONENT_ID],
        )

    def test_get_all_params_component_via_variable_ref(self):
        GetAllParamsComponentOperation(
            operation_ref=TEST_OPERATION_VARAIABLE_REF_VARIABLE,
            variable_id=TEST_RELATED_COMPONENT_LIST_VARIABLE_NAME,
        ).run()

        self.assertListEqual(
            self.system.variables[TEST_RELATED_COMPONENT_LIST_VARIABLE_NAME].data[
                VALUE_KEY
            ],
            [TEST_SLIDER_COMPONENT_ID],
        )

    def test_get_all_params_component_without_both_operation_ref_and_id(self):
        GetAllParamsComponentOperation(
            variable_id=TEST_RELATED_COMPONENT_LIST_VARIABLE_NAME,
        ).run()

        self.assertEqual(
            self.error_obsever.update.call_count,
            CALL_OBSERVER_COUNT,
        )
