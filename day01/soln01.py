from functools import partial
from typing import List, Callable

import utils


def get_input(filename: str) -> str:
    with open(filename, 'r') as f:
        as_str = f.read()
    return as_str


def puzzle1(input_str: str) -> List[List[int]]:
    list_list_strs = utils.split_when(lambda s: s == '', input_str.split('\n'))
    # list_list_ints = map(lambda list_strs: map(int, list_strs), list_list_strs)
    # list_sums = map(sum, list_list_ints)

    fcns = [lambda list_strs: map(int, list_strs), sum]
    chained_fcn = partial(utils.chain, fcns)
    return max(map(chained_fcn, list_list_strs))


if __name__ == '__main__':
    print(puzzle1(get_input('test.txt')))
