from typing import TypeVar, Generic, List, Tuple

T = TypeVar('T')


class Stack(Generic[T]):
    @staticmethod
    def push(item: T, stack: Tuple[T]) -> Tuple[T]:
        return stack + tuple(item)

    @staticmethod
    def is_empty(stack: Tuple[T]) -> bool:
        return len(stack) == 0

    @staticmethod
    def pop(stack: Tuple[T]) -> Tuple[T, Tuple[T]]:
        return stack[-1], stack[:-1]
