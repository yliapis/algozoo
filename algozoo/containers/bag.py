
#: Node def


class _bag_node:

    def __init__(self, val, hash_id):

        self.hash_id = None
        self.val = val
        self.count = 1
        self.next = None


#: Bag def


class Bag:

    def __init__(self, items=None, size=256, hash_function=hash):

        self.table = [None for _ in range(size)]
        self.hash_function = hash_function
        self.size = size
        self.cardinality = 0

        if hasattr(items, '__iter__'):
            for item in items:
                self.add(item)
        elif items is not None:
            raise Exception("items={} is not iterable".format(items))

    def __iter__(self):

        for entry in self.table:
            while entry:
                for _ in range(entry.count):
                    yield entry.val
                entry = entry.next

    def __len__(self):

        return self.cardinality

    def __repr__(self):

        bag_string = ', '.join([repr(val) for val in self])
        bag_string = 'Bag(' + bag_string + ')'

        return bag_string

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
            self.table[idx] = _bag_node(val, hash_id)
            self.cardinality += 1
        else:
            node = self.table[idx]
            while True:
                # check if value has already been added
                if node.val == val:
                    node.count += 1
                    self.cardinality += 1
                    return
                # check if there is another node in the chain
                if node.next:
                    node = node.next
                # if not, break and add it
                else:
                    break
            node.next = _bag_node(val, hash_id)
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
                if node.count > 1:
                    node.count -= 1
                else:
                    if node is root_node:
                        self.table[idx] = None
                    else:
                        prev_node.next = node.next
                self.cardinality -= 1
                return
            else:
                prev_node = node
                node = node.next

    def union(self, other_bag):

        new_bag = Bag(self)

        for val in other_bag:
            new_bag.add(val)

        return new_bag

    def difference(self, other_bag):

        new_bag = Bag(self)

        for val in other_bag:
            self.remove(val)

        return new_bag

    def intersection(self, other_bag):

        raise NotImplementedError()
        # new_bag = Bag()
        # union = self.union(self, other_bag)

        # for item in union:
        #     if item in self and item in other_bag:
        #         new_bag.add(item)

        # return new_bag

    def symmetric_difference(self, other_bag):

        raise NotImplementedError()
        # new_bag = self.union(self, other_bag)

        # for item in new_bag:
        #     if item in self and item in other_bag:
        #         new_bag.remove(item)

        # return new_bag


#: for testing


def _main():

    mybag = Bag()

    mybag.add(3)
    mybag.add(4)
    mybag.add(1234)
    mybag.add("hello")
    mybag.remove(3)

    for i in range(1000):
        mybag.add(i)

    for i in range(10):
        mybag.add(i)

    for i in range(3, 1000):
        mybag.remove(i)

    print(mybag)


if __name__ == '__main__':

    _main()
