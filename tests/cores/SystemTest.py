import unittest
from unittest.mock import Mock

from src.cores import System
from src.utils import PublisherBase
from src.constants import (
    VALUE_KEY,
    EMPTY_STRING,
)


class SystemTest(unittest.TestCase):
    def setUp(self):
        self.system = System()

    def test_system_has_no_error_at_the_beginning(self):
        self.assertEqual(self.system.error.data[VALUE_KEY], EMPTY_STRING)

    def test_system_has_no_variables_at_the_beginning(self):
        self.assertEqual(len(self.system.variables.keys()), 0)

    def test_system_is_subclass_of_publisher_base(self):
        self.assertTrue(isinstance(self.system, PublisherBase))
