import unittest
from unittest.mock import (
    Mock,
)

from src.interfaces import (
    IObserver,
)
from src.cores import System
from src.constants import *
from src.operations.system_call import *
from tests.constants import *
from tests.tools import *


TRANSFORM_VARIABLE_TO_IMAGE_OPERATION = "Transform Variable To Image Operation"


class TransformVariableToValueTest(unittest.TestCase):
    def setUp(self) -> None:
        self.system = System()
        self.error_observer = Mock(spec=IObserver)
        self.variable_observer = Mock(spec=IObserver)
        self.system.error.add_observer(self.error_observer)

        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_IMAGE_VARIABLE_NAME,
        ).run()

        CreateVariableOperation(
            variable_id=TEST_NONE_VARIABLE,
        ).run()

        CreateVariableOperation(
            variable_id=TEST_IMAGE_VARIABLE_NAME,
            variable_value=load_test_image()
        ).run()

        CreateVariableOperation(
            variable_id=TEST_BIG_VARIABLE_NAME,
        ).run()

    def test_convert_name_variable_to_image(self):
        CreateOperationOperation(
            operation_id=TRANSFORM_VARIABLE_TO_IMAGE_OPERATION,
            operation_type=OperationType.TRANSFORM_VARIABLE_TO_VALUE.value,
        ).run()

        SetOperationRelatedVariableOperation(
            operation_id=TRANSFORM_VARIABLE_TO_IMAGE_OPERATION,
            src_params_dict={
                SRC_VARIABLE: TEST_VARIABLE_NAME,
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_BIG_VARIABLE_NAME,
            },
        ).run()

        self.assertEqual(
            self.system.variables[TEST_BIG_VARIABLE_NAME].type,
            VariableType.IMAGE
        )

    def test_convert_non_exist_src_image_variable_to_image(self):
        CreateOperationOperation(
            operation_id=TRANSFORM_VARIABLE_TO_IMAGE_OPERATION,
            operation_type=OperationType.TRANSFORM_VARIABLE_TO_VALUE.value,
        ).run()

        SetOperationRelatedVariableOperation(
            operation_id=TRANSFORM_VARIABLE_TO_IMAGE_OPERATION,
            src_params_dict={
                SRC_VARIABLE: TEST_NON_EXISTED_VARIABLE_NAME,
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_BIG_VARIABLE_NAME,
            },
        ).run()

        self.assertEqual(
            self.error_observer.update.call_count,
            CALL_OBSERVER_COUNT,
        )

    def test_convert_with_none_src_variable(self):
        CreateOperationOperation(
            operation_id=TRANSFORM_VARIABLE_TO_IMAGE_OPERATION,
            operation_type=OperationType.TRANSFORM_VARIABLE_TO_VALUE.value,
        ).run()

        SetOperationRelatedVariableOperation(
            operation_id=TRANSFORM_VARIABLE_TO_IMAGE_OPERATION,
            src_params_dict={
                SRC_VARIABLE: TEST_NONE_VARIABLE,
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_BIG_VARIABLE_NAME,
            },
        ).run()

        self.assertGreaterEqual(
            self.error_observer.update.call_count,
            NOT_CALL_OBSERVER_COUNT,
        )

    def test_convert_when_variable_is_updated(self):
        CreateOperationOperation(
            operation_id=TRANSFORM_VARIABLE_TO_IMAGE_OPERATION,
            operation_type=OperationType.TRANSFORM_VARIABLE_TO_VALUE.value,
        ).run()

        SetOperationRelatedVariableOperation(
            operation_id=TRANSFORM_VARIABLE_TO_IMAGE_OPERATION,
            src_params_dict={
                SRC_VARIABLE: TEST_VARIABLE_NAME,
            },
            res_params_dict={
                RESULT_VARIABLE: TEST_BIG_VARIABLE_NAME,
            },
        ).run()

        ChangeVariableValueOperation(
            variable_id=TEST_VARIABLE_NAME,
            new_value=load_test_image(),
        ).run()
