

#: class def


class BinarySearchTree:
    """
    """

    def __init__(self, val=None, left=None, right=None):

        self.val = val
        self.left = left
        self.right = right

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
        for val in iterable:
            self.insert(val)

        return self


    def insert(self, val):

        if self.val is None:  # for uninitialized tree
            self.val = val
        elif val > self.val:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BinarySearchTree(val)
        else:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BinarySearchTree(val)

    def search(self, val):

        if self.val == val:
            return True
        elif val > self.val:
            if self.right:
                return self.right.search(val)
            else:
                return False
        else:
            if self.left:
                return self.left.search(val)
            else:
                return False

#: for testing


def _main():

    items = [1, 3, 7, 5, 4]

    tree = BinarySearchTree.from_iterable(items)

    print(tree)

    for i in range(8):
        msg = "" if i in tree else "not "
        print("{i} is {msg}in tree".format(i=i, msg=msg))

    return tree

if __name__ == '__main__':

    _main()
