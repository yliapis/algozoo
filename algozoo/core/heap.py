

class Heap(object):

    def __init__(self, items=None, base_size=256,
                 comparator=lambda a, b: a > b):
        self.table = [0] * base_size
        self.size = 0
        self._table_size = base_size
        self._base_size = base_size
        self.comparator = comparator

        if hasattr(items, '__iter__'):
            for item in items:
                self.insert(item)
        elif items is not None:
            raise Exception("items={} is not iterable".format(items))

    def __iter__(self):
        yield from self.table[:self.size]

    def __repr__(self):
        return "{name}({items})".format(
            name=self.__class__.__name__,
            items=self.table[:self.size])

    def __len__(self):
        return self.size

    def __contains__(self):
        raise NotImplementedError

    def _downscale(self):
        self.table = self.table[:self._table_size // 2]

    def _upscale(self):
        self.table.extend([0] * self._table_size)

    def insert(self, val):

        ptr = self.size
        if ptr >= self._table_size:
            self._upscale()

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

        if self.size <= 0:
            raise Exception("heap is empty, cannot pop")

        val = self.table[0]

        self.size -= 1
        self.table[0] = self.table[self.size]

        ptr = 0
        while ptr < self.size:
            left = ((ptr + 1) * 2) - 1
            right = (ptr + 1) * 2

            swap = ptr
            if (left < self.size and
               self.comparator(self.table[swap], self.table[left])):
                swap = left
            if (right < self.size and
               self.comparator(self.table[swap], self.table[right])):
                swap = right

            if swap != ptr:
                self.table[ptr], self.table[swap] = (
                    self.table[swap], self.table[ptr])
                ptr = swap
            else:
                break

        if ((self.size // 4) < self._table_size and
           self._table_size // 2 >= self._base_size):
            self._downscale()

        return val

    def peak(self):

        if self.size > 0:
            return self.table[0]
        else:
            return None


#: for testing


def _main():

    print()

    items = [1, 4, 2, 3, -1]

    heap = Heap(items, base_size=2)

    print("items:", items)
    print(heap)
    print()

    sorted_items = []
    while len(heap) > 0:
        sorted_items.append(heap.pop())

    print("sorted items:", sorted_items)

    print()


if __name__ == '__main__':

    _main()
