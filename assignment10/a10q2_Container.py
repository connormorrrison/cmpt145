"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""


class Container:
    """
    Purpose:
        A superclass for container, providing attributes and methods.
    Pre-conditions:
        None
    Post-conditions:
        Initializes a Container instance with size attribute set to 0, ready to track number of elements.
    """

    def __init__(self):
        """
        Purpose:
            Initialize Container instance with attributes.
        Pre-conditions:
            None
        Post-conditions:
            Container size is set to 0.
        Return:
            None
        """
        self._size = 0

    def is_empty(self):
        """
        Purpose:
            Check whether container is empty.
        Pre-conditions:
            None
        Post-conditions:
            None
        Return:
            True if container is empty, False otherwise.
        """
        return self._size == 0

    def size(self):
        """
        Purpose:
            Get number of elements in the container.
        Pre-conditions:
            None
        Post-conditions:
            None
        Return:
            The number of elements in the container.
        """
        return self._size
