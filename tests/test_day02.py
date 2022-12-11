import unittest

from day02.solution import score1, win, selection1, get_outcome


class TestScore(unittest.TestCase):
    def test_score(self):
        self.assertEqual(8, score1('A Y'))

    def test_win(self):
        self.assertEqual(0, win(0, 1))
        self.assertEqual(2, win(2, 1))
        self.assertEqual(1, win(2, 2))

    def test_selection(self):
        self.assertEqual(1, selection1('B'))

    def test_get_outcome(self):
        self.assertEqual(2, get_outcome(1, 2))
        self.assertEqual(2, get_outcome(2, 1))
        self.assertEqual(2, get_outcome(0, 0))


if __name__ == '__main__':
    unittest.main()
