"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

# CMPT 145 Course material
# Copyright (C) 2017-2020 Michael C Horsch
# All rights reserved.
#
# This document contains resources for homework assigned to students of
# CMPT 145 and shall not be distributed without permission.  Posting this 
# file to a public or private website, or providing this file to a person 
# not registered in CMPT 145, constitutes Academic Misconduct, according 
# to the University of Saskatchewan Policy on Academic Misconduct.
# 
# Synopsis:
#    SOme functions to test.


def newtonraphson(x):
    """
    Purpose:
        Compute square root of a non-negative number.
    Pre-conditions:
        x: non-negative float or integer.
    Post-conditions:
        None.
    Return:
        Square root of x.
    """
    # Note: Docstring has been written for the original code

    # Original code
    # root = 1
    # while abs(x - root * root) > 0.00001:
    #     root = (x/root + root) / 2.0
    # return root

    # Corrected code (to fix edge case when x == 0)
    if x == 0:
        return 0.0

    root = 1
    while abs(x - root * root) > 0.00001:
        root = (x/root + root) / 2.0
    return root
 
 
def gcd(a, b):
    """
    Purpose:
        Calculate the greatest common divisor of two integers.
    Pre-conditions:
        - a: an integer.
        - b: an integer.
    Post-conditions:
        None.
    Return:
        The greatest common divisor for a and b.
    """
    # Note: Docstring has been written for the original code

    # Original code
    # while a != b:
    #     if a > b:
    #         a = a - b
    #     else:
    #         b = b - a
    # print(a)

    # Corrected code (to fix infinite loop and negative edge cases)
    a = abs(a)
    b = abs(b)

    if a == 0:
        return b
    if b == 0:
        return a

    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def read_triangle(filename):
    """
    Purpose:
        Read a triangle of integers from a file, store in nested list.
    Pre-conditions:
        filename: string representing filepath to a readable text file.
    Post-conditions:
        None.
    Return:
        Tuple containing size of triangle and a nested list, each inner list represents a level of the triangle.
    """
    file = open(filename)
    triangle = []
    for line in file:
        line = line.rstrip().split()
        line = [int(d) for d in line]
        triangle.append(line)
    file.close()
    size = triangle[0][0]
    triangle = triangle[1:]
    return (size, triangle)

def remdup(alist):
    """
    Purpose:
        Removes duplicates from list, keeps only first occurrence of each item.
    Pre-conditions:
        alist: list that can contain any types that are comparable.
    Post-conditions:
        alist is modified, and any duplicates removed.
    Return:
        None.
    """
    # Note: Docstring has been written for the original code

    # Original code
    # alist.reverse()
    # for i in range(len(alist)-1):
    #     while alist[i] in alist[i+1:]:
    #         del alist[i]
    # alist.reverse()

    # Corrected code (to fix return None)
    result = []

    for item in alist:
        if item not in result:
            result.append(item)
    return result
