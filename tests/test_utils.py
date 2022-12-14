import utils
import unittest
import numpy as np


class TestSplitWhen(unittest.TestCase):
    @staticmethod
    def test_ends_false():
        lst = [2, 7, 0, -3, 0, 5, -4, 7]
        guess = utils.split_when(lambda a: a == 0, lst)
        solution = [[2, 7], [-3], [5, -4, 7]]
        np.testing.assert_array_equal(solution, list(guess))

    @staticmethod
    def test_ends_true():
        lst = [2, 7, 0, -3, 0, 5, -4, 7, 0]
        guess = utils.split_when(lambda a: a == 0, lst)
        solution = [[2, 7], [-3], [5, -4, 7]]
        np.testing.assert_array_equal(solution, list(guess))


class TestSplitByCount(unittest.TestCase):
    def test_even(self):
        lst = [1, 2, 3, 4, 5, 6]
        guess = utils.split_by_count(2, lst)
        solution = [[1, 2], [3, 4], [5, 6]]
        np.testing.assert_array_equal(solution, list(guess))

    def test_odd(self):
        lst = [1, 2, 3, 4, 5]
        guess = utils.split_by_count(2, lst)
        solution = [[1, 2], [3, 4], [5]]
        np.testing.assert_array_equal(solution, list(guess))


if __name__ == '__main__':
    unittest.main()
