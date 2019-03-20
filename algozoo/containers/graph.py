

from collections import defaultdict


#: class def


class Graph:

    def __init__(self):

        self._graph_lut = defaultdict(list)

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
        for src, dsts in adjacency_list:
            self.add_edges(src, dsts)
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
        self._graph_lut[src].append(dst)

    def add_edges(self, src, dsts):
        self._graph_lut[src].extend(dsts)

    # representation extraction methods

    def get_edgelist(self):
        edgelist = []
        for src, dsts in self._graph_lut.items():
            for dst in dsts:
                edgelist.append((src, dst))
        return edgelist

    def get_adjacency_list(self):
        return [(src, dsts) for src, dsts in
                self._graph_lut.items()]

    def get_adjacency_matrix(self):
        raise NotImplementedError


#: for testing


def __main():

    print()

    raise NotImplementedError

    print()


if __name__ == '__main__':

    __main()
