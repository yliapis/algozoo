

def _greater_than(a, b):
    return a > b


class _tree_node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:

    def __init__(self, items=None, comparator=_greater_than):

        self.root = None
        self.comparator = comparator

        if hasattr(items, '__iter__'):
            for item in items:
                self.insert(item)
        elif items is not None:
            raise Exception("items={} is not iterable".format(items))

    def __iter__(self, node="root"):
        """ DFS iteration """

        if node == "root":
            node = self.root

        if node:

            if node.left:
                for val in self.__iter__(node.left):
                    yield val

            yield node.val

            if node.right:
                for val in self.__iter__(node.right):
                    yield val

    def __str__(self):

        bst_str = ', '.join([repr(item) for item in self])
        bst_str = "BST({})".format(bst_str)

        return bst_str

    def insert(self, val, node=None):

        if self.root is None:
            self.root = _tree_node(val)
            return

        if node is None:
            node = self.root

        if self.comparator(val, node.val):
            if node.right is None:
                node.right = _tree_node(val)
            else:
                self.insert(val, node.right)
        else:
            if node.left is None:
                node.left = _tree_node(val)
            else:
                self.insert(val, node.left)

    def search(self, val, node=None):

        if not node:
            node = self.root

        if not node:
            return False

        if node.val == val:
            return True
        elif self.comparator(val, node.val):
            if node.right is None:
                return False
            else:
                self.search(val, node.right)
        else:
            if node.left is None:
                return False
            else:
                self.search(node.left)


if __name__ == '__main__':

    items = [1, 3, 2, 5, 4, 9]

    tree = BST(items)

    print(tree)
