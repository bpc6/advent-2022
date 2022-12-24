import functools
from typing import List
import utils


def move_blocks_1_at_time(
    num_to_move: int,
    from_col: int,
    to_col: int,
    curr_stacks: List[List[str]]
) -> List[List[str]]:
    for _ in range(num_to_move):
        curr_stacks[to_col].append(curr_stacks[from_col].pop())
    return curr_stacks


def move_blocks_at_once(
    num_to_move: int,
    from_col: int,
    to_col: int,
    curr_stacks: List[List[str]]
) -> List[List[str]]:
    curr_stacks[to_col] += curr_stacks[from_col][-num_to_move:]
    curr_stacks[from_col] = curr_stacks[from_col][:-num_to_move]
    return curr_stacks


def build_stacks(s: str, curr_stacks: List[List[str]]) -> List[List[str]]:
    for idx, c in enumerate(s):
        if c.isalpha():
            stack_idx = int(idx / 4)
            for _ in range(stack_idx - len(curr_stacks) + 1):
                curr_stacks.append([])
            curr_stacks[stack_idx].insert(0, c)
    return curr_stacks


def first_nonspace(s: str) -> str:
    for c in s:
        if not c.isspace():
            return c
    return ''


def build_and_sort(stacks, input_lines, sorting_fcn):
    for line in input_lines:
        match first_nonspace(line):
            case '[':
                build_stacks(line, stacks)
            case 'm':
                utils.chain_args(
                    [
                        utils.parse_ints,
                        lambda a, b, c: (a, b - 1, c - 1),
                        functools.partial(sorting_fcn, curr_stacks=stacks)
                    ]
                )(line)
    return stacks


if __name__ == '__main__':
    filename = 'input.txt'
    stacks = build_and_sort([[]], utils.input_gen(filename), move_blocks_1_at_time)
    print(functools.reduce(lambda a, b: a + b.pop(), stacks, ''))

    # puzzle 2
    stacks2 = build_and_sort([[]], utils.input_gen(filename), move_blocks_at_once)
    print(functools.reduce(lambda a, b: a + b.pop(), stacks2, ''))

