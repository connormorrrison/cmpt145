"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

# a3q3_gcd.py

import a3q3

# Test cases
gcd_tests = [
    {
        "input": (27, 6),
        "expected": 3,
        "reason": "Standard case with a > b."
    },
    {
        "input": (17, 13),
        "expected": 1,
        "reason": "Standard case with b > a."
    },
    {
        "input": (5, 5),
        "expected": 5,
        "reason": "Boundary case with a = b."
    },
    {
        "input": (0, 0),
        "expected": 0,
        "reason": "Both numbers are zero."
    },
    {
        "input": (0, 5),
        "expected": 5,
        "reason": "Boundary case with a = 0."
    },
    {
        "input": (5, 0),
        "expected": 5,
        "reason": "Boundary case with b = 0."
    },
    {
        "input": (-27, 6),
        "expected": 3,
        "reason": "Negative number as input a."
    },
    {
        "input": (27, -6),
        "expected": 3,
        "reason": "Negative number as input b."
    },
    {
        "input": (-27, -6),
        "expected": 3,
        "reason": "Both a and b are negative."
    }
]

# Test driver
for testcase in gcd_tests:
    input = testcase['input']
    expected = testcase['expected']
    result = a3q3.gcd(*input)
    if result != expected:
        print('Error: returned', result,
              'when given', input,
              'Reason:', testcase['reason'])
