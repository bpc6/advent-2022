import re
import utils


def sequence_enclosed(s0_min: int, s0_max: int, s1_min: int, s1_max: int) -> bool:
    """If sequence 0 is completely enclosed by sequence 1"""
    return s0_min >= s1_min and s0_max <= s1_max


def either_enclosed(s0_min: int, s0_max: int, s1_min: int, s1_max: int) -> bool:
    return sequence_enclosed(s0_min, s0_max, s1_min, s1_max) or sequence_enclosed(s1_min, s1_max, s0_min, s0_max)


def parse_input(s: str):
    return map(int, re.split('[,-]', s))


if __name__ == '__main__':
    filename = 'input.txt'
    line_enclosed = utils.chain_args([parse_input, either_enclosed])
    solution1 = sum(map(line_enclosed, utils.input_gen(filename)))
    print('solution1:', solution1)
