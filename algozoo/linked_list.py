

#: Node defs


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

    def __getitem__(self, pos):

        return self.get(pos)

    def __setitem__(self, val, pos):

        self.set(val, pos)

    def __len__(self):

        return self.count

    def __repr__(self):

        item_str = ', '.join(map(repr, self))
        repr_str = "{name}({items})".format(name=self.__class__.__name__,
                                            items=item_str)

        return repr_str

    def __str__(self):

        return repr(self)

    def get(self, pos=0):

        raise NotImplementedError()

    def set(self, val, pos=0):

        raise NotImplementedError()

    def insert(self, val, pos=0):

        raise NotImplementedError()

    def remove(self, pos=0):

        raise NotImplementedError()


class SinglyLinkedList(_base):

    def get(self, pos=0):

        if pos < 0:
            pos += self.count

        if not self.head:
            return None

        node = self.head
        ptr = 0
        while node.next and ptr < pos:
            node = node.next
            ptr += 1

        return node.val

    def set(self, val, pos=0): 

        if pos < 0:
            pos += self.count

        if not self.head:
            return None

        node = self.head
        ptr = 0
        while node.next and ptr < pos:
            node = node.next
            ptr += 1

        node.val = val

    def insert(self, val, pos=0):

        if pos < 0:
            pos += self.count + 1

        self.count += 1

        if not self.head:
            self.head = _single_node(val)
            return

        prev = None
        node = self.head
        ptr = 0
        while node and ptr < pos:
            prev = node
            node = node.next
            ptr += 1

        if prev is None:
            self.head = _single_node(val, next=node)
        else:
            prev.next = _single_node(val, next=node)

    def remove(self, pos=0):

        if pos < 0:
            pos += self.count

        if not self.head:
            return
        elif len(self) == 1:
            self.head = None

        self.count -= 1

        prev = None
        node = self.head
        ptr = 0
        while node.next and ptr < pos:
            prev = node
            node = node.next
            ptr += 1

        if prev is None:
            self.head = self.head.next
        else:
            prev.next = node.next


def DoublyLinkedList(_base):

    def get(self, pos=0):

        if not self.head:
            return None

        if pos >= 0:
            ptr = 0
            node = self.head
            while node.next and ptr < pos:
                node = node.next
                ptr += 1
        else:
            ptr = -1
            node = self.tail
            while node.prev and ptr > pos:
                node = node.prev
                ptr -= 1

        return node.val

    def set(self, val, pos=0):

        if not self.head:
            return None

        if pos >= 0:
            ptr = 0
            node = self.head
            while node.next and ptr < pos:
                node = node.next
                ptr += 1
        else:
            ptr = -1
            node = self.tail
            while node.prev and ptr > pos:
                node = node.prev
                ptr -= 1

        node.val = val

    def insert(self, val, pos=0):

        self.count += 1

        if not self.head:
            self.head = self.tail = _double_node(val)
            return

        if pos >= 0:

            prev = None
            node = self.head
            ptr = 0
            while node.next and ptr < pos:
                prev = node
                node = node.next
                ptr += 1

            if prev is None:
                self.head = _double_node(val, next=node)
                node.prev = self.head
            elif node.next:
                prev.next = _double_node(val, prev=prev, next=node)

        else:

            next = None
            node = self.tail
            ptr = -1
            while node and ptr > pos:
                next = node
                node = node.prev
                ptr -= 1

            if next is None:
                self.tail = _double_node(val, prev=node)
                node.next = self.tail
            elif node:
                node.prev.next = _double_node(val, prev=node.prev, next=next)
            else:
                self.head = _double_node(val, next=next)
                next.prev = self.head


#: for testing


def _main():

    print()

    sll = SinglyLinkedList(range(9))

    print(sll)

    sll.remove()
    sll.remove(2)

    sll.insert(-1)
    sll.insert(-2, 1)
    sll.insert(-1, 3)
    sll.insert(-1, -1)
    sll.insert(-2, sll.count - 1)
    # sll.insert(-1, sll.count)

    print(sll)
    print(sll.get())
    print(sll.get(4))
    print(sll.get(-1))

    sll.remove()
    sll.remove(-2)
    print(sll)

    print()


if __name__ == '__main__':

    _main()
