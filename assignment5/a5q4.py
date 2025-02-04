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
#    Assignment 5 Question 4

import node as N
from a5q3 import to_string


def sumnc(node_chain):
    """
    Purpose:
        Given a node chain with numeric data values, calculate 
        the sum of the data values.
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty, containing 
        numeric data values
    Post-condition:
        None
    Return
        :return: the sum of the data values in the node chain
    """
    total = 0
    current = node_chain  # Starting point of node chain

    while current is not None:
        total += current.get_data()
        current = current.get_next()

    return total


def count_in(node_chain, value):
    """
    Purpose:
        Counts the number of times a value appears in a node chain
    Pre-conditions:
        :param node_chain: a node chain, possibly empty
        :param value: a data value
    Return:
        :return: The number times the value appears in the node chain
    """
    count = 0
    current = node_chain

    while current is not None:
        if current.get_data() == value:
            count += 1
        current = current.get_next()

    return count


def replace_in(node_chain, target, replacement):
    """
    Purpose:
        Replaces each occurrence of the target value with the replacement
    Pre-conditions:
        :param node_chain: a node-chain, possibly empty
        :param target: a value that might appear in the node chain
        :param replacement: the value to replace the target
    Post-conditions:
        Each occurrence of the target value in the chain is replaced with 
        the replacement value.
    Return:
        None
    """
    current = node_chain

    while current is not None:
        if current.get_data() == target:
            current.set_data(replacement)
        current = current.get_next()
