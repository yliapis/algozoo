
from algozoo.core.linked_list import DoublyLinkedList, SinglyLinkedList


#: Base class


class _BaseDequeue:

    _buffer_factory = None

    def __init__(self, items=None):
        if items is None:
            self.buffer = self._buffer_factory()
        elif hasattr(items, '__iter__'):
            self.buffer = [item for item in items]
        else:
            raise Exception("items {!r} are not iterable".format(items))

    def __contains__(self, val):
        return val in self.buffer

    def __iter__(self):
        for item in self.buffer:
            yield item

    def __len__(self):
        return len(self.buffer)

    def __repr__(self):
        item_str = ', '.join(map(repr, self.buffer))
        repr_str = "{name}({items})".format(name=self.__class__.__name__,
                                            items=item_str)
        return repr_str


#: class defs


class Dequeue(_BaseDequeue):

    _buffer_factory = DoublyLinkedList

    def peak_start(self):
        return self.buffer.get(0)

    def peak_end(self):
        return self.buffer.get(-1)

    def pop_start(self):
        val = self.buffer.get(0)
        self.buffer.remove(0)
        return val

    def pop_end(self):
        val = self.buffer.get(-1)
        self.buffer.remove(-1)
        return val

    def push_start(self, val):
        self.buffer.insert(val, 0)

    def push_end(self, val):
        self.buffer.insert(val, -1)


class Stack(_BaseDequeue):

    _buffer_factory = SinglyLinkedList

    def push(self, val):
        self.buffer.insert(val, 0)

    def pop(self):
        val = self.buffer.get(0)
        self.buffer.remove(0)
        return val

    def peak(self):
        return self.buffer.get(0)


class Queue(_BaseDequeue):

    _buffer_factory = DoublyLinkedList

    def enqueue(self, val):
        self.buffer.insert(val, 0)

    def dequeue(self, val):
        val = self.buffer.get(-1)
        self.buffer.remove(-1)
        return val

    def peak(self):
        return self.buffer.get(-1)


#: for testing


def _main():

    dequeue = Dequeue()
    N = 16

    print()
    print("Generating Dequeue of size {N}".format(N=N))

    for i in range(N):
        if i % 2:
            dequeue.push_start(i)
        else:
            dequeue.push_end(i)

    print(" " * 4, dequeue)

    first = 4
    last = 8

    print()
    print("Popping first {first}".format(first=first))
    for i in range(first):
        dequeue.pop_start()
    print(" " * 4, dequeue)

    print()
    print("Popping last {last}".format(last=last))
    for i in range(last):
        dequeue.pop_end()
    print(" " * 4, dequeue)

    print()


if __name__ == "__main__":

    _main()
