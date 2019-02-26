

def _greater_than(a, b):
    return a > b


class _tree_node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:

    def __init__(self, comparator=_greater_than):

        self.root = None
        self.comparator = comparator

    def insert(self, val, node=None):

        if self.root is None:
            self.root = _tree_node(val)
            return

        if node is None:
            node = self.root

        if self.comarator(val, node.val):
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
