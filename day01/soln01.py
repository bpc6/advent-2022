from functools import partial
from typing import Generator

import utils


def get_input(filename: str) -> Generator[str, None, None]:
    with open(filename, 'r') as f:
        for line in f:
            yield line


def puzzle1(filename: str) -> int:
    stripped_strings = map(lambda s: s.strip('\n'), get_input(filename))
    list_list_strs = utils.split_when(lambda s: s == '', stripped_strings)

    # # loops 3 times
    # list_list_ints = map(lambda list_strs: map(int, list_strs), list_list_strs)
    # list_sums = map(sum, list_list_ints)
    # return max(list_sums)

    # loops 1 time
    fcns = [lambda list_strs: map(int, list_strs), sum]
    chained_fcn = partial(utils.chain, fcns)
    return max(map(chained_fcn, list_list_strs))  # since map is lazy


if __name__ == '__main__':
    print(puzzle1('input.txt'))
