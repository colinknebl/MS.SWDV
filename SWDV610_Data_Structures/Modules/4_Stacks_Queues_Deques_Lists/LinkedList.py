class LinkedList:
    """An ADT for managing a linked list."""

    class _Node:
        """A class for managing the links between

        the different nodes in the Linked List.
        """

        def __init__(self, value, next_node, prev_node):
            """Creates a node instance

            Sets the value of the nodes, and establishes the
            next and previous links for the Linked List"""
            self._value = value
            self._next = next_node
            self._prev = prev_node

        def get_value(self):
            """Returns the value of the node."""
            return self._value

        def set_next(self, next):
            """Sets the next node in the Linked List"""
            self._next = next

        def get_next(self):
            """Returns the next node in the Linked List"""
            return self._next

        def set_prev(self, prev):
            """Sets the previous node in the Linked List"""
            self._prev = prev

        def get_prev(self):
            """Returns the previous node in the Linked List"""
            return self._prev

    def __init__(self):
        """Creates an empty Linked List with sentinels at the head and tail of the list."""
        self._head = self._Node('head sentinel', None, None)        # head sentinel
        self._tail = self._Node('tail sentinel', self._head, None)  # tail sentinel
        self._head.set_prev(self._tail)
        self._size = 0

    def __iter__(self):
        """Iterates through each element in the Linked List excluding the sentinels"""
        if self._size > 0:
            node = self._head.get_prev()
            yield node.get_value()
            for i in range(self._size - 1):
                node = node.get_prev()
                yield node.get_value()

    def __len__(self):
        """Returns the size of the Linked List."""
        return self._size

    def get_size(self):
        """Returns the size of the Linked List."""
        return len(self)

    def is_empty(self):
        """Return True if the list is empty, otherwise False"""
        return self.get_size() == 0

    def peek(self):
        """Returns the node at the front of the Linked List"""
        return self._head.get_prev().get_value()

    def peek_last(self):
        """Returns the node at the back of the Linked List"""
        return self._tail.get_next().get_value()

    def _insert_between(self, prev, item, next):
        """Inserts a node between two nodes"""
        return self._Node(item, next, prev)

    def add_item_to_front(self, item):
        """Adds an item to the front of a Linked List"""
        if self._size == 0:
            prev = self._tail
        else:
            prev = self._head.get_prev()

        new_node = self._insert_between(prev, item, self._head)

        self._head.set_prev(new_node)
        prev.set_next(new_node)
        self._size += 1
        return new_node

    def add_item_to_back(self, item):
        """Adds an item to the back of a Linked List"""
        if self._size == 0:
            next = self._head
        else:
            next = self._tail.get_next()

        new_node = self._insert_between(self._tail, item, next)

        self._tail.set_next(new_node)
        next.set_prev(new_node)
        self._size += 1
        return new_node

    def _remove_between(self, prev, next):
        """Updates the links of two nodes effectively removing
        the node in between from the Linked List"""
        prev.set_next(next)
        next.set_prev(prev)
        self._size -= 1

    def remove_item_from_front(self):
        """Removes the node at the front of the Linked List"""
        removed = None
        if self._size > 0:
            removed = self._head.get_prev()
            self._remove_between(removed.get_prev(), self._head)
        return removed.get_value() if removed else None

    def remove_item_from_back(self):
        """Removes the node at the back of the Linked List """
        removed = None
        if self._size > 0:
            removed = self._tail.get_next()
            self._remove_between(self._tail, removed.get_next())
        return removed.get_value()


if __name__ == '__main__':
    print('TESTING LINKED LIST')
    l = LinkedList()            # []
    assert(l.is_empty() == True)
    assert(l._head.get_value() == 'head sentinel')
    assert(l._tail.get_value() == 'tail sentinel')

    l.add_item_to_front(0)      # [0]
    l.add_item_to_front(1)      # [1, 0]
    l.add_item_to_front(2)      # [2, 1, 0]
    l.add_item_to_front('foo')  # ['foo', 2, 1, 0]

    assert (l.is_empty() == False)
    assert(l.peek() == 'foo')
    assert(l.peek_last() == 0)

    assert(l.get_size() == 4)
    assert(len(l) == 4)

    for el in l:
        print(el)

    assert(l.remove_item_from_front() == 'foo')
    assert(len(l) == 3)
    assert(l.remove_item_from_front() == 2)

    print('nodes left:', 1, 0)
    for el in l:
        print(el)

    print('ALL TESTS PASSED')