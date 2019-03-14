

from binary_search_tree import _TreeNode, BinarySearchTree


class _RBTNode(_TreeNode):

    def __init__(self, val, red=True, *args, **kwargs):
        super().__init__(val, *args, **kwargs)
        self.red = red


class RedBlackTree(BinarySearchTree):

    _node_factory = _RBTNode

    def __init__(self, *args, **kwargs):

        # remove once implementation is complete
        raise NotImplementedError
