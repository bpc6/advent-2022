import utils


def score2(s: str) -> int:
    them, outcome = map(read_selection, s.split())
    me = get_outcome(them, outcome)
    return total_score(them, me)


def total_score(them: int, me: int) -> int:
    participation = me + 1
    win_bonus = 3 * win(them, me)
    return participation + win_bonus


def read_selection(s: str) -> int:
    """Convert your string selection to int:
    Rock -> 0, Paper -> 1, Scissors -> 2"""
    match s:
        case 'A' | 'X': return 0
        case 'B' | 'Y': return 1
        case 'C' | 'Z': return 2


def win(them: int, me: int) -> int:
    """Return 0 for loss, 1 for tie, 2 for win"""
    # result is 0 for tie, 1 for loss, 2 for win
    result = (them - me) % 3
    match result:
        case 0: return 1
        case 1: return 0
        case 2: return 2


def get_outcome(them: int, outcome: int) -> int:
    """Inverse of win. Determine what I should throw to get the outcome"""
    match outcome:
        case 1: return them
        case 2: return (them + 1) % 3
        case 0: return (them - 1) % 3


if __name__ == '__main__':
    filename = 'input.txt'

    fcns1 = [lambda s: map(read_selection, s.split()), total_score]
    all_fcns = [fcns1, [score2]]
    solutions = map(lambda f: sum(map(utils.chain_args(f), utils.input_gen(filename))), all_fcns)
    print(list(solutions))
