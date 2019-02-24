

class _dict_node:

    def __init__(self, hash_id, val, next=None):
        self.hash_id = hash_id
        self.val = val
        self.next = None


class dictionary:

    def __init__(self, size=256, hash_function=hash):

        self.table = [None for _ in range(size)]
        self.size = size
        self.hash_function = hash_function

    def __setitem__(self, key, val):

        # Note: assuming no collisions in raw hash output
        try:
            hash_id = self.hash_function(key)
        except TypeError:
            TypeError("Error: type {} is not hashable".format(type(key)))

        idx = hash_id % self.size

        if self.table[idx] is None:
            self.table[idx] = _dict_node(key, val)
        else:
            node = self.table[idx]
            while True:
                # check if value has already been added
                if node.hash_id == hash_id:
                    node.val = val
                    return
                # check if there is another node in the chain
                if node.next:
                    node = node.next
                # if not, break and add it
                else:
                    break
            node.next = _dict_node(hash_id, val)

    def __getitem__(self, key):

        # Note: assuming no collisions in raw hash output
        try:
            hash_id = self.hash_function(key)
        except TypeError:
            TypeError("Error: type {!r} is not hashable".format(key))

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
            TypeError("Error: type {!r} is not hashable".format(key))

        idx = hash_id % self.size

        if self.table[idx] is None:
            raise KeyError("Key {} does not exist".format(key))

        root_node = self.table[idx]
        node = root_node
        while node:
            if node.hash_id == hash_id:
                if node is root_node:
                    self.table[idx] = None
                    return
                else:
                    prev_node.next = node.next
            else:
                prev_node = node
                node = node.next

        raise KeyError("Key {} does not exist".format(key))


if __name__ == '__main__':

    d = dictionary()
    d[0] = 1
    print(d[0])
    d[0] = 3
    d[2] = 4
    print(d[0])
    print(d[2])
    del d[2]
