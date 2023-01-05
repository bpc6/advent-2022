from typing import Optional


class Node:
    def __init__(self, name: str, filesize: int = 0):
        self._name = name
        self._size = filesize
        self._children = {}
        self.parent: Optional[Node] = None

    @property
    def name(self) -> str:
        return self._name

    def add_child(self, node: 'Node') -> None:
        node.parent = self
        self._children[node.name] = node

    def get_child(self, name: str) -> 'Node':
        try:
            return self._children[name]
        except KeyError:
            raise KeyError(f'Name {name} is not a child.')

    def tostring(self, depth: int = 0) -> str:
        children_strings = [n.tostring(depth + 1) for n in self._children.values()]
        return depth * ' ' + self._name + '\n' + ''.join(children_strings)
