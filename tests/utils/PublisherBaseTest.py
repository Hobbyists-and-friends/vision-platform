import unittest
from unittest.mock import Mock

from src.interfaces import IObserver
from src.utils import PublisherBase


TEST_KEY = 'key'
TEST_VALUE = 'value'


class PublisherBaseTest(unittest.TestCase):
    def setUp(self):
        self.publisher = PublisherBase()
        self.publiser_with_initial_dict = PublisherBase(**{
            TEST_KEY: TEST_VALUE
        })
        self.first_observer = Mock(spec=IObserver)
        self.second_observer = Mock(spec=IObserver)
        self.third_observer = Mock(spec=IObserver)

    def test_publisher_base_adds_observer(self):
        publisher = PublisherBase()
        publisher.add_observer(self.first_observer)

        publisher.notify()

        self.first_observer.update.assert_called_with(publisher, {})
        self.assertEqual(
            self.first_observer.update.call_count,
            2
        )

    def test_publisher_with_initial_dict(self):
        self.publiser_with_initial_dict.add_observer(self.first_observer)

        self.publiser_with_initial_dict.notify()

        self.first_observer.update.assert_called_with(
            self.publiser_with_initial_dict,
            {TEST_KEY: TEST_VALUE}
        )
        self.assertEqual(
            self.first_observer.update.call_count,
            2
        )

    def test_publisher_base_adds_two_observers(self):
        self.publisher.add_observer(self.first_observer)
        self.publisher.add_observer(self.second_observer)

        self.publisher.notify()

        self.first_observer.update.assert_called_with(
            self.publisher,
            {}
        )
        self.assertEqual(self.first_observer.update.call_count, 2)
        self.second_observer.update.assert_called_with(
            self.publisher,
            {}
        )
        self.assertEqual(self.second_observer.update.call_count, 2)

    def test_publisher_base_removes_observer(self):
        self.publisher.add_observer(self.first_observer)
        self.publisher.add_observer(self.second_observer)
        self.publisher.remove_observer(self.second_observer)

        self.publisher.notify()

        self.assertEqual(self.first_observer.update.call_count, 2)
        self.assertEqual(self.second_observer.update.call_count, 1)

    def test_publisher_base_adds_existed_observer(self):
        self.publisher.add_observer(self.first_observer)
        self.publisher.add_observer(self.first_observer)

        self.publisher.notify()

        self.first_observer.update.assert_called_with(
            self.publisher,
            {}
        )

    def test_publisher_base_removes_not_existed_observer(self):
        self.publisher.add_observer(self.first_observer)
        self.publisher.remove_observer(self.second_observer)

        self.publisher.notify()

        self.first_observer.update.assert_called_with(
            self.publisher,
            {}
        )
        self.second_observer.update.assert_not_called()
