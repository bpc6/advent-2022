

class Node:
    def __init__(self, name: str, filesize: int = 0):
        self._name = name
        self._size = filesize
        self._children = []

    def add_child(self, node: 'Node') -> None:
        self._children.append(node)
