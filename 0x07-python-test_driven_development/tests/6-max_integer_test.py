#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class MaxIntegerTest(unittest.TestCase):
    def test_module_docstring(self):
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_max_at_end(self):
        l = [12, 1, 18, 6, 14, 40]
        self.assertEqual(max_integer(l), 40)

    def test_function_docstring(self):
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_no_args(self):
        self.assertIsNone(max_integer())

    def test_empty_list(self):
        l = []
        self.assertIsNone(max_integer(l))

    def test_two_of_max(self):
        l = [12, 1, 40, 6, 14, 40]
        self.assertEqual(max_integer(l), 40)

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_max_at_beginning(self):
        l = [130, 129, 23, 6, 0, 10]
        self.assertEqual(max_integer(l), 130)

    def test_non_int_arg(self):
        l = [1, "string", 3, 4, 5]
        with self.assertRaises(TypeError):
            max_integer(l)

    def test_all_negative(self):
        l = [-1, -2, -3, -4, -5]
        self.assertEqual(max_integer(l), -1)

    def test_one_element(self):
        l = [10]
        self.assertEqual(max_integer(l), 10)

    def test_max_at_middle(self):
        l = [1, 10, 23, 30, 14, 12]
        self.assertEqual(max_integer(l), 30)

    def test_one_negative(self):
        l = [10, -10, 1, 6, 4, 2]
        self.assertEqual(max_integer(l), 10)

    def test_all_10(self):
        l = [10, 10, 10, 10, 10, 10]
        self.assertEqual(max_integer(l), 10)

if __name__ == "__main__":
    unittest.main()
