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


class Stack(Container):
    """
    Purpose:
        Implements stack, inheriting attributes and methods from Container.
    Pre-conditions:
        None
    Post-conditions:
        New Stack instance is initialized with top elements set to None.
    """

    def __init__(self):
        """
        Purpose:
            Initialize a Stack instance.
        Pre-conditions:
            None
        Post-conditions:
            'self._top' set to None. Inherits '_size' from Container set to 0.
        Return:
            None
        """
        super().__init__()
        self._top = None

    def push(self, item):
        """
        Purpose:
            Add an item to top of the stack.
        Pre-conditions:
            'item': The item to be added.
        Post-conditions:
            Stack has one more item and '_size' is increased.
        Return:
            None
        """
        new_node = Node(item, self._top)
        self._top = new_node
        self._size += 1

    def pop(self):
        """
        Purpose:
            Remove and return item at top of stack.
        Pre-conditions:
            Assumes stack is not empty.
        Post-conditions:
            Stack has one less item and '_size' is decreased.
        Return:
            Item that was at the top of the stack.
        """
        if self.is_empty():
            raise IndexError("Pop from an empty stack.")
        item = self._top.get_data()
        self._top = self._top.get_next()
        self._size -= 1
        return item

    def peek(self):
        """
        Purpose:
            Return item at top of the stack without removing it.
        Pre-conditions:
            Assumes stack is not empty.
        Post-conditions:
            None
        Return:
            Item at the top of the stack.
        """
        if self.is_empty():
            raise IndexError("Peek from an empty stack.")
        return self._top.get_data()
