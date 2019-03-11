

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


#: base class


class _BaseLinkedList:

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


#: class defs


class SinglyLinkedList(_BaseLinkedList):

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


class DoublyLinkedList(_BaseLinkedList):

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
            ptr = 1
            while node.next and ptr < pos:
                prev = node
                node = node.next
                ptr += 1    
        else:
            node = self.tail
            ptr = -1
            while node.prev and ptr > pos:
                node = node.prev
                ptr -= 1

        # break down into cases and insert node
        if pos == 0 or pos + self.count < 0:
             self.head = node.prev = _double_node(val, next=node)
        else:
            new_node = _double_node(val, prev=node, next=node.next)
            if node.next:
                node.next.prev = node.next = new_node
            else:
                self.tail = node.next = new_node

    def remove(self, pos=0):

        if not self.head:
            return

        self.count += -1

        # find node to be removed
        if pos >= 0:
            node = self.head
            ptr = 0
            while node.next and ptr < pos:
                node = node.next
                ptr += 1
        else:
            node = self.tail
            ptr = -1
            while node.prev and ptr > pos:
                node = node.prev
                ptr -= 1

        # break down into cases and remove node
        if node.prev and node.next:
            node.next.prev = node.prev
            node.prev.next = node.next
        elif not node.prev and node.next:
            self.head = node.next
            node.next.prev = None
        elif node.prev and not node.next:
            self.tail = node.prev
            node.prev.next = None
        else:
            self.head = self.tail = None

    def reverse(self):

        node = self.head

        head = self.head
        tail = self.tail

        while node:
            node.prev, node.next = node.next, node.prev
            node = node.prev

        self.head, self.tail = tail, head

#: for testing


def _test_sll():

    print("Testing SinglyLinkedList")

    sll = SinglyLinkedList(range(9))

    print(sll)

    sll.remove()
    sll.remove(2)

    sll.insert(-1)
    sll.insert(-2, 1)
    sll.insert(-1, 3)
    sll.insert(-1, -1)
    sll.insert(-2, sll.count - 1)
    sll.insert(-3, sll.count)

    print(sll)
    print(sll.get())
    print(sll.get(4))
    print(sll.get(-1))

    sll.remove()
    sll.remove(-2)
    print(sll, len(sll), len(list(sll)))

    print()


def debug(ll):
    print("debug", ll)
    len1 = len(ll)
    ll.reverse()
    len2 = len(ll)
    assert len1 == len2
    ll.reverse

def _test_dll():

    print("Testing DoublyLinkedList")

    dll = DoublyLinkedList(range(9))

    debug(dll)

    dll.remove()

    debug(dll)

    dll.remove(2)
    debug(dll)


    dll.insert(-1)
    debug(dll)
    dll.insert(-2, 1)
    debug(dll)
    dll.insert(-1, 3)
    debug(dll)
    dll.insert(-1, -1)
    debug(dll)
    dll.insert(-2, dll.count - 1)
    debug(dll)
    dll.insert(-3, dll.count)
    debug(dll)

    print(dll)
    print(dll.get())
    print(dll.get(4))
    print(dll.get(-1))

    dll0 = DoublyLinkedList(list(dll)[::-1])
    # print(dll, len(dll), len(list(dll)))
    dll.remove()
    # print(dll, len(dll), len(list(dll)))
    # import pdb; pdb.set_trace()
    dll.remove(-2)
    print(dll, len(dll), len(list(dll)))

    print()


def _main():

    print()

    _test_sll()
    _test_dll()

    print()


if __name__ == '__main__':

    _main()
