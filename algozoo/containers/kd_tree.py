

#: helper class


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
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError

    def __len__(self):
        return self.size

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        raise NotImplementedError

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

    def add(self, item):
        raise NotImplementedError

    def remove(self, item):
        raise NotImplementedError

    def in_range(self, upper, lower, axis=None):
        raise NotImplementedError


#: testing


def __main():

    print()

    raise NotImplementedError

    print()


if __name__ == '__main__':

    __main()
