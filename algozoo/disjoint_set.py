

from collections import defaultdict


#: class def

class NumberedDisjointSet(object):

    def __init__(self, N=0):

        # assume items are numbered 0 to N - 1
        self.table = list(range(N))
        self.size = N

        # whether all sets are pointing to root thier root subset
        self.flattened = True

    def __contains__(self, val):

        return val < self.size

    def __iter__(self):

        for disjoint_set in self.get_disjoint_sets():
            yield disjoint_set

    def __len__(self):

        return self.size

    def __repr__(self):

        # need to perform a groupby root to separate subsets
        self.flatten_table()

        disjoint_sets = self.get_disjoint_sets()

        subset_strings = []
        for items in disjoint_sets:
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

    def get_disjoint_sets(self):

        # need to perform a groupby root to separate subsets
        self.flatten_table()

        lut = defaultdict(list)

        for i, root in enumerate(self.table):
            lut[root].append(i)

        disjoint_sets = tuple(map(tuple, lut.values()))

        return disjoint_sets

    def is_disjoint(self, a, b):

        if not self.flattened:
            self.flatten(a)
            self.flatten(b)

        return self.table[a] != self.table[b]

    def is_joint(self, a, b):

        return not self.is_disjoint(a, b)


class FixedDisjointSet(NumberedDisjointSet):

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

        disjoint_sets = self.get_disjoint_sets()

        subset_strings = []
        for items in disjoint_sets:
            subset_strings.append("({})".format(
                                  ", ".join(map(repr, items))))

        subset_str = ", ".join(subset_strings)
        repr_str = "{name}({subsets})".format(name=self.__class__.__name__,
                                              subsets=subset_str)

        return repr_str

    def get_disjoint_sets(self):

        # need to perform a groupby root to separate subsets
        self.flatten_table()

        lut = defaultdict(list)

        for val, root in zip(self.lut.keys(), self.table):
            lut[root].append(val)

        disjoint_sets = tuple(map(tuple, lut.values()))

        return disjoint_sets

    def union(self, a, b):
        id_a, id_b = self.lut[a], self.lut[b]
        return super().union(id_a, id_b)

    def is_disjoint(self, a, b):
        id_a, id_b = self.lut[a], self.lut[b]
        return super().is_disjoint(id_a, id_b)


class DisjointSet(FixedDisjointSet):

    def __init__(self, items=None):

        super().__init__(items)

    def __contains__(self, val):

        return val in self.lut

    def add(self, val):

        if val not in self:
            self.lut[val] = self.size
            self.table.append(self.size)
            self.size += 1

    def union(self, a, b):

        if a not in self:
            self.add(a)
        if b not in self:
            self.add(b)

        super().union(a, b)

    def is_disjoint(self, a, b):
        if (a not in self) or (b not in self):
            return True
        return super().is_disjoint(a, b)


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


def _test_fds():

    ls = [1, 2, 56, 23,
          'aas', 'f', 2.3, (1, 2, 3)]

    fds = FixedDisjointSet(ls)

    fds.union(1, 2)
    fds.union(56, 2.3)
    fds.union(2.3, 2)

    fds.union('aas', (1, 2, 3))
    fds.union(2.3, 2.3)

    print(fds)

    return fds


def _test_ds():

    ls = [1, 2, 56, 23,
          'aas', 'f', 2.3, (1, 2, 3)]

    ds = DisjointSet(ls)

    ds.union(1, 2)
    ds.union(56, 2.3)
    ds.union(2.3, 2)

    ds.union('aas', (1, 2, 3))
    ds.union(2.3, 2.3)

    ds.add('extra')
    ds.add('extra2')

    ds.union('extra3', 'extra2')
    ds.union('extra2', 23)

    print(ds)

    return ds


def _main():

    print()
    _test_nds()

    print()
    _test_fds()

    print()
    _test_ds()

    print()


if __name__ == '__main__':

    _main()
