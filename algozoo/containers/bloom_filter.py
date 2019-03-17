

from math import ceil, log


#: class def


class BloomFilter:

    def __init__(self, items=None, size=128, k=1):

        self.table = bytearray(size)
        self.size = size

        if k < 1:
            raise Exception("Error: you must have at least 1"
                            "hash function, and k={k} was"
                            "specified".format(k=k))
        self.k = k

        if hasattr(items, '__iter__'):
            for item in items:
                self.add(item)
        elif items is not None:
            raise Exception("items={} is not iterable".format(items))

    def _hash(self, val):
        return hash(str(val))

    def _get_bit_list(self, val):

        hashes = [hash(val)]
        for i in range(self.k - 1):
            hashes.append(self._hash(hashes[i]))

        bit_list = []
        for hash_id in hashes:
            idx = hash_id % (self.size << 3)
            table_idx = idx >> 3
            bit = 1 << (idx & 7)  # 7 = b'111'
            bit_list.append((table_idx, bit))

        return bit_list

    @classmethod
    def from_specification(cls, p=0.01, N=1024):
        """Instantiate bloom filter from expected number
        of elements `N` and desired false positive rate `p`
        """
        # initially, compute optimal size and k
        size = int(ceil((-N * log(p)) / (log(2) ** 2)))
        k = int(ceil(-log(p, 2)))
        # initialize self
        self = cls(size=size, k=k)
        return self

    def add(self, val):

        bit_list = self._get_bit_list(val)

        for idx, bit in bit_list:
            self.table[idx] |= bit

    def __contains__(self, val):

        bit_list = self._get_bit_list(val)

        for idx, bit in bit_list:
            if not self.table[idx] & bit:
                return False
        return True


#: testing


def _main():

    print()
    print("Testing Bloom Filter")

    bf = BloomFilter(k=3)

    for i in range(3, 8):
        print("Adding {val}".format(val=i))
        bf.add(i)

    print()

    for i in range(10):
        msg = "" if i in bf else "not "
        print("{val} is {msg}in set".format(val=i, msg=msg))

    print()
    print(bf)

    print()


if __name__ == '__main__':

    _main()
