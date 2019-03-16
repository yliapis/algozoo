

#: Node def


class _TreeNode:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#: Tree def


class BinarySearchTree:

    _node_factory = _TreeNode

    def __init__(self, items=None, comparator=None):

        self.root = None
        self.size = 0

        if comparator is None:
            self.comparator = lambda a, b: a > b
        elif callable(comparator):
            self.comparator = comparator
        else:
            raise Exception("comparator={!r} is not "
                            "callable".format(comparator))

        if hasattr(items, '__iter__'):
            for item in items:
                self.insert(item)
        elif items is not None:
            raise Exception("items={!r} is not iterable".format(items))

    def __contains__(self, val):
        return self.search(val)

    def __iter__(self, node=None, start=True):
        """ DFS iteration """

        if start:
            node = self.root

        if node:
            if node.left:
                yield from self.__iter__(node.left, start=False)
            yield node.val
            if node.right:
                yield from self.__iter__(node.right, start=False)

    def __len__(self):
        return self.size

    def __repr__(self):

        bst_str = ', '.join(repr(item) for item in self)
        bst_str = "{name}({items})".format(name=self.__class__.__name__,
                                           items=bst_str)

        return bst_str

    def insert(self, val):
        self._insert_node(self._node_factory(val))

    def _insert_node(self, new_node):

        self.size += 1

        if not self.root:
            self.root = new_node
            return

        node = self.root
        while True:
            if self.comparator(new_node.val, node.val):
                if node.right:
                    node = node.right
                else:
                    node.right = new_node
                    return
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = new_node
                    return

    def remove(self, val):

        if not self.root:
            return

        node = self.root
        parent = None

        while node:
            if node.val == val:
                break
            elif self.comparator(val, node.val):
                if node.right:
                    parent = node
                    node = node.right
                else:
                    return
            else:
                if node.left:
                    parent = node
                    node = node.left
                else:
                    return

        self.size -= 1

        if parent:
            # break link
            if self.comparator(node.val, parent.val):
                parent.right = None
            else:
                parent.left = None
            # insert subtrees
            if node.right:
                self._insert_node(node.right)
            if node.left:
                self._insert_node(node.left)
        else:
            self.root = node.right
            if node.left:
                self._insert_node(node.left)

    def search(self, val):

        node = self.root

        while node:
            if node.val == val:
                return True
            elif self.comparator(val, node.val):
                node = node.right
            else:
                node = node.left

        return False


#: for testing


def _main():

    print()

    items = [1, 3, 2, 7, 4]

    tree = BinarySearchTree(items)

    print(tree)
    print()

    print("Removing 3")
    tree.remove(3)
    print(tree)
    print()

    for i in range(8):
        msg = "" if i in tree else "not "
        print("{i} is {msg}in tree".format(i=i, msg=msg))

    print()


if __name__ == '__main__':

    _main()
