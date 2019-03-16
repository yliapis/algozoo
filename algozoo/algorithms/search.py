

#

def dfs_iter(root=None, key=lambda node: node.next):
    """Generic depth-first search iterator 

    NOTE: assumes structure is directed acyclic graph;
    does not work with cyclic data structures
    """

    if root is None:
        return

    yield root.val
    yield from key(root)


def bfs_iter(root=None, key=lambda node: node.next):
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
            yield node.val
            queue.extend(list(key(node)))


#: for testing


def _main():

    print()

    _test_dfs()
    print()

    _test_bfs()
    print()


if __name__ == '__main__':

    _main()
