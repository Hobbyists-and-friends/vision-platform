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
from src.cores import (
    System,
)
from src.operations import (
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
)

from tests.constants import (
    TEST_OPERATION_NAME,
    TEST_VARIABLE_NAME,
    TEST_VARIABLE_VALUE,
)

from tests.tools import (
    create_mocked_system,
    create_mocked_int_variable,
    add_vars_system,
    add_no_vars_system,
)


class CreateVariableTest(unittest.TestCase):
    def setUp(self):
        self.system = System()

    def test_create_variable(self):
        operation = CreateVariableOperation(
            self.system, TEST_OPERATION_NAME, TEST_VARIABLE_NAME, TEST_VARIABLE_VALUE)

        operation.run()

        self.assertEqual(
            self.system.variables[TEST_VARIABLE_NAME].data[VALUE_KEY],
            TEST_VARIABLE_VALUE,
        )

    def test_create_image_variable(self):
        image = load_test_image()
        operation = CreateVariableOperation(
            self.system,
            TEST_CREATE_VARIABLE_OPERATION_NAME,
            TEST_IMAGE_VARIABLE_NAME,
            image,
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
            self.system, TEST_OPERATION_NAME, TEST_VARIABLE_NAME, TEST_VARIABLE_VALUE).run()

        operation = CreateVariableOperation(
            self.system,
            TEST_SECOND_OPERATION_NAME,
            TEST_VARIABLE_NAME,
            TEST_VARIABLE_SECOND_VALUE,
        )

        operation.run()

        self.assertEqual(
            self.system.variables[TEST_VARIABLE_NAME].data[VALUE_KEY], TEST_VARIABLE_VALUE)
