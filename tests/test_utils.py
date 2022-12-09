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


class TestSplitWhen2(unittest.TestCase):
    def test_ends_false(self):
        lst = [2, 7, 0, -3, 0, 5, -4, 7]
        guess = utils.split_when2(lambda a: a == 0, iter(lst))
        solution = [[2, 7], [-3], [5, -4, 7]]

        for inner_guess, inner_soln in zip(guess, solution):
            self.assertEqual(inner_soln, list(inner_guess))
        # self.assertEqual(solution, utils.recursive_list(guess))

    def test_ends_true(self):
        lst = [2, 7, 0, -3, 0, 5, -4, 7, 0]
        guess = list(utils.split_when2(lambda a: a == 0, iter(lst)))
        solution = [[2, 7], [-3], [5, -4, 7]]
        self.assertEqual(solution, utils.recursive_list(guess))


if __name__ == '__main__':
    unittest.main()
