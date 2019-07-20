from LinkedList import LinkedList

class Queue(LinkedList):
    """Manages a Queue.

    Adds/Removes elements on a first in, first out (FIFO) basis.
    """

    def enqueue(self, item):
        """Adds item to the queue"""
        super().add_item_to_front(item)

    def dequeue(self):
        """Removes and returns an item from the queue
        on a FIFO basis"""
        return super().remove_item_from_back()

    def first(self):
        """Returns the first element in the Queue"""
        return super().peek_last()



if __name__ == '__main__':
    print('TESTING QUEUE')
    q = Queue()         # []
    assert(len(q) == 0)
    q.enqueue(1)        # [1]
    assert(len(q) == 1)

    q.enqueue(2)        # [2, 1]
    q.enqueue(3)        # [3, 2, 1]
    q.enqueue(4)        # [4, 3, 2, 1]
    q.enqueue('foo')    # ['foo', 4, 3, 2, 1]

    assert(q.get_size() == 5)

    assert(q.first() == 1)

    for el in q:
        print(el)

    assert(q.dequeue() == 1)    # ['foo', 4, 3, 2]
    assert(q.dequeue() == 2)    # ['foo', 4, 3]
    assert (q.get_size() == 3)

    print('nodes left:', 'foo', 4, 3)
    for el in q:
        print(el)

    print('ALL TESTS PASSED')