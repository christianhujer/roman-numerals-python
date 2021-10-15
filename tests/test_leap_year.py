import unittest


class LeapYearTest(unittest.TestCase):
    def test_regularYear(self):
        self.assertFalse(is_leap_year(1999))
