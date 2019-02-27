

class _set_node:

    def __init__(self, val, hash_id):

        self.hash_id = None
        self.val = val
        self.next = None


class UnorderedSet:

    def __init__(self, size=256, hash_function=hash):

        self.table = [None for _ in range(size)]
        self.hash_function = hash_function
        self.size = size
        self.cardinality = 0

    def __iter__(self):

        for entry in self.table:
            while entry:
                yield entry.val
                entry = entry.next

    def __len__(self):

        return self.cardinality

    def __repr__(self):

        set_string = ', '.join([repr(val) for val in self])
        set_string = '{' + set_string + '}'

        return set_string

    def __str__(self):

        return self.__repr__()

    def __contains__(self, val):

        # Note: assuming no collisions in raw hash output
        try:
            hash_id = self.hash_function(val)
        except TypeError:
            TypeError("Error: type {} is not hashable".format(type(val)))

        idx = hash_id % self.size

        node = self.table[idx]

        while node:
            if node.val == val:
                return True
            node = node.next

        return False

    def add(self, val):

        # Note: assuming no collisions in raw hash output
        try:
            hash_id = self.hash_function(val)
        except TypeError:
            TypeError("Error: type {} is not hashable".format(type(val)))

        idx = hash_id % self.size

        if self.table[idx] is None:
            self.table[idx] = _set_node(val, hash_id)
            self.cardinality += 1
        else:
            node = self.table[idx]
            while True:
                # check if value has already been added
                if node.hash_id == hash_id:
                    return
                # check if there is another node in the chain
                if node.next:
                    node = node.next
                # if not, break and add it
                else:
                    break
            node.next = _set_node(val, hash_id)
            self.cardinality += 1

    def remove(self, val):

        # Note: assuming no collisions in raw hash output
        try:
            hash_id = self.hash_function(val)
        except TypeError:
            TypeError("Error: type {} is not hashable".format(type(val)))

        idx = hash_id % self.size

        root_node = self.table[idx]
        prev_node = None
        node = root_node
        while node:
            if node.val == val:
                if node is root_node:
                    self.table[idx] = None
                else:
                    prev_node.next = node.next
                self.cardinality -= 1
                return
            else:
                prev_node = node
                node = node.next

    def union(self, other_set):

        for val in other_set:
            self.add(val)

    def difference(self, other_set):

        for val in other_set:
            self.remove(val)


if __name__ == '__main__':

    myset = UnorderedSet()

    myset.add(3)
    myset.add(4)
    myset.add(1234)
    myset.add("hello")
    myset.remove(3)

    for i in range(1000):
        myset.add(i)

    for i in range(3, 1000):
        myset.remove(i)

    print(myset)
