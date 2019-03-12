

from collections import defaultdict


#: class def

class NumberedDisjointSet(object):

    def __init__(self, N=0):

        # assume items are numbered 0 to N - 1
        self.table = list(range(N))
        self.size = N

        #
        self.flattened = True

    def __contains__(self, val):

        return val < self.size

    def __len__(self):

        return self.size

    def __repr__(self):

        # need to perform a groupby root to separate subsets
        self.flatten_table()

        lut = defaultdict(list)

        for i, root in enumerate(self.table):
            lut[root].append(i)

        subset_strings = []
        for items in lut.values():
            subset_strings.append("({})".format(
                                  ", ".join(map(repr, items))))

        subset_str = ", ".join(subset_strings)
        repr_str = "{name}({subsets})".format(name=self.__class__.__name__,
                                              subsets=subset_str)

        return repr_str

    def __str__(self):

        return repr(self)

    def union(self, a, b):

        self.flattened = False

        # assume both values are already initialized
        root_a, root_b = self.table[a], self.table[b]
        root = min(*(a, b, root_a, root_b))
        self.table[a] = root
        self.table[b] = root
        self.table[root_a] = root
        self.table[root_b] = root

    def flatten(self, val):

        root = self.table[val]
        while root != self.table[root]:
            root = self.table[root]

        self.table[val] = root

    def flatten_table(self):

        if not self.flattened:
            for val in range(self.size):
                self.flatten(val)

    def is_disjoint(self, a, b):

        if not self.flattened:
            self.flatten(a)
            self.flatten(b)

        return self.table[a] != self.table[b]

    def is_joint(self, a, b):

        return not self.is_disjoint(a, b)


class DisjointSet(NumberedDisjointSet):

    def __init__(self, items):

        if hasattr(items, '__iter__'):
            self.lut = {item: i for i, item in enumerate(items)}
        elif items is None:
            self.lut = dict()
        else:
            raise Exception("items={} is not iterable".format(items))

        N = len(self.lut)

        super().__init__(N)

    def __contains__(self, val):
        return val in self.lut

    def __repr__(self):

        # need to perform a groupby root to separate subsets
        self.flatten_table()

        lut = defaultdict(list)

        for val, root in zip(self.lut.keys(), self.table):
            lut[root].append(val)

        subset_strings = []
        for items in lut.values():
            subset_strings.append("({})".format(
                                  ", ".join(map(repr, items))))

        subset_str = ", ".join(subset_strings)
        repr_str = "{name}({subsets})".format(name=self.__class__.__name__,
                                              subsets=subset_str)

        return repr_str

    def union(self, a, b):
        id_a, id_b = self.lut[a], self.lut[b]
        return super().union(id_a, id_b)

    def is_disjoint(self, a, b):
        id_a, id_b = self.lut[a], self.lut[b]
        return super().is_disjoint(id_a, id_b)



#: for testing


def _test_nds():

    nds = NumberedDisjointSet(16)

    nds.union(4, 5)
    nds.union(2, 3)
    nds.union(2, 4)

    nds.union(11, 12)
    nds.union(13, 15)

    nds.union(0, 14)

    print(nds)

    return nds


def _test_ds():

    ls = [1, 2, 56, 23,
          'aas', 'f', 2.3, (1, 2, 3)]

    ds = DisjointSet(ls)

    ds.union(1, 2)
    ds.union(56, 2.3)
    ds.union(2.3, 2)

    ds.union('aas', (1, 2, 3))
    ds.union(2.3, 2.3)

    print(ds)

    return ds


def _main():

    print()

    _test_nds()

    print()
    
    _test_ds()

    print()


if __name__ == '__main__':

    _main()
