import unittest

from day07.tree import Node


class TestTree(unittest.TestCase):
    def test_tostring(self):
        n = Node('/')
        a = Node('a')
        a.add_child(Node('f.txt', 13579))
        n.add_child(a)
        n.add_child(Node('b.txt', 12345))
        n.add_child(Node('c.txt', 2468))
        print(n.tostring())


if __name__ == '__main__':
    unittest.main()
