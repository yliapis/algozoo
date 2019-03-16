

# testing imports
if __name__ == '__main__':
    import random


#: search functions


def dfs_iter(root=None,
             value=lambda node: node.val,
             key=lambda node: node.next):
    """Generic depth-first search iterator

    NOTE: assumes structure is tree-like;
    does not work with cyclic data structures
    """

    if root is None:
        return

    yield value(root)
    for node in key(root):
        yield from dfs_iter(node)


def bfs_iter(root=None,
             value=lambda node: node.val,
             key=lambda node: node.next):
    """Generic breadth-first search iterator

    NOTE: assumes structure is tree-like;
    does not work with cyclic data structures
    """

    queue = [root]

    while queue:
        node = queue.pop(0)
        if node is not None:
            yield value(node)
            queue.extend(key(node))


#: for testing


class __testNode:

    def __init__(self, val, next=None):

        self.val = val

        if next is None:
            self.next = []
        else:
            self.next = next

    def __repr__(self):
        return "({val}: ({next}))".format(
                    val=self.val,
                    next=", ".join(map(repr, self.next)))


def __construct_random_tree(size=8):

    # create nodes
    nodes = []
    for i in range(size):
        nodes.append(__testNode(i))

    for i in range(1, size):
        parent_id = random.randint(0, i - 1)
        nodes[parent_id].next.append(nodes[i])

    return nodes[0]


def _test_dfs(tree):
    print(list(dfs_iter(tree)))


def _test_bfs(tree):
    print(list(bfs_iter(tree)))


def _main():

    print()

    tree = __construct_random_tree(8)
    print(tree)
    print()

    _test_dfs(tree)
    print()

    _test_bfs(tree)
    print()


if __name__ == '__main__':

    _main()
