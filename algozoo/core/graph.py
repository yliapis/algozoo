

from collections import defaultdict

from algozoo.algorithms.search import bfs_iter, dfs_iter


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
        return self

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

    # search methods

    def _get_val(self, node_id):
        return node_id

    def _get_next(self, node_id):
        return self._graph_lut[node_id]

    def dfs(self, node_id):
        yield from dfs_iter(root=node_id,
                            value=self._get_val,
                            key=self._get_next,
                            mode="graph",
                            order="first")

    def bfs(self, node_id):
        yield from bfs_iter(root=node_id,
                            value=self._get_val,
                            key=self._get_next,
                            mode="graph")

    def topological_sort(self, node_id):

        if not self.is_directed():
            raise Exception("topological_sort does not work "
                            "for directed graphs")

        raise NotImplementedError

    # graph properties

    def is_cyclic(self):
        raise NotImplementedError

    def is_directed(self):
        return self.directed


class WeightedGraph:

    def __init__(self):
        raise NotImplementedError


#: for testing


def __main():

    print()

    mat = [[0, 1, 0, 1],
           [0, 0, 1, 1],
           [0, 0, 0, 1],
           [0, 0, 0, 0]]

    g = Graph.from_adjacency_matrix(mat)

    print(g)
    print()

    print("DFS:", list(g.dfs(0)))
    print()

    print("BFS:", list(g.bfs(0)))
    print()


if __name__ == '__main__':

    __main()
