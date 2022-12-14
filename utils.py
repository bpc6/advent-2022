import functools
from collections.abc import Iterable
from typing import Callable, List, TypeVar, Generator

T = TypeVar('T')


def chain(functions):
    """Chain the functions together so that they can be called on data later.
    Use when inputs are aggregate data types."""
    def chain_and_call(fcns, data):
        return functools.reduce(lambda prev, nex: nex(prev), fcns, data)
    return functools.partial(chain_and_call, functions)


def chain_args(functions):
    """Chain the functions together so that they can be called on data later.
    Use when mapping aggregate data to multiple inputs."""
    def chain_and_call(fcns, *args):
        return functools.reduce(lambda prev, nex: nex(*prev), fcns, args)
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


def split_by_count(n: int, iterable: Iterable[T]) -> List[T]:
    inner = []
    for item in iterable:
        inner.append(item)
        if len(inner) == n:
            yield inner
            inner = []
    if len(inner) > 0:
        yield inner


def input_gen(filename: str) -> Generator[str, None, None]:
    """Create a generator that returns the data line by line."""
    with open(filename, 'r') as f:
        for line in f:
            yield line.strip('\n')
