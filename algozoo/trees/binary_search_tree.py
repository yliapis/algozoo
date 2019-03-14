

#: class def


class _BSTNode:
    """
    """

    def __init__(self, val=None, left=None, right=None,
                 comparator=None, *args, **kwargs):

        self.val = val
        self.left = left
        self.right = right

        if comparator is None:
            self.comparator = lambda a, b: a > b
        else:
            self.comparator = comparator

        # for name, val in kwargs:
        #     setattr(self, name, val)

    def __contains__(self, val):

        return self.search(val)

    def __iter__(self):

        if self.left:
            yield from self.left
        yield self.val
        if self.right:
            yield from self.right

    def __repr__(self):

        repr_vals = ", ".join(map(repr, self))
        repr_str = "{name}({items})".format(name=self.__class__.__name__,
                                            items=repr_vals)

        return repr_str

    @classmethod
    def from_iterable(cls, iterable):

        self = cls()
        self.insert_items(iterable)
        return self

    def insert(self, val):

        if self.val is None:  # for uninitialized tree
            self.val = val
        elif self.comparator(val, self.val):
            if self.right:
                self.right.insert(val)
            else:
                self.right = _BSTNode(val, comparator=self.comparator)
        else:
            if self.left:
                self.left.insert(val)
            else:
                self.left = _BSTNode(val, comparator=self.comparator)

    def insert_items(self, items):

        for item in items:
            self.insert(item)

    def search(self, val):

        if self.val is None:
            return False
        if self.val == val:
            return True
        elif self.comparator(val, self.val):
            if self.right:
                return self.right.search(val)
            else:
                return False
        else:
            if self.left:
                return self.left.search(val)
            else:
                return False


class BinarySearchTree:

    def __init__(self, items=None):

        if hasattr(items, '__iter__'):
            self.tree = _BSTNode.from_iterable(items)
        elif items is None:
            self.tree = _BSTNode()
        else:
            raise Exception("items={} is not iterable".format(items))

    def __contains__(self, val):
        return val in self.tree

    def __iter__(self):
        return iter(self.tree)

    def __repr__(self):

        repr_vals = ", ".join(map(repr, self))
        repr_str = "{name}({items})".format(name=self.__class__.__name__,
                                            items=repr_vals)

        return repr_str

    def insert(self, *args, **kwargs):
        self.tree.insert(*args, **kwargs)

    def search(self, *args, **kwargs):
        self.tree.search(*args, **kwargs)


#: for testing


def _main():

    print()

    items = [1, 3, 7, 5, 4]

    tree = BinarySearchTree(items)

    print(tree)
    print()

    for i in range(8):
        msg = "" if i in tree else "not "
        print("{i} is {msg}in tree".format(i=i, msg=msg))

    print()

    return tree


if __name__ == '__main__':

    _main()
