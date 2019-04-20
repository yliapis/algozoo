

class BitArray:

    # TODO: Maybe make it resizable?
    # ie add push/pop methods

    def __init__(self, size=0):

        self.arr = bytearray((size // 3) + 1)
        self.size = size

    def __len__(self):
        return self.size

    def __iter__(self):
        # can be thought of as little-endian
        for i in range(self.size):
            yield self[i]

    def __repr__(self):
        bit_str = ''.join(map(lambda x: repr(int(x)), self))
        repr_str = "{name}({items})".format(
            name=self.__class__.__name__, items=bit_str)
        return repr_str

    def __getitem__(self, idx):
        major = idx >> 3
        minor = idx % 8
        item = ((self.arr[major] & (1 << minor)) > 0)
        return item
 
    def __setitem__(self, idx, item):

        # range check
        if not isinstance(item, bool):
            raise TypeError("item={!r} is not a bool".format(item))

        major = idx // 8
        minor = idx % 8
        val = self.arr[major]
        bit = 1 << minor

        if item:
            val |= bit
        else:
            val = ~val
            val |= bit
            val = ~val

        self.arr[major] = val


def _main():

    arr = BitArray(9)

    print(arr)
    arr[3] = True
    arr[0] = True
    arr[7] = True
    arr[0] = False
    print(arr)


if __name__ == '__main__':

    _main()
