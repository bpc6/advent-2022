from typing import List
import utils


def parse_line(s: str, curr_stacks: List[List[str]]) -> List[List[str]]:
    match first_nonspace(s):
        case '[':
            build_stacks(s, curr_stacks)
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


if __name__ == '__main__':
    filename = 'test.txt'
    stacks = [[]]
    for line in utils.input_gen(filename):
        stacks = parse_line(line, stacks)

    final = ''
    for stack in stacks:
        final += stack.pop()
    print(final)
