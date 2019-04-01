

class BitArray:

    def __init__(self, size=0):

        self.arr = bytearray((size >> 3) + 1)

    def __repr__(self):
        bit_str = ''.join(map(
            lambda x: bin(x)[2:], self.arr))
        repr_str = "{name}({items})".format(
            name=self.__class__.__name__, items=bit_str)
        return repr_str

    def __getitem__(self, idx):
        major = idx >> 3
        minor = idx % 8
        item = ((self.arr[major] & (1 << minor)) >> minor)
        return item

    def __setitem__(self, idx, item):
        
        # range check
        if item not in (0, 1):
            raise ValueError("item={!r} is not in "
                             "(0, 1)".format(item))
        
        major = idx >> 3
        minor = idx % 8
        val = self[major]
        bit = 1 << minor

        if item:
            val |= bit
        else:
            val = ~val
            val |= bit
            val = ~val

        self.arr[major] = val

"""
old item new

0 0 0
0 1 1
1 0 0
1 1 1

NOTE: has bugs

In [5]: a = BitArray(9)

In [6]: a
Out[6]: BitArray(00)

In [7]: a[3] = 1

In [8]: a
Out[8]: BitArray(10000)

In [9]: a[0] = 1

In [10]: a
Out[10]: BitArray(10)

In [11]: a[3] = 1

In [12]: a
Out[12]: BitArray(10010)

In [13]: a[0] = 1

In [14]: a
Out[14]: BitArray(10)

"""