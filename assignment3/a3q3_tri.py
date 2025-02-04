"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

# a3q3_tri.py

import a3q3

# Test cases
read_triangle_tests = [
    {
        "input": "triangle1.txt",
        "expected": (7, [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1],
            [1, 5, 10, 10, 5, 1],
            [1, 6, 15, 20, 15, 6, 1]
        ]),
        "reason": "Pascal's triangle with 7 levels."
    },
    {
        "input": "triangle2.txt",
        "expected": (5, [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]),
        "reason": "Pascal's triangle with 5 levels."
    },
    {
        "input": "triangle3.txt",
        "expected": (2, [
            [1],
            [1, 1]
        ]),
        "reason": "Pascal's triangle with 2 levels."
    },
    {
        "input": "triangle4.txt",
        "expected": (3, [
            [1],
            [2, 3],
            [4, 5, 6]
        ]),
        "reason": "Pascal's triangle with 3 levels."
    },
    {
        "input": "triangle5.txt",
        "expected": (4, [
            [1],
            [1, 2],
            [1, 3, 3],
            [1, 4, 6, 4]
        ]),
        "reason": "Pascal's triangle with 4 levels."
    }
]

# Test driver
for testcase in read_triangle_tests:
    input = testcase['input']
    expected = testcase['expected']
    result = a3q3.read_triangle(input)
    if result != expected:
        print('Error: returned', result,
              'when given', input,
              'Reason:', testcase['reason'])
