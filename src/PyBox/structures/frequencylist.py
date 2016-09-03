"""
frequencylist.py
Defines a frequency list class, 
which adds frequency tracking to 
the standard Python list.
"""

class FrequencyList(list):
    """
    A subclass of the Python list class; 
    Keeps track of the frequency of each 
    item in the list.
    """
    def __init__(self, members):
        super().__init__(members)

    def frequency(self):
        """Returns a dictionary containing the frequency 
        of each item, where the item is the key and 
        the value is the frequency."""
        counts = {}
        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1
        return counts