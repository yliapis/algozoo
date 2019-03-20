

#: class def


class Graph:

    def __init__(self):

        raise NotImplementedError

    # __ methods

    def __contains__(self, node_id):
        raise NotImplementedError

    # class methods:
    # construct from various representations

    @classmethod
    def from_edgelist(cls, edgelist):
        self = cls()
        for head, tail in edgelist:
            self.add_edge(head, tail)
        return self

    @classmethod
    def from_adjacency_list(cls, adjacency_list):
        self = cls()
        for node, neighbors in adjacency_list:
            for neighbor in neighbors:
                self.add_edge(node, neighbor)
        return self

    @classmethod
    def from_adjacency_matrix(cls, root):
        self = cls()
        raise NotImplementedError
        return self

    @classmethod
    def from_structure(cls, root):
        self = cls()
        raise NotImplementedError
        return self

    # manipulation methods

    def add_edge(self, src, dst):
        raise NotImplementedError

    # representation extraction methods

    def get_edgelist(self):
        raise NotImplementedError

    def get_adjacency_list(self):
        raise NotImplementedError

    def get_adjacency_matrix(self):
        raise NotImplementedError


#: for testing


def __main():

    print()

    raise NotImplementedError

    print()


if __name__ == '__main__':

    __main()
