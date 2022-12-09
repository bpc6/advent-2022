from functools import partial
from typing import Generator

import utils


def get_input(filename: str) -> Generator[str, None, None]:
    with open(filename, 'r') as f:
        for line in f:
            yield line


if __name__ == '__main__':
    filename = 'input.txt'
    stripped_strings = map(lambda s: s.strip('\n'), get_input(filename))
    list_list_strs = utils.split_when(lambda s: s == '', stripped_strings)

    fcns = [lambda list_strs: map(int, list_strs), sum]
    chained_fcn = partial(utils.chain, fcns)
    in_order = sorted(map(chained_fcn, list_list_strs))
    print('solution 1:', in_order[-1])
    print('solution 2:', sum(in_order[-3:]))
