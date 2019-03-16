

#

def dfs_iter(root=None,
             value=lambda node: node.val,
             key=lambda node: node.next):
    """Generic depth-first search iterator

    NOTE: assumes structure is directed acyclic graph;
    does not work with cyclic data structures
    """

    if root is None:
        return

    yield value(root)
    yield from key(root)


def bfs_iter(root=None,
             value=lambda node: node.val,
             key=lambda node: node.next):
    """Generic breadth-first search iterator

    NOTE: assumes structure is directed acyclic graph;
    does not work with cyclic data structures
    """

    if root is None:
        return

    queue = [root]

    while queue:
        node = queue.pop(0)
        if node is not None:
            yield value(node)
            queue.extend(list(key(node)))


#: for testing


def _test_dfs():
    pass


def _test_bfs():
    pass


def _main():

    print()

    _test_dfs()
    print()

    _test_bfs()
    print()


if __name__ == '__main__':

    _main()
