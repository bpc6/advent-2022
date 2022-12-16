import utils


def score2(s: str) -> int:
    them, outcome = map(selection1, s.split())
    me = get_outcome(outcome, them)
    return total_score(them, me)


def total_score(them: int, me: int) -> int:
    participation = me + 1
    win_bonus = 3 * win(me, them)
    return participation + win_bonus


def selection1(s: str) -> int:
    """Convert your string selection to int:
    Rock -> 0, Paper -> 1, Scissors -> 2"""
    match s:
        case 'A' | 'X': return 0
        case 'B' | 'Y': return 1
        case 'C' | 'Z': return 2


def win(me: int, them: int) -> int:
    """Return 0 for loss, 1 for tie, 2 for win"""
    # result is 0 for tie, 1 for loss, 2 for win
    result = (them - me) % 3
    match result:
        case 0: return 1
        case 1: return 0
        case 2: return 2


def get_outcome(outcome: int, them: int) -> int:
    """Inverse of win. Determine what I should throw to get the outcome"""
    match outcome:
        case 1: return them
        case 2: return (them + 1) % 3
        case 0: return (them - 1) % 3


if __name__ == '__main__':
    filename = 'input.txt'

    fcn1 = utils.chain_args([lambda s: map(selection1, s.split()), total_score])
    total_score1 = sum(map(fcn1, utils.input_gen(filename)))
    print('solution 1:', total_score1)

    total_score2 = sum(map(score2, utils.input_gen(filename)))
    print('solution 1:', total_score2)
