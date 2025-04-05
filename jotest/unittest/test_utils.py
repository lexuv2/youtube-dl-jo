import unittest

import datetime

from youtube_dl.utils import date_from_str, hyphenate_date, base_url

class TestUtils(unittest.TestCase):
    def test_date_from_str_yyyymmdd(self):
        self.assertEqual(date_from_str("20050125"), datetime.date(2005, 1, 25))
        self.assertEqual(date_from_str("20050122"), datetime.date(2005, 1, 22))
        self.assertRaises(ValueError, lambda: date_from_str("20050133"))

    def test_hyphenate_date(self):
        self.assertEqual(hyphenate_date("20050125"), '2005-01-25')
        self.assertEqual(hyphenate_date("20050121"), '2005-01-21')

    def test_base_url(self):
        self.assertEqual(base_url("https://docs.python.org/3/library/unittest.html"), 'https://docs.python.org/3/library/')
        self.assertEqual(base_url("https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory"), 'https://stackoverflow.com/questions/1732438/')
