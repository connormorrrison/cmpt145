"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

# CMPT 145 Course material
# Copyright (c) 2017-2024 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this
# file to a public or private website, or providing this file to a person
# not registered in CMPT 145, constitutes Academic Misconduct, according
# to the University of Saskatchewan Policy on Academic Misconduct.
#
# Synopsis:
#    Assignment 5 Question 3

import node as N

def to_string(node_chain):
    """
    Purpose:
        Create a string representation of the node chain.  E.g.,
        [ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]
    Pre-conditions:
        :param node_chain:  A node-chain, possibly empty (None)
    Post_conditions:
        None
    Return: A string representation of the nodes.
        NOTE: THIS VERSION OF THE FUNCTION IS KNOWN TO BE BROKEN!!!
    """
    # special case: empty node chain
    if node_chain is None:
        return 'EMPTY'
    else:
        result = ''
        walker = node_chain
        while walker is not None:
            value = walker.get_data()
            if walker.get_next() is not None:
                # for nodes that are not at the end
                result += '[ {} | *-]-->'.format(str(value))
            else:
                # for the last node
                result += '[ {} | / ]'.format(str(value))
            walker = walker.get_next()

        return result
