import unittest
from unittest.mock import (
    Mock,
)

from src.cores import System
from src.constants import *
from src.operations.system_call import *
from src.interfaces import (
    IObserver,
)
from tests.constants import *
from tests.tools import *


NON_LIST_SRC_VARIABLE = SRC_VARIABLE + "NON_LIST"


class GetParamFromMultiObserverTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.error_observer = Mock(spec=IObserver)
        self.system.error.add_observer(self.error_observer)

        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()

        CreateVariableOperation(
            variable_id=TEST_IMAGE_SOURCE_NAME,
            variable_value=load_test_image()
        ).run()

        CreateVariableOperation(
            variable_id=TEST_GRAY_IMAGE_VARIABLE_NAME,
        ).run()

        CreateOperationOperation(
            operation_id=TEST_OPERATION_NAME,
            operation_type=OperationType.CONVERT_IMAGE_TO_GRAY.value,
        ).run()

        SetOperationRelatedVariableOperation(
            operation_id=TEST_OPERATION_NAME,
            src_params_dict={
                SRC_VARIABLE: TEST_IMAGE_SOURCE_NAME,
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_GRAY_IMAGE_VARIABLE_NAME,
            }
        ).run()

        CreateVariableOperation(
            variable_id=TEST_SRC_VAIABLE_NAME,
        ).run()

        CreateVariableOperation(
            variable_id=TEST_RES_VARIABLE_NAME,
        ).run()

        CreateVariableOperation(
            variable_id=SRC_VARIABLE,
            variable_value=[SRC_VARIABLE]
        ).run()

        CreateVariableOperation(
            variable_id=NON_LIST_SRC_VARIABLE,
            variable_value=SRC_VARIABLE
        ).run()

        CreateVariableOperation(
            variable_id=TEST_NONE_VARIABLE,
        ).run()

        CreateVariableOperation(
            variable_id=TEST_NON_EXISTED_PARAM,
            variable_value=[TEST_NON_EXISTED_IMAGE_PATH],
        ).run()

        CreateVariableOperation(
            variable_id=TEST_OPERATION_NAME_VARIABLE,
            variable_value=TEST_OPERATION_NAME
        ).run()

        CreateVariableOperation(
            variable_id=TEST_RESULT_VARIABLE_NAME,
            variable_value=TEST_SRC_VAIABLE_NAME,
        ).run()

        CreateOperationOperation(
            operation_id=TEST_GET_SRC_PARAM,
            operation_type=OperationType.GET_PARAM_FROM_MULTI_OBSERVER.value,
        ).run()

    def test_get_param(self) -> None:
        SetOperationRelatedVariableOperation(
            operation_id=TEST_GET_SRC_PARAM,
            src_params_dict={
                SRC_OPERATION: TEST_OPERATION_NAME_VARIABLE,
                PARAM_VALUE: SRC_VARIABLE,
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_RESULT_VARIABLE_NAME,
            },
        ).run()

        self.assertListEqual(
            self.system.variables[TEST_SRC_VAIABLE_NAME].data[VALUE_KEY],
            [TEST_IMAGE_SOURCE_NAME],
        )

    def test_get_param_of_without_param_value(self):
        SetOperationRelatedVariableOperation(
            operation_id=TEST_GET_SRC_PARAM,
            src_params_dict={
                SRC_OPERATION: TEST_OPERATION_NAME_VARIABLE,
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_RESULT_VARIABLE_NAME,
            },
        ).run()

        self.assertListEqual(
            self.system.variables[TEST_SRC_VAIABLE_NAME].data[VALUE_KEY],
            [TEST_IMAGE_SOURCE_NAME],
        )

        self.assertEqual(
            self.error_observer.update.call_count,
            NOT_CALL_OBSERVER_COUNT
        )

    def test_get_param_with_list_src_variable(self):
        SetOperationRelatedVariableOperation(
            operation_id=TEST_GET_SRC_PARAM,
            src_params_dict={
                SRC_OPERATION: TEST_NON_EXISTED_PARAM,
                PARAM_VALUE: TEST_NON_EXISTED_PARAM
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_RESULT_VARIABLE_NAME,
            },
        ).run()

        self.assertGreaterEqual(
            self.error_observer.update.call_count,
            CALL_OBSERVER_COUNT
        )

    def test_get_param_with_non_src_operation(self):
        SetOperationRelatedVariableOperation(
            operation_id=TEST_GET_SRC_PARAM,
            src_params_dict={
                SRC_OPERATION: TEST_NONE_VARIABLE,
                PARAM_VALUE: TEST_NON_EXISTED_PARAM
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_RESULT_VARIABLE_NAME,
            },
        ).run()

        self.assertEqual(
            self.error_observer.update.call_count,
            NOT_CALL_OBSERVER_COUNT,
        )

    def test_get_param_with_non_list_param_varaible(self):
        SetOperationRelatedVariableOperation(
            operation_id=TEST_GET_SRC_PARAM,
            src_params_dict={
                SRC_OPERATION: TEST_OPERATION_NAME_VARIABLE,
                PARAM_VALUE: NON_LIST_SRC_VARIABLE
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_RESULT_VARIABLE_NAME,
            },
        ).run()

        self.assertEqual(
            self.system.variables[TEST_SRC_VAIABLE_NAME].data[VALUE_KEY],
            TEST_IMAGE_SOURCE_NAME,
        )
