

#: internal node class


class _KDNode:

    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


#: implementation class


class KDTree:

    def __init__(self, items):
        # NOTE: items need to all have the same dimension
        items = list(items)
        dim = len(items[0])

        self.dim = dim
        self.size = len(items)

        self.root = self._construct_tree(items)

    def __contains__(self, item):

        node = self.root

        depth = 0

        while node:

            level = depth % self.dim

            if node.key == item:
                return True
            elif node.key[level] < item[level]:
                node = node.left
            else:
                node = node.right

            depth += 1

        return False

    def __iter__(self):
        yield from self._iter_tree(self.root)

    def __len__(self):
        return self.size

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        item_str = ", ".join(map(repr, self._nested_items(self.root)))
        repr_str = "{name}({items})".format(name=self.__class__.__name__,
                                            items=item_str)
        return repr_str

    def _construct_tree(self, items, level=0):

        if len(items) == 0:
            return None

        items = sorted(items, key=lambda item: item[level])

        median = len(items) // 2
        node = _KDNode(items[median])

        lower = items[:median]
        upper = items[median + 1:]

        next_level = (level + 1) % self.dim
        node.left = self._construct_tree(lower, next_level)
        node.right = self._construct_tree(upper, next_level)

        return node

    def _iter_tree(self, node):

        if node is None:
            return

        yield from self._iter_tree(node.left)
        yield node.key
        yield from self._iter_tree(node.right)

    def _nested_items(self, node):
        if node is None:
            return ()
        else:
            return (node.key,
                    self._nested_items(node.left),
                    self._nested_items(node.right))

    def _recursive_remove(self, node, item, depth=0):

        if not node:
            return None
        elif node.key == item:
            return self._construct_tree([*self._iter_tree(node.left),
                                         *self._iter_tree(node.right)])

        level = depth % self.dim
        depth += 1
        if node.key[level] < item[level]:
            return self._recursive_remove(node.left, item, depth)
        else:
            return self._recursive_remove(node.right, item, depth)

    def add(self, item, depth=0):

        node = self.root

        if self.root is None:
            node = _KDNode(item)
            return

        while True:

            level = depth % self.dim

            if node.key == item:
                return
            elif (node.key[level] < item[level]
                  and not node.left):
                node.left = _KDNode(item)
                return
            elif not node.right:
                node.right = _KDNode(item)
                return

            depth += 1

    def remove(self, item):
        self.root = self._recursive_remove(self.root, item)

    def in_range(self, upper, lower, axis=None):
        raise NotImplementedError


#: testing


def __main():

    print()

    items = [(1, 2),
             (9, 3),
             (8, 1),
             (3, 2),
             (7, -1)
             ]

    kdt = KDTree(items)
    print(kdt)

    print()


if __name__ == '__main__':

    __main()
