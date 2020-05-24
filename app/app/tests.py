from django.test import TestCase

from app.calc import add,subtract

# flake8: noqa

class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers are added togehter"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """test that values are subtracted and returned"""
        self.assertEqual(subtract(5, 11), 6)
