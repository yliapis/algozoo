

from binary_search_tree import _TreeNode, BinarySearchTree


class _RBTNode(_TreeNode):

    def __init__(self, val, red=True, *args, **kwargs):
        super().__init__(val, *args, **kwargs)
        self.red = red


class RedBlackTree(BinarySearchTree):
    """ Left leaning red link, red-black BST
    """

    # update node factory
    _node_factory = _RBTNode

    def insert(self, val):
        new_node = self._node_factory(val)
        self.root = self._insert_node(new_node, self.root)

    def _insert_node(self, new_node, node=None):

        # standard insert
        self.size += 1
        if node is None:
            return new_node
        elif self.comparator(new_node.val, node.val):
            node.right = self._insert_node(new_node, node.right)
        else:
            node.left = self._insert_node(new_node, node.left)

        # rebalancing rules applied
        node = self._rebalance(node)

        return node

    def remove(self, val):
        self.root = self._recursive_remove(val, self.root)

    def _recursive_remove(self, val, node):

        # TODO: double check this implementation, make sure
        # it still results in a balanced tree

        if node is None:
            return None

        if val == node.val:
            if node.left and node.right:
                return self._insert_node(node.left, node.right)
            elif node.left:
                return node.left
            else:
                return node.right
        elif self.comparator(val, node.val):
            node.right = self._recursive_remove(val, node.right, node)
        else:
            node.left = self._recursive_remove(val, node.left, node)

        return node

    def _rebalance(self, node):
        # left leaning link red-black BST rules
        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)
        if self._is_red(node.right) and self._is_red(node.left):
            self._flip_colors(node)

        return node

    def _is_red(self, node):

        if node is None:
            return False
        else:
            return node.red

    def _rotate_left(self, node):
        # rotate
        parent = node.right
        node.right = node.left
        node.left = node
        # modify colors
        parent.red = node.red
        node.red = True
        return parent

    def _rotate_right(self, node):
        # rotate
        parent = node.left
        node.left = node.right
        node.right = node
        # modify colors
        parent.red = node.red
        node.red = True
        return parent

    def _flip_colors(self, node):
        node.red = True
        node.left.red = node.right.red = False


#: for testing


def _main():

    print()

    items = [1, 3, 2, 7, 4]

    tree = RedBlackTree(items)

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
