
from algozoo.core.linked_list import SinglyLinkedList


#: Dictionary def


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

        item = (hash_id, key, val)

        if self.table[idx] is None:
            sll = SinglyLinkedList()
            sll.insert(item)
            self.table[idx] = sll
            self.cardinality += 1
        else:
            sll = self.table[idx]
            success = sll.replace(hash_id, item, getter=lambda x: x[0])
            if not success:
                sll.insert(item)
                self.cardinality += 1

    def __getitem__(self, key):

        try:
            hash_id = self.hash_function(key)
        except TypeError:
            TypeError("Error: type {} is not hashable".format(type(key)))

        idx = hash_id % self.size

        sll = self.table[idx]
        if sll is None:
            raise KeyError("Key {} does not exist".format(key))

        item = sll.getitem(hash_id, getter=lambda x: x[0])
        if item:
            return item[2]

        raise KeyError("Key {} does not exist".format(key))

    def __delitem__(self, key):

        # Note: assuming no collisions in raw hash output
        try:
            hash_id = self.hash_function(key)
        except TypeError:
            TypeError("Error: type {} is not hashable".format(type(key)))

        idx = hash_id % self.size

        sll = self.table[idx]
        if sll is None:
            raise KeyError("Key {} does not exist".format(key))

        success = sll.delitem(hash_id, getter=lambda x: x[0])
        if not success:
            raise KeyError("Key {} does not exist".format(key))
        else:
            self.cardinality -= 1

    def __iter__(self):
        for entry in self.table:
            if entry:
                for item in iter(entry):
                    yield (item[1], item[2])

    def __len__(self):
        return self.cardinality

    def __repr__(self):
        dict_items = ", ".join(["{!r}: {!r}".format(key, val) for
                                key, val in self])
        dict_str = "{name}({items})".format(name=self.__class__.__name__,
                                            items=dict_items)
        return dict_str

    def __str__(self):
        return self.__repr__()

    def keys(self):
        for pair in self:
            yield pair[0]

    def values(self):
        for pair in self:
            yield pair[1]

    def items(self):
        yield from self.__iter__()


#: for testing


def _main():

    print()

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

    print()


if __name__ == '__main__':

    _main()
