

def _avl_tree_node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.n_left = 0
        self.n_right = 0

    @property
    def balance(self):
        return self.n_right - self.n_left

    def insert(self, val):

        pass

    