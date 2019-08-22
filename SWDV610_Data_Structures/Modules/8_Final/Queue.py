class Queue:
    """A Queue that uses a LinkedList as the underlying data structure

    first in, first out

    Public methods:
    get_size - returns the size of the queue
    enqueue - adds an item to the queue
    dequeue - removes an item from the queue

    Example:
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.dequeue() => 1
    """

    class LinkedList:
        """A Doubly Linked List

        Public methods:
        pop_first - removes the head element
        pop_last - removes the tail element
        push_first = adds an element to the beginning of the list
        push_last - adds an element to the end of the list
        """

        class Node:
            """A Node used in the Linked List

            Keeps track of the next and previous elements in the list
            """
            def __init__(self, element, next=None, previous=None):
                """Initializes a new Node"""
                self.element = element
                self.next = next
                self.previous = previous

        def __len__(self):
            """Returns the size of the queue"""
            return self.size

        def __iter__(self):
            """An iterator to iterate over all elments in the list starting with the head element"""
            if self.size > 0:
                next_node = self.head
                yield next_node.element
                while next_node.next:
                    next_node = next_node.next
                    yield next_node.element

        def __init__(self):
            """Initializes an empty list"""
            self.head = None
            self.tail = None
            self.size = 0

        def pop_first(self):
            """Removes the head item from the list"""
            if self.size > 0:
                old_head = self.head
                if self.size == 1:
                    self.tail = None
                    self.head = None
                else:
                    self.head = old_head.next
                    self.head.previous = None
                self.size -= 1
                return old_head.element
            else:
                return None

        def pop_last(self):
            """Removes the last item from the list"""
            if self.size > 0:
                old_tail = self.tail
                if self.size == 1:
                    self.tail = None
                    self.head = None
                else:
                    self.tail = old_tail.previous
                    self.tail.next = None
                self.size -= 1
                return old_tail.element
            else:
                return None

        def push_first(self, element):
            """Adds to the front of the list"""
            if self.size == 0:
                self.head = self.Node(element)
                self.tail = self.head
            else:
                prev_head = self.head
                self.head = self.Node(element, prev_head, None)
                prev_head.previous = self.head
            self.size += 1

        def push_last(self, element):
            """Adds to the end of the list"""
            if self.size == 0:
                self.head = self.Node(element)
                self.tail = self.head
            else:
                prev_tail = self.tail
                self.tail = self.Node(element, None, prev_tail)
                prev_tail.next = self.tail
            self.size += 1

    def __iter__(self):
        """An iterator to iterate over all elments on the queue"""
        return self.queue.__iter__()

    def __len__(self):
        """Retruns the size of the Queue"""
        return self.get_size()

    def __init__(self):
        """Initializes an empty queue"""
        self.queue = self.LinkedList()

    def get_size(self):
        """Returns the size of the queue"""
        return self.queue.size

    def enqueue(self, item):
        """Adds an item to the queue"""
        self.queue.push_last(item)

    def dequeue(self):
        """Removes an item from the queue"""
        return self.queue.pop_first()


if __name__ == '__main__':

    # Tests for the LinkedList
    l = Queue.LinkedList()
    l.push_last(1)
    l.push_last(2)
    l.push_last(3)
    l.push_last(4)
    assert l.size == 4
    assert l.pop_last() == 4
    assert l.pop_last() == 3
    assert l.pop_last() == 2
    assert l.pop_last() == 1
    assert l.pop_last() == None
    l.push_last(1)
    l.push_last(2)
    assert l.size == 2
    l.push_last(3)
    l.push_last(4)
    assert l.size == 4
    assert l.pop_first() == 1
    assert l.pop_first() == 2
    assert l.pop_first() == 3
    assert l.pop_first() == 4

    l.push_first(1)
    l.push_first(2)
    l.push_first(3)
    assert l.head.element == 3
    assert l.tail.element == 1

    assert l.pop_first() == 3
    assert l.pop_last() == 1

    l.push_last(4)
    assert l.pop_last() == 4
    assert l.size == 1
    assert l.pop_first() == 2
    assert l.pop_first() == None
    assert l.pop_last() == None
    assert l.size == 0

    # Tests for the Queue
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    assert q.get_size() == 5
    assert len(q) == 5
    assert q.dequeue() == 1
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.dequeue() == 4
    assert q.dequeue() == 5

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    i = 1
    for el in q:
        assert i == el
        i += 1