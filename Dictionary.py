

class _dict_node:

    def __init__(self, hash_id, key, val, next=None):

        self.hash_id = hash_id
        self.key = key
        self.val = val
        self.next = None


class Dictionary:

    def __init__(self, size=256, hash_function=hash):

        self.table = [None for _ in range(size)]
        self.size = size
        self.hash_function = hash_function
        self.cardinality = 0

    def __setitem__(self, key, val):

        try:
            hash_id = self.hash_function(key)
        except TypeError:
            TypeError("Error: type {} is not hashable".format(type(key)))

        idx = hash_id % self.size

        if self.table[idx] is None:
            self.table[idx] = _dict_node(hash_id, key, val)
            self.cardinality += 1
        else:
            node = self.table[idx]
            while True:
                # check if value has already been added,
                # and modify accordingly
                if node.key == key:
                    node.val = val
                    return
                # check if there is another node in the chain
                if node.next:
                    node = node.next
                # if not, break and add it
                else:
                    break
            node.next = _dict_node(hash_id, key, val)
            self.cardinality += 1

    def __getitem__(self, key):

        try:
            hash_id = self.hash_function(key)
        except TypeError:
            TypeError("Error: type {} is not hashable".format(type(key)))

        idx = hash_id % self.size

        if self.table[idx] is None:
            raise KeyError("Key {} does not exist".format(key))

        node = self.table[idx]
        while node:
            if node.hash_id == hash_id:
                return node.val
            node = node.next

        raise KeyError("Key {} does not exist".format(key))

    def __delitem__(self, key):

        # Note: assuming no collisions in raw hash output
        try:
            hash_id = self.hash_function(key)
        except TypeError:
            TypeError("Error: type {} is not hashable".format(type(key)))

        idx = hash_id % self.size

        if self.table[idx] is None:
            raise KeyError("Key {} does not exist".format(key))

        root_node = self.table[idx]
        prev_node = None
        node = root_node
        while node:
            if node.key == key:
                if node is root_node:
                    self.table[idx] = None
                else:
                    prev_node.next = node.next
                self.cardinality -= 1
                return
            else:
                prev_node = node
                node = node.next

        raise KeyError("Key {} does not exist".format(key))

    def __iter__(self):

        for entry in self.table:
            while entry:
                yield entry.key, entry.val
                entry = entry.next

    def __len__(self):

        return self.cardinality

    def __repr__(self):

        dict_items = ["{!r}: {!r}".format(key, val) for key, val
                      in self]

        dict_str = 'Dictionary(' + ", ".join(dict_items) + ')'

        return dict_str

    def __str__(self):

        return self.__repr__()

    def keys(self):

        for entry in self.table:
            while entry:
                yield entry.key
                entry = entry.next

    def values(self):

        for entry in self.table:
            while entry:
                yield entry.val
                entry = entry.next

    def items(self):

        return self.__iter__()


if __name__ == '__main__':

    d = Dictionary()
    d[0] = 1
    print(d[0])
    d[0] = 3
    d[2] = 4
    print(d[0])
    print(d[2])
    del d[2]

    print()
    print(d)
    print(len(d))
