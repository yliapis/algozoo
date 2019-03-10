

#: Node devs


class _single_node:

    def __init__(self, val, next=None):

        self.val = val
        self.next = next


class _double_node:

    def __init__(self, val, prev=None, next=None):

        self.val = val
        self.prev = prev
        self.next = next


#: list defs


class _base:

    def __init__(self, items=None):

        self.head = None
        self.tail = None
        self.count = 0

        if hasattr(items, '__iter__'):
            for item in items:
                self.insert(item)

    def __iter__(self):

        node = self.head

        while node:
            yield node.val
            node = node.next

    def __len__(self):

        return self.count

    def __repr__(self):

        item_str = ', '.join(map(repr, self))
        repr_str = "{name}({items})".format(name=self.__class__.__name__,
                                            items=item_str)

        return repr_str

    def get(self, pos=0):

        raise NotImplementedError()

    def insert(self, val, pos=0):

        raise NotImplementedError()

    def remove(self, pos=0):

        raise NotImplementedError()


class SinglyLinkedList(_base):

    def get(self, pos=0):
        
        if pos < 0:
            raise Exception("pos={!r} must be greater than 0: ".format(pos))

        if not self.head:
            return None

        prev = None
        node = self.head
        depth = 0
        while node.next and depth < pos:
            prev = node
            node = node.next
            depth += 1

        return node.val

    def insert(self, val, pos=0):

        if pos < 0:
            raise Exception("pos={!r} must be greater than 0: ".format(pos))

        self.count += 1

        if not self.head:
            self.head = _single_node(val)
            return

        prev = None
        node = self.head
        depth = 0
        while node.next and depth < pos:
            prev = node
            node = node.next
            depth += 1

        if prev is None:
            self.head = _single_node(val, next=node)
        else:
            prev.next = _single_node(val, next=node)

    def remove(self, pos=0):

        if pos < 0:
            raise Exception("pos={!r} must be greater than 0: ".format(pos))

        if not self.head:
            return
        elif len(self) == 1:
            self.head = None

        self.count -= 1

        prev = None
        node = self.head
        depth = 0
        while node.next and depth < pos:
            prev = node
            node = node.next
            depth += 1

        if prev is None:
            self.head = self.head.next
        else:
            prev.next = node.next


def DoublyLinkedList(_base):

    pass


#: for testing


def _main():

    print()

    sll = SinglyLinkedList(range(9))

    print(sll)

    sll.remove()
    sll.remove(2)

    sll.insert(-1)
    sll.insert(-1, 3)

    print(sll)
    print(sll.get())
    print(sll.get(4))

    print()


if __name__ == '__main__':

    _main()
