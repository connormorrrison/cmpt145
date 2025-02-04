"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

import LocationNode as LN


class MobilityProfile(object):
    def __init__(self, aList=None):
        """
        Purpose: creates a mobility profile. If no aList is given, profile is set to None
        Pre-condition:
            aList: A list of five strings, showing the sequential locations that the user had visited.
        Post-condition: A mobility profile is created
        Return: None
        """
        self.profile = None
        if aList:
            self.create_profile(aList)

    def create_profile(self, aList):
        """
        Purpose:
            Creates a mobility profile using the given aList 
        Pre-conditions:
            aList: A list of five strings, showing the sequential locations that the user had visited. 
            aList should only have five locations.
        Post-condition:
            A mobility profile is created
        Return: None
        """
        if len(aList) != 5:
            raise ValueError("Profile list must contain exactly five locations.")
        self.profile = LN.LocationNode(aList[0])
        current_node = self.profile
        for location in aList[1:]:
            next_node = LN.LocationNode(location)
            current_node.set_next_location(next_node)
            current_node = next_node

    def compare_profile(self, otherProfile):
        """
        Purpose:
            Compare two mobility profiles. Return True when the two mobility profile as a location matched.
        Pre-conditions:
            otherProfile: Another user's mobility profile for comparison.
            Both self and other profiles must not be None.
        Post-condition:
            None
        Return: True if there is a match, False for otherwise.
        """
        if self.profile is None or otherProfile.profile is None:
            raise ValueError("Both profiles must be created before comparison.")
        self_current = self.profile
        other_current = otherProfile.profile

        while self_current is not None and other_current is not None:
            if self_current.get_current_location() == other_current.get_current_location():
                return True
            self_current = self_current.get_next_location()
            other_current = other_current.get_next_location()

        return False
