import functools
from typing import Tuple
import utils


def split_string_in_half(s: str) -> Tuple[str, str]:
    return s[:len(s)//2], s[len(s)//2:]


def find_repeat(s0: str, s1: str) -> str:
    for c in s1:
        if c in s0:
            return c
    return ''


def priority_of_char(c: str) -> int:
    if c.islower():
        return ord(c) - 96
    return ord(c) - 64 + 26


if __name__ == '__main__':
    filename = 'test.txt'

    fcns = [split_string_in_half, find_repeat, priority_of_char]
    priority_of_line_fcn = functools.partial(utils.chain_and_call, fcns)
    solution1 = sum(map(priority_of_line_fcn, utils.input_gen(filename)))
    print('solution 1:', solution1)
