

from binary_search_tree import BinarySearchTree


def AVLTree(BinarySearchTree):

    def __init__(self, *args, **kwargs):

        self.n_left = 0
        self.n_right = 0

        super().__init__()

        # remove once implementation is complete
        raise NotImplementedError


    @property
    def balance(self):
        return self.n_left - self.n_right
    