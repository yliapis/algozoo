

# testing imports
if __name__ == '__main__':
    import random


#: core/helper functions


def _graph_dfs_iter(root=None,
                    value=lambda node: node.val,
                    key=lambda node: node.next,
                    visited=None,
                    order="first"):
    """Generic depth-first search iterator"""

    if visited is None:
        visited = set()

    if root is None:
        return

    if root not in visited:
        if order == "first":
            yield value(root)
        visited.add(root)
        for node in key(root):
            yield from _graph_dfs_iter(node,
                                       key=key,
                                       value=value,
                                       visited=visited,
                                       order=order)
        if order == "last":
            yield value(root)


def _graph_bfs_iter(root=None,
                    value=lambda node: node.val,
                    key=lambda node: node.next):
    """Generic breadth-first search iterator"""

    queue = [root]
    visited = set()

    while queue:
        node = queue.pop(0)
        if node is not None and node not in visited:
            yield value(node)
            visited.add(node)
            queue.extend(key(node))


def _tree_dfs_iter(root=None,
                   value=lambda node: node.val,
                   key=lambda node: node.next,
                   order="first"):
    """Generic depth-first search iterator

    NOTE: assumes structure is tree-like;
    does not work with cyclic data structures
    """

    if root is None:
        return

    if order == "first":
        yield value(root)
    for node in key(root):
        yield from _tree_dfs_iter(node,
                                  key=key,
                                  value=value,
                                  order=order)
    if order == "last":
        yield value(root)


def _tree_bfs_iter(root=None,
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


#: search functions


def dfs_iter(root, mode="graph", *args, **kwargs):
    if mode == "graph":
        return _graph_dfs_iter(root, *args, **kwargs)
    elif mode == "tree":
        return _tree_dfs_iter(root, *args, **kwargs)
    else:
        raise NotImplementedError(
                "Error: dfs not implimented for "
                "mode={mode}".format(mode=mode))


def bfs_iter(root, mode="graph", *args, **kwargs):
    if mode == "graph":
        return _graph_bfs_iter(root, *args, **kwargs)
    elif mode == "tree":
        return _tree_bfs_iter(root, *args, **kwargs)
    else:
        raise NotImplementedError(
                "Error: bfs not implimented for "
                "mode={mode}".format(mode=mode))


#: for testing


class __testNode:

    def __init__(self, val, next=None):

        self.val = val

        if next is None:
            self.next = []
        else:
            self.next = next

    def __repr__(self):
        # NOTE: this breaks for cyclic structures
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
    print("dfs")
    print("first", list(dfs_iter(tree, order="first")))
    print("last", list(dfs_iter(tree, order="last")))


def _test_bfs(tree):
    print("bfs")
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
