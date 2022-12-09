import functools
from typing import Callable, List, TypeVar


T = TypeVar('T')


def chain(fns, data):
    for fn in fns:
        data = fn(data)
    return data


def split_when(condition: Callable[[T], bool], lst: List[List[T]]):
    """Split the list into a list of lists according to the condition."""
    outter = []
    inner = []
    for s in lst:
        if condition(s):
            outter.append(inner)
            inner = []
        else:
            inner.append(s)
    if len(inner) > 0:
        outter.append(inner)
    return outter
