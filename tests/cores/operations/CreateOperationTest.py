import unittest
from unittest.mock import Mock


from src.interfaces import (
    ISystem,
)


TEST_OPERATION_NAME = 'test_operation_name'


class CreateOperationTest(unittest.TestCase):
    @unittest.skip('Not implemented')
    def test_create_operation(self):
        system = Mock(spec=ISystem)
        create_operation_operation = CreateOperationOperation(
            system, TEST_OPERATION_NAME,
            args=[], kwargs={})

        system.run_operation(create_operation_operation)

        self.assertEqual(
            self.system.operations[TEST_OPERATION_NAME].data[VALUE_KEY], TEST_OPERATION_VALUE)
