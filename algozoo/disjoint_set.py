

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

        table = self.table[:]
        lut = defaultdict(list)

        for i, root in enumerate(table):
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

    def add(self, val):
        # should be initialized at class construction
        raise NotImplementedError()

    def union(self, a, b):

        self.flattened = False

        # assume both values are already initialized
        if a < b:
            self.table[b] = a
        else:
            self.table[a] = b

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


#: for testing


def _main():

    nds = NumberedDisjointSet(16)

    nds.union(4, 5)
    nds.union(2, 3)
    nds.union(2, 4)

    nds.union(11, 12)
    nds.union(13, 15)

    nds.union(0, 14)

    print(nds)

    return nds


if __name__ == '__main__':

    _main()
