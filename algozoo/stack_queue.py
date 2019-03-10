

#: Base class


class _base:

    def __init__(self, items=None):

        if items is None:
            self.buffer = []
        elif hasattr(items, '__iter__'):
            self.buffer = [item for item in items]
        else:
            raise Exception("items {!r} are not iterable".format(items))

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

    def _push_start(self, val):

        self.buffer = [val] + self.buffer

    def _push_end(self, val):

        self.buffer.append(val)

    def _pop_start(self):

        if self.buffer:
            return self.buffer.pop(0)
        else:
            return None

    def _pop_end(self):

        if self.buffer:
            return self.buffer.pop()
        else:
            return None

    def _peak_start(self):

        if self.buffer:
            return self.buffer[0]
        else:
            return None

    def peak_end(self):

        if self.buffer:
            return self.buffer[-1]
        else:
            return None


#: class defs


class Dequeue(_base):

    def peak_start(self):
        return self._peak_start()

    def peak_end(self):
        return self._peak_end()

    def pop_start(self):
        return self._pop_start()

    def pop_end(self):
        return self._pop_end()

    def push_start(self, val):
        self._push_start(val)

    def push_end(self, val):
        self._push_end(val)


class Stack(_base):

    def push(self, val):
        self._push_end(val)

    def pop(self):
        return self._pop_end()

    def peak(self):
        return self._peak_end()


class Queue(_base):

    def enqueue(self, val):
        self._push_end(val)

    def dequeue(self, val):
        return self._pop_start()

    def peak(self):
        return self._peak_start()


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
