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


def split_when2(
        condition: Callable[[T], bool],
        gen: Generator[List[T], None, None]
):
    """Split the list into a generator of lists according to the condition."""

    class InnerIter:
        def __init__(self, outer_gen):
            self._gen = outer_gen
        def __next__(self):
            for val in next(self._gen):
                if condition(val):
                    raise StopIteration
                return val
        def __iter__(self):
            return self

    return InnerIter(gen)


def recursive_list(generator):
    lst = []
    try:
        for item in generator:
            if isinstance(item, Generator):
                lst.append(recursive_list(item))
            else:
                lst.append(item)
    except Exception:
        pass
    return lst
