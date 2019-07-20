from LinkedList import LinkedList


class Deque(LinkedList):
    """Manages a Deque

    Elements can be added/removed from both the front
    and the back of the Deque.
    """

    def add_first(self, item):
        """Add item to the front of the deque"""
        super().add_item_to_front(item)

    def add_last(self, item):
        """Add item to the back of the deque"""
        super().add_item_to_back(item)

    def delete_first(self):
        """Removes and return the first element
        from the deque"""
        return super().remove_item_from_front()

    def delete_last(self):
        """Removes and return the last element
        from the deque"""
        return super().remove_item_from_back()

    def first(self):
        """Returns the first element in the Deque"""
        return super().peek()

    def last(self):
        """Returns the last element in the Deque"""
        return super().peek_last()


if __name__ == '__main__':
    print('TESTING DEQUE')
    d = Deque()     # []

    d.add_first(1)  # [1]
    d.add_first(2)  # [2, 1]
    assert(d.first() == 2)
    d.add_last(3)   # [2, 1, 3]
    assert(d.last() == 3)

    assert(d.get_size() == 3)

    for el in d:
        print(el)

    assert(d.delete_last() == 3)    # [2, 1]
    assert(d.get_size() == 2)

    assert(d.delete_first() == 2)   # [1]

    assert(d.peek() == 1)

    d.add_last('foo')       # [1, 'foo']
    d.add_first('bar')      # ['bar', 1, 'foo']
    d.add_first('baz')      # ['baz', 'bar', 1, 'foo']

    d.delete_first()        # ['bar', 1, 'foo']
    assert(len(d) == 3)

    print('nodes left:', 'bar', 1, 'foo')
    for el in d:
        print(el)

    print('ALL TESTS PASSED')