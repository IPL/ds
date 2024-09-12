import datetime
import unittest
from freezegun import freeze_time

from src.my_greeter import MyGreeter


class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._my_greeter = MyGreeter()

    def test_init(self):
        self.assertIsInstance(self._my_greeter, MyGreeter)

    def test_greeting(self):
        self.assertTrue(len(self._my_greeter.greeting())>0)

    def test_greeting_morning(self):
        test_now = datetime.datetime(2024, 9, 12, 8, 0, 0)
        self.assertTrue(self._my_greeter.greeting(test_now) == "Good morning")

    def test_greeting_afternoon(self):
        test_now = datetime.datetime(2024, 9, 12, 13, 0, 0)
        self.assertTrue(self._my_greeter.greeting(test_now) == "Good afternoon")

    def test_greeting_evening(self):
        test_now = datetime.datetime(2024, 9, 12, 19, 0, 0)
        self.assertTrue(self._my_greeter.greeting(test_now) == "Good evening")

    @freeze_time("2024-09-12 08:00:00")
    def test_mock_greeting_morning(self):
        mock_now = datetime.datetime.now()
        self.assertTrue(self._my_greeter.greeting() == "Good morning")

    @freeze_time("2024-09-12 13:00:00")
    def test_mock_greeting_afternoon(self):
        mock_now = datetime.datetime.now()
        self.assertTrue(self._my_greeter.greeting() == "Good afternoon")

    @freeze_time("2024-09-12 19:00:00")
    def test_mock_greeting_evening(self):
        mock_now = datetime.datetime.now()
        self.assertTrue(self._my_greeter.greeting() == "Good evening")

if __name__ == '__main__':
    unittest.main()
