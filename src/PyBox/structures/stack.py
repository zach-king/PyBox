"""
File: stack.py
Author: Zachary King

Defines a basic stack class, which can be used
to help define future implementations 
of stacks.
"""

from collections.abc import Container

class Stack(Container):
    """A basic stack class."""
    def __init__(self, source=None):
        """Sets the initial state, and adds the initial 
        items from source if provided."""
        self._items = []
        self._index = -1
        if source:
            for item in source:
                self.add(item)

    def __contains__(self, item):
        """Returns True if item is in the stack, 
        and False otherwise."""
        # Iterate over the items, index 0 - self._index 
        # and compare them
        for elem in self._items[:self._index+1]:
            if elem == item:
                return True
        return False

    def __len__(self):
        """Returns the number of items in the stack."""
        return self._index + 1

    def __add__(self, item):
        """Returns a copy of the stack with 
        the item added to the top of the stack."""
        # Make a copy of the stack
        copy = Stack(source=self._items[:self._index])

        # Add the item to the copied Stack
        copy.add(item)

        return copy

    def __str__(self):
        """Returns a string represenation of the stack."""
        return self._items[:self._index+1].__str__()

    def pop(self):
        """Removes and returns the top item on the stack"""
        if self._index < 0:
            raise IndexError('The stack is empty.')

        # Copy the top item
        top = self._items[self._index]
        self._items[self._index] = None

        # Decrement the current index
        self._index -= 1

        # Return the copied top item
        return top

    def top(self):
        """Returns a copy of the item on the stack.
        Does not remove the item."""
        if self._index < 0:
            raise IndexError('The stack is empty.')
            
        return self._items[self._index]

    def add(self, item):
        """Adds the item to the top of the stack."""
        # Increment the current index pointer
        self._index += 1

        # Add the new item
        try:
            self._items[self._index] = item
        except IndexError: # reached the end of the list
            self._items.append(item)
