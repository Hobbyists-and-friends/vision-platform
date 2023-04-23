import unittest
from unittest.mock import (
    Mock,
    PropertyMock,
)

from src.interfaces import (
    ISystem,
    IVariable,
)
from src.constants import (
    VALUE_KEY,
    VariableType,
)
from src.operations.trigger import (
    CompareVariable,
)
from src.cores import (
    System,
)
from src.operations.system_call import (
    CreateVariableOperation,
)

from tests.tools import (
    load_test_image,
)
from tests.constants import (
    TEST_CREATE_VARIABLE_OPERATION_NAME,
    TEST_IMAGE_VARIABLE_NAME,
    TEST_VARIABLE_SECOND_VALUE,
    TEST_SECOND_OPERATION_NAME,
    TEST_TRIGGER_ID,
)

from tests.constants import (
    TEST_OPERATION_NAME,
    TEST_VARIABLE_NAME,
    TEST_VARIABLE_VALUE,
    TEST_TRIGGER_ID_FALSE,
    TEST_TRIGGER_ID_TRUE,
    TEST_SMALL_VARIABLE_NAME,
    TEST_BIG_VARIABLE_NAME,
)


class CreateVariableTest(unittest.TestCase):
    def setUp(self):
        self.system = System()

        CreateVariableOperation(
            variable_id=TEST_SMALL_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE,
        ).run()
        CreateVariableOperation(
            variable_id=TEST_BIG_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE + 1,
        ).run()

        self.system.triggers[TEST_TRIGGER_ID_TRUE] = CompareVariable(
            trigger_id=TEST_TRIGGER_ID_TRUE,
            small_variable_id=TEST_SMALL_VARIABLE_NAME,
            big_variable_id=TEST_BIG_VARIABLE_NAME,
        )

        self.system.triggers[TEST_TRIGGER_ID_FALSE] = CompareVariable(
            trigger_id=TEST_TRIGGER_ID_FALSE,
            small_variable_id=TEST_BIG_VARIABLE_NAME,
            big_variable_id=TEST_SMALL_VARIABLE_NAME,
        )

    def test_create_variable(self):
        operation = CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE)

        operation.run()

        self.assertEqual(
            self.system.variables[TEST_VARIABLE_NAME].data[VALUE_KEY],
            TEST_VARIABLE_VALUE,
        )

    def test_create_image_variable(self):
        image = load_test_image()
        operation = CreateVariableOperation(
            variable_id=TEST_IMAGE_VARIABLE_NAME,
            variable_value=image,
        )

        operation.run()

        self.assertEqual(
            self.system.variables[TEST_IMAGE_VARIABLE_NAME].type, VariableType.IMAGE)
        self.assertAlmostEqual(
            self.system.variables[TEST_IMAGE_VARIABLE_NAME].data[VALUE_KEY].all(
            ),
            image.all()
        )

    def test_create_variable_with_existed_name(self):
        CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_VALUE).run()

        operation = CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            variable_value=TEST_VARIABLE_SECOND_VALUE,
        )

        operation.run()

        self.assertEqual(
            self.system.variables[TEST_VARIABLE_NAME].data[VALUE_KEY], TEST_VARIABLE_VALUE)

    def test_crate_variable_with_trigger(self):
        operation = CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            trigger_id=TEST_TRIGGER_ID_TRUE,
            variable_value=TEST_VARIABLE_VALUE,
        )

        operation.run()

        self.assertTrue(
            TEST_VARIABLE_NAME in self.system.variables,
        )

    def test_create_variable_with_trigger_false(self):
        operation = CreateVariableOperation(
            variable_id=TEST_VARIABLE_NAME,
            trigger_id=TEST_TRIGGER_ID_FALSE,
            variable_value=TEST_VARIABLE_VALUE,
        )

        operation.run()

        self.assertTrue(
            TEST_VARIABLE_NAME not in self.system.variables,
        )
