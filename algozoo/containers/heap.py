

class FiniteHeap(object):

    def __init__(self, items=None, size=256):
        self.table = [0] * size
        self.size = 0
        self._table_size = size
        self.comparator = lambda a, b: a > b

        if hasattr(items, '__iter__'):
            for item in items:
                self.insert(item)
        elif items is not None:
            raise Exception("items={} is not iterable".format(items))

    def __iter__(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    def __len__(self):
        return self.size

    def __contains__(self):
        raise NotImplementedError

    def insert(self, val):
        
        ptr = self.size
        if ptr >= self._table_size:
            raise NotImplementedError("element does not fit")

        self.table[ptr] = val
        self.size += 1

        while ptr > 0:
            parent = (ptr - 1) // 2
            if self.comparator(self.table[ptr],
                               self.table[parent]):
                break
            else:
                self.table[parent], self.table[ptr] = (
                    self.table[ptr], self.table[parent])
                ptr = parent

    def pop(self):
        
        val = self.table[0]

        self.size -= 1
        self.table[0] = self.table[self.size]

        ptr = 0
        while ptr < self.size:
            left = ((ptr + 1) * 2) - 1
            right = (ptr + 1) * 2

            if (self.comparator(self.table[left], self.table[ptr]) and
                self.comparator(self.table[right], self.table[ptr])):
                break
            elif self.comparator(self.table[left], self.table[right]):
                self.table[right], self.table[ptr] = (
                    self.table[ptr], self.table[right])
                ptr = right
            else:
                self.table[left], self.table[ptr] = (
                    self.table[ptr], self.table[left])
                ptr = left

        return val


#: for testing


def _main():

    items = [1, 4, 2, 3, -1]

    fh = FiniteHeap(items)

    print("items:", items)
    print(fh.table)

    sorted_items = []
    while len(fh) > 0:
        sorted_items.append(fh.pop())

    print("sorted items:", sorted_items)


if __name__ == '__main__':

    _main()
