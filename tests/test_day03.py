import unittest

from day03.solution03 import priority_of_char, find_repeat_in_list


class TestDay03(unittest.TestCase):
    def test_priority_of_char(self):
        self.assertEqual(1, priority_of_char('a'))
        self.assertEqual(16, priority_of_char('p'))
        self.assertEqual(38, priority_of_char('L'))
        self.assertEqual(42, priority_of_char('P'))

    def test_find_repeat(self):
        self.assertEqual('P', find_repeat_in_list(['PmmdzqPrV', 'vPwwTWBwg']))
        strs = [
            'vJrwpWtwJgWrhcsFMMfFFhFp',
            'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
            'PmmdzqPrVvPwwTWBwg'
        ]

        def gen(strings: list):
            for s in strings:
                yield s

        self.assertEqual('r', find_repeat_in_list(gen(strs)))


if __name__ == '__main__':
    unittest.main()
