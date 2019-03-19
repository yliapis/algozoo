

from math import ceil, log
from math import e as euler


if __name__ == '__main__':
    import random
    from collections import Counter


class CountMinSketch:

    def __init__(self, w=None, d=None):

        if w is None:
            raise Exception
        if d is None:
            raise Exception

        self.w = w  # rows
        self.d = d  # columns

        self.table = [[0 for _ in range(d)] for _ in range(w)]
        self.size = 0

    def _hash(self, val, j):
        return hash(str(hash(val)) + str(j))

    @classmethod
    def from_specification(cls, epsilon=0.01, error=0.01):
        w = ceil(euler / epsilon)
        d = ceil(log(1 / error))
        return cls(w=w, d=d)

    def update(self, item):
        self.size += 1
        for j in range(self.w):
            k = self._hash(item, j) % self.d
            self.table[j][k] += 1

    def batch_update(self, items):
        for item in items:
            self.update(item)

    def count(self, item):
        counts = []
        for j in range(self.w):
            k = self._hash(item, j) % self.d
            counts.append(self.table[j][k])
        return min(counts)


#: testing


def __main():

    print()

    N = 1000000  # 1 million

    items = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

    probs = {1: 1 / 10,
             2: 2 / 10,
             3: 3 / 10,
             4: 4 / 10}

    data = [random.choice(items) for _ in range(N)]

    cms = CountMinSketch.from_specification(0.10, 0.10)
    cms.batch_update(data)

    unique = set(items)

    counter = Counter(data)
    for item in unique:
        count = counter[item]
        print("item: {item}\n"
              "exp. p(item): {exp}\n"
              "true p(item): {true}\n"
              "est. p(item): {est}\n".format(
                item=item, exp=probs[item], true=count/N,
                est=cms.count(item)/cms.size))

    print()


if __name__ == '__main__':

    __main()
