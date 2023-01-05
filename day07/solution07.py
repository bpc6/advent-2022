from typing import Tuple

import utils
from day07.tree import Node


def add_to_tree(lines: Tuple[str], idx: int, tree: Node):
    try:
        line = lines[idx]
    except IndexError:
        return tree

    if line.startswith('$'):
        return parse_lines(lines, idx, tree)

    fsize, fname = line.split()
    if fsize == 'dir':
        tree.add_child(Node(fname))
    else:
        tree.add_child(Node(fname, int(fsize)))

    return add_to_tree(lines, idx + 1, tree)


def parse_lines(lines: Tuple[str], idx: int, tree: Node) -> Node:
    try:
        line = lines[idx]
    except IndexError:
        return tree

    if line.startswith('$ ls'):
        parse_lines(lines, idx + 1, add_to_tree(lines, idx + 1, tree))
    elif line.startswith('$ cd'):
        new_dir = line.strip().split()[-1]
        if new_dir == '..':
            new_tree = tree.parent
        else:
            new_tree = tree.get_child(new_dir)
        return add_to_tree(lines, idx + 1, new_tree)
    return tree


if __name__ == '__main__':
    filename = 'test.txt'
    with open(filename, 'r') as f:
        line_list = tuple(f.readlines())

    result = parse_lines(line_list, 1, Node('/'))
    print(result.tostring())
