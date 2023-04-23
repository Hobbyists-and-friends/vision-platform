import unittest
from unittest.mock import Mock

from src.interfaces import (
    IObserver,
    ISystem,
)
from src.constants import (
    VALUE_KEY,
    NAME_KEY,
    EMPTY_STRING,
    VariableType,
)
from src.cores import Variable
from src.utils import PublisherBase


TEST_NUMBER_NAME = 'threshold'
TEST_NUMBER_VALUE = 0.34
TEST_NUMBER_VALUE_CHANGED_VALUE = 23.4

TEST_STRING_NAME = 'notification string'
TEST_STRING_VALUE = 'test'

TEST_NULL_NAME = 'null variable'


class VariableTest(unittest.TestCase):
    def setUp(self):
        self.system = Mock(spec=ISystem)

        self.number_variable = Variable(
            system=self.system,
            **{
                NAME_KEY: TEST_NUMBER_NAME,
                VALUE_KEY: TEST_NUMBER_VALUE,
            }
        )

        self.string_variable = Variable(
            system=self.system,
            **{
                NAME_KEY: TEST_STRING_NAME,
                VALUE_KEY: TEST_STRING_VALUE
            }
        )

        self.null_variable = Variable(
            system=self.system,
            **{
                NAME_KEY: TEST_NULL_NAME,
            }
        )

        self.no_name_variable = Variable(system=self.system,
                                         **{
                                             VALUE_KEY: TEST_NUMBER_VALUE
                                         }
                                         )

        self.first_test_observer = Mock(spec=IObserver)
        self.second_test_observer = Mock(spec=IObserver)

    def test_get_name_of_the_variable(self):
        self.assertEqual(self.number_variable.variable_id, TEST_NUMBER_NAME)
        self.assertEqual(self.string_variable.variable_id, TEST_STRING_NAME)

    def test_create_variable_without_name(self):
        self.assertEqual(self.no_name_variable.variable_id, EMPTY_STRING)

    def test_create_variable_without_value(self):
        self.assertEqual(self.null_variable.data[VALUE_KEY], None)
        self.assertEqual(self.null_variable.type, VariableType.NULL)

    def test_create_number_variable(self):
        self.assertEqual(self.number_variable.type, VariableType.NUMBER)
        self.assertEqual(
            self.number_variable.data[VALUE_KEY], TEST_NUMBER_VALUE)

    def test_create_string_variable(self):
        self.assertEqual(self.string_variable.type, VariableType.STRING)
        self.assertEqual(
            self.string_variable.data[VALUE_KEY], TEST_STRING_VALUE)

    def test_the_variable_is_subclass_of_PublisherBase(self):
        self.assertTrue(isinstance(self.string_variable, PublisherBase))

    def test_change_value_of_the_variable(self):
        self.number_variable.change_value(**{
            VALUE_KEY: TEST_NUMBER_VALUE_CHANGED_VALUE
        })

        self.assertEqual(self.number_variable.data[VALUE_KEY],
                         TEST_NUMBER_VALUE_CHANGED_VALUE)

    def test_when_the_value_has_been_modified_then_notify(self):
        self.number_variable.add_observer(self.first_test_observer)
        self.number_variable.change_value(**{
            VALUE_KEY: TEST_NUMBER_VALUE_CHANGED_VALUE
        })

        self.assertEqual(self.number_variable.data[VALUE_KEY],
                         TEST_NUMBER_VALUE_CHANGED_VALUE)

        self.first_test_observer.update.assert_called()
        self.assertEqual(self.first_test_observer.update.call_count, 2)
        self.second_test_observer.update.assert_not_called()

    def test_when_the_value_has_been_modified_with_wrong_type(self):
        self.number_variable.add_observer(self.first_test_observer)
        self.number_variable.change_value(**{
            VALUE_KEY: TEST_STRING_VALUE
        })

        self.assertEqual(self.number_variable.data[VALUE_KEY],
                         TEST_NUMBER_VALUE)
        self.first_test_observer.update.assert_called_once()

    def test_when_change_value_of_the_null_variable(self):
        self.null_variable.change_value(**{
            VALUE_KEY: TEST_NUMBER_VALUE
        })

        self.assertEqual(self.null_variable.data[VALUE_KEY],
                         TEST_NUMBER_VALUE)
        self.assertEqual(self.null_variable.type, VariableType.NUMBER)

    def test_when_change_value_without_value_key(self):
        self.number_variable.change_value(**{
        })

        self.assertEqual(self.number_variable.data[VALUE_KEY],
                         TEST_NUMBER_VALUE)
