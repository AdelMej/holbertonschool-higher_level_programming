#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test suite for max_integer

    """
    def test_max_integer(self):
        self.assertEqual(max_integer([1, 10, 334]), 334)

    def test_max_integer_negative(self):
        self.assertEqual(max_integer([-1, -46, -2]), -1)

    def test_max_integer_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_max_integer_single_elem(self):
        self.assertEqual(max_integer([4]), 4)

    def test_max_integer_float(self):
        self.assertEqual(max_integer([1, 1.2, 2.3]), 2.3)


if __name__ == '__main__':
    unittest.main()
