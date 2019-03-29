

from algozoo.core.heap import FiniteHeap


#: class def


class PiorityQueue:

    def __init__(self, items=None):

        self.heap = FiniteHeap(comparator=lambda pair1, pair2:
                               pair1[0] > pair2[0])

        if hasattr(items, '__iter__'):
            self.enqueue_batch(items)
        elif items is not None:
            raise ValueError("Cannot initialize {name} "
                             "with items={items!r}".format(items))

    def __len__(self):
        return len(self.heap)

    def enqueue(self, item, priority):
        self.heap.insert((priority, item))

    def enqueue_batch(self, item_pairs):
        for item, priority in item_pairs:
            self.enqueue(item, priority)

    def dequeue(self):
        return self.heap.pop()[1]

    def peak(self):
        return self.heap.peak()[0]


#: testing


def __main():

    print()

    items = [('a', 1),
             ('b', 2),
             ('c', 5),
             ('d', 3),
             ('e', 0)]

    pq = PiorityQueue()

    print("Enqueing...")
    for item, priority in items:
        print("\titem={!r}, priority={!r}".format(
                item, priority))
        pq.enqueue(item, priority)
    print()

    print("Dequeing...")
    while len(pq) > 0:
        item = pq.dequeue()
        print("\titem={!r}".format(item))

    print()


if __name__ == '__main__':

    __main()
