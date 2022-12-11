import functools
from typing import Callable, List, TypeVar, Generator

T = TypeVar('T')


def chain(functions):
    """Chain the functions together so that they can be called on data later."""
    def chain_and_call(fcns, data):
        return functools.reduce(lambda prev, nex: nex(prev), fcns, data)
    return functools.partial(chain_and_call, functions)


def split_when(
    condition: Callable[[T], bool],
    gen: Generator[List[T], None, None]
) -> List[T]:
    """Split the list into a generator of lists according to the condition."""
    inner = []
    for item in gen:
        if condition(item):
            yield inner
            inner = []
        else:
            inner.append(item)
    if len(inner) > 0:
        yield inner


def input_gen(filename: str) -> Generator[str, None, None]:
    """Create a generator that returns the data line by line."""
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip('\n')
