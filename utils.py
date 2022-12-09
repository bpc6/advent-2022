import functools
from typing import Callable, List, TypeVar, Generator

T = TypeVar('T')


def chain(fns, data):
    return functools.reduce(lambda prev, nex: nex(prev), fns, data)


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


def get_input(filename: str) -> Generator[str, None, None]:
    with open(filename, 'r') as f:
        for line in f:
            yield line
