from LinkedList import LinkedList


class Stack(LinkedList):
    """Manages a stack.

    Adds/Removes elements on a list in, first out (LIFO) basis.
    """

    def push(self, item):
        """Adds an item to the stack"""
        super().add_item_to_front(item)

    def pop(self):
        """Removes and returns an item for the stack
        on a LIFO basis"""
        return super().remove_item_from_front()

    def top(self):
        """Returns the element at the top of the stack"""
        return super().peek()


if __name__ == '__main__':
    print('TESTING STACK')
    s = Stack()         # []
    assert(s.is_empty() == True)
    assert(len(s) == 0)
    s.push(1)           # [1]
    assert(len(s) == 1)
    assert(s.peek() == 1)
    assert(s.peek_last() == 1)
    s.push(2)           # [2, 1]
    s.push('foo')       # ['foo', 2, 1]
    s.push('bar')       # ['bar', 'foo', 2, 1]
    s.push(True)        # [True, 'bar', 'foo', 2, 1]

    print('top:', s.top())

    for el in s:
        print(el)

    assert(s.peek_last() == 1)
    assert(s.get_size() == 5)
    s.pop()                         # ['bar', 'foo', 2, 1]
    popped = s.pop()                # ['foo', 2, 1]
    print('popped:', popped)        # 'bar'
    assert (s.get_size() == 3)

    print('nodes left:', 'foo', 2, 1)
    for el in s:
        print(el)

    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    assert(len(s) == 0)

    for stackEl in s:
        raise Exception('Stack is empty, should not have entered loop')

    print('ALL TESTS PASSED')