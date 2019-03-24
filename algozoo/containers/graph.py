

from collections import defaultdict


#: class def


class Graph:

    def __init__(self, directed=True):

        self._graph_lut = defaultdict(set)
        self.directed = directed

    # __ methods

    def __contains__(self, node_id):
        return node_id in self._graph_lut

    def __len__(self):
        return len(self._graph_lut)

    # class methods:
    # construct from various representations

    @classmethod
    def from_edgelist(cls, edgelist, *args, **kwargs):
        self = cls(*args, **kwargs)
        for head, tail in edgelist:
            self.add_edge(head, tail)
        return self

    @classmethod
    def from_adjacency_list(cls, adjacency_list, *args, **kwargs):
        self = cls(*args, **kwargs)
        for src, dsts in adjacency_list:
            self.add_edges(src, dsts)
        return self

    @classmethod
    def from_adjacency_matrix(cls, matrix, *args, **kwargs):
        self = cls(*args, **kwargs)
        N = len(matrix)
        for m in range(N):
            for n in range(N):
                if matrix[m][n]:
                    self.add_edge(m, n)

    @classmethod
    def from_structure(cls, root, *args, **kwargs):
        self = cls(*args, **kwargs)
        raise NotImplementedError
        return self

    # manipulation methods

    def add_edge(self, src, dst):
        self._graph_lut[src].add(dst)
        if not self.directed:
            self._graph_lut[dst].add(src)

    def add_edges(self, src, dsts):
        self._graph_lut[src].update(dsts)
        if not self.directed:
            for dst in dsts:
                self._graph_lut[dst].add(src)

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
        N = len(self)
        matrix = [[0] * N for _ in range(N)]
        for src, dsts in self._graph_lut:
            for dst in dsts:
                matrix[src][dst] = 1

        return matrix


#: for testing


def __main():

    print()

    raise NotImplementedError

    print()


if __name__ == '__main__':

    __main()
