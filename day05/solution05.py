import functools
from typing import List, Tuple
from itertools import zip_longest

import utils
from stack import Stack


def move_blocks_1_at_time(
    num_to_move: int,
    from_col: int,
    to_col: int,
    curr_stacks: Tuple[Tuple[str]]
) -> Tuple[Tuple[str]]:
    if num_to_move == 0:
        return curr_stacks

    popped, from_stack = Stack[str].pop(curr_stacks[from_col])
    to_stack = Stack[str].push(popped, curr_stacks[to_col])

    def place_stack(idx: int) -> Tuple[str]:
        if idx == from_col:
            return from_stack
        elif idx == to_col:
            return to_stack
        else:
            return curr_stacks[idx]

    return move_blocks_1_at_time(
        num_to_move - 1, from_col, to_col, tuple(map(place_stack, range(len(curr_stacks))))
    )


def move_blocks_at_once(
    num_to_move: int,
    from_col: int,
    to_col: int,
    curr_stacks: Tuple[Tuple[str]]
) -> Tuple[Tuple[str]]:
    popped = curr_stacks[from_col][-num_to_move:]
    from_stack = curr_stacks[from_col][:-num_to_move]
    to_stack = curr_stacks[to_col] + popped

    def place_stack(idx: int) -> Tuple[str]:
        if idx == from_col:
            return from_stack
        elif idx == to_col:
            return to_stack
        else:
            return curr_stacks[idx]

    return tuple(map(place_stack, range(len(curr_stacks))))


def build_stacks(s: str, curr_stacks):
    def condense(list_list_chars):
        """Takes a list of lists of chars. Each list of char will have 0 or 1
        alpha chars. Extract the alpha char to a tuple of length 0 or 1."""
        def alpha_or_empty(ch: str) -> str:
            return ch if ch.isalpha() else ''
        return map(lambda strs: tuple(functools.reduce(lambda a, b: a + alpha_or_empty(b), strs, '')), list_list_chars)

    next_push = utils.chain(
        [functools.partial(utils.split_by_count, 4), condense]
    )
    return (n + c for n, c in zip_longest(next_push(s), curr_stacks, fillvalue=()))


def first_nonspace(s: str) -> str:
    for c in s:
        if not c.isspace():
            return c
    return ''


def build_and_sort(stacks, input_lines, sorting_fcn):
    try:
        line = input_lines.__next__()
    except StopIteration:
        return stacks

    match first_nonspace(line):
        case '[':
            new_stacks = build_stacks(line, stacks)
        case 'm':
            new_stacks = utils.chain_args(
                [
                    utils.parse_ints,
                    lambda a, b, c: (a, b - 1, c - 1),
                    functools.partial(sorting_fcn, curr_stacks=tuple(stacks))
                ]
            )(line)
        case _:
            new_stacks = stacks
    return build_and_sort(new_stacks, input_lines, sorting_fcn)


if __name__ == '__main__':
    filename = 'input.txt'
    stacks = build_and_sort(tuple(), utils.input_gen(filename), move_blocks_1_at_time)
    print(functools.reduce(lambda a, b: a + Stack[str].pop(b)[0], stacks, ''))

    # puzzle 2
    stacks2 = build_and_sort(tuple(), utils.input_gen(filename), move_blocks_at_once)
    print(functools.reduce(lambda a, b: a + Stack[str].pop(b)[0], stacks2, ''))

