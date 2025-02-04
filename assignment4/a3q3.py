"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""


class Statistics(object):
    def __init__(self):
        """
        Purpose:
            Initialize a Statistics object instance, setting up tracking for count, mean, minimum, maximum, and mode of data values.
        Pre-Conditions:
            none
        Post-Conditions:
            Initializes internal counters for count, mean, and dictionaries for tracking minimum, maximum, and mode.
        Return:
            none
        """
        self.__count = 0      # how many data values seen so far
        self.__avg = 0        # the running average so far

        # Modified code for min() and max()
        self.__max = None
        self.__min = None
        self.__values = {}

    def add(self, value):
        """
        Purpose:
            Add a new value to the statistics calculation, updating the mean, minimum, maximum, and mode accordingly.
        Pre-Conditions:
            :param value: Numerical value to be added to the statistics.
        Post-Conditions:
            Updates count, mean, and if applicable, the minimum, maximum, and mode.
        Return:
            none
        """
        self.__count += 1
        k = self.__count           # convenience
        diff = value - self.__avg  # convenience
        self.__avg += diff / k

        # Modified code for min() and max()
        if self.__max is None or value > self.__max:
            self.__max = value
        else:
            self.__max = self.__max

        if self.__min is None or value < self.__min:
            self.__min = value
        else:
            self.__min = self.__min

        # Modified code for mode()
        if value in self.__values:
            self.__values[value] += 1
        else:
            self.__values[value] = 1

    def mean(self):
        """
        Purpose:
            Return the average of all the values seen so far.
        Post-conditions:
            (none)
        Return:
            The mean of the data seen so far.
            Note: if no data has been seen, 0 is returned.
                  This is clearly false.
        """
        return self.__avg

    def count(self):
        """
        Purpose:
            Return the number of values seen so far.
        Post-conditions:
            (none)
        Return:
            The number of values seen so far.
            Note: if no data has been seen, 0 is returned.
                  This is clearly false.
        """
        return self.__count

    # range() method
    def range(self):
        """
        Purpose:
            Calculate and return the range of values added to the statistics.
        Pre-Conditions:
            none
        Post-Conditions:
            none
        Return:
            The range (max - min) of all added values. Returns None if no values have been added.
        """
        if self.__count == 0:
            return None
        return self.__max - self.__min

    # mode() method
    def mode(self):
        """
        Purpose:
            Calculate and return the mode(s) of values added to the statistics.
        Pre-Conditions:
            none
        Post-Conditions:
            none
        Return:
            The mode of all added values. If multiple modes exist, returns a tuple of modes. Returns None if no values have been added.
        """
        if self.__count == 0 or not self.__values:
            return None

        max_frequency = max(self.__values.values())
        # All values unique and added only once
        if max_frequency == 1 and len(self.__values) > 1:
            return None

        # Handles if multiple modes exist
        modes = []
        for val, frequency in self.__values.items():
            if frequency == max_frequency:
                modes.append(val)

        # Single mode
        if len(modes) == 1:
            return modes[0]
        # Multiple modes
        elif len(modes) > 1:
            return tuple(modes)

    # max() method
    def max(self):
        """
        Purpose:
            Return the maximum value added to the statistics.
        Pre-Conditions:
            none
        Post-Conditions:
            none
        Return:
            The maximum value added. Returns None if no values have been added.
        """
        return self.__max

    # min() method
    def min(self):
        """
        Purpose:
            Return the minimum value added to the statistics.
        Pre-Conditions:
            none
        Post-Conditions:
            none
        Return:
            The minimum value added. Returns None if no values have been added.
        """
        return self.__min
