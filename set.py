

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

    def __str__(self):

        set_entries = []

        for entry in self.table:
            while entry:
                set_entries.append(str(entry.val))
                entry = entry.next

        set_string = ', '.join(set_entries)
        set_string = '{' + set_string + '}'

        return set_string

    def add(self, val):

        # Note: assuming no collisions in raw hash output
        try:
            hash_id = self.hash_function(val)
        except TypeError:
            TypeError("Error: type {} is not hashable".format(type(val)))

        idx = hash_id % self.size

        if self.table[idx] is None:
            self.table[idx] = _set_node(val, hash_id)
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


if __name__ == '__main__':

    myset = UnorderedSet()

    myset.add(3)
    myset.add(4)
    myset.add(1234)
    myset.add("hello")

    print(myset)
