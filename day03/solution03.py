import functools
from typing import List, Iterable
import utils


def split_string_in_half(s: str) -> List[str]:
    return [s[:len(s)//2], s[len(s)//2:]]


def find_repeat_in_list(strs: Iterable[str]) -> str:
    """Find the character that is repeated in each string in the list.
    Example
    -------
    >>> find_repeat_in_list(['cat', 'rat', 'car'])
    'a'
    """
    def find_repeats_in_2_strings(s0: str, s1: str, repeats: str = '') -> str:
        if s0 == '':
            return repeats
        c = s0[0]
        if c in s1 and c not in repeats:
            new_repeats = repeats + c
        else:
            new_repeats = repeats
        return find_repeats_in_2_strings(s0[1:], s1, new_repeats)

    return functools.reduce(find_repeats_in_2_strings, strs)


def priority_of_char(c: str) -> int:
    if c.islower():
        return ord(c) - 96
    return ord(c) - 64 + 26


if __name__ == '__main__':
    filename = 'input.txt'

    fcns = [split_string_in_half, find_repeat_in_list, priority_of_char]
    priority_of_line_fcn1 = utils.chain(fcns)
    solution1 = sum(map(priority_of_line_fcn1, utils.input_gen(filename)))
    print('solution 1:', solution1)

    str_groups = utils.split_by_count(3, utils.input_gen(filename))
    fcns2 = [
        find_repeat_in_list,
        priority_of_char
    ]
    priority_of_line_fcn2 = utils.chain(fcns2)
    solution2 = sum(map(priority_of_line_fcn2, str_groups))
    print('solution 2:', solution2)
