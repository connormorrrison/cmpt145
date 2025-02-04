"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

from a10q2_Container import Container
from node import Node


class Queue(Container):
    """
    Purpose:
        Implements queue, inheriting attributes and methods from Container.
    Pre-conditions:
        None
    Post-conditions:
        New Queue instance is initialized with front and rear elements set to None.
    """

    def __init__(self):
        """
        Purpose:
            Initialize a Queue instance.
        Pre-conditions:
            None
        Post-conditions:
            'self._front' and 'self._rear' are set to None. Inherits '_size' from Container set to 0.
        Return:
            None
        """
        super().__init__()
        self._front = None
        self._rear = None

    def enqueue(self, item):
        """
        Purpose:
            Add item to rear of the queue.
        Pre-conditions:
            'item': Item to be added.
        Post-conditions:
            Queue has one more item and '_size' is increased.
        Return:
            None
        """
        new_node = Node(item, None)
        if self.is_empty():
            self._front = self._rear = new_node
        else:
            self._rear.set_next(new_node)
            self._rear = new_node
        self._size += 1

    def dequeue(self):
        """
        Purpose:
            Remove and return item from front of queue.
        Pre-conditions:
            Assumes queue is not empty.
        Post-conditions:
            Queue has one less item and '_size' is reduced.
        Return:
            Item that was at front of the queue.
        """
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue.")
        item = self._front.get_data()
        self._front = self._front.get_next()
        if self._front is None:
            self._rear = None
        self._size -= 1
        return item

    def peek(self):
        """
        Purpose:
            Return item at front of the queue without removing it.
        Pre-conditions:
            Assumes queue is not empty.
        Post-conditions:
            None
        Return:
            Item at front of the queue.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty queue.")
        return self._front.get_data()
