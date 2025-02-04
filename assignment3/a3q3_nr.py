"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

# a3q3_nr.py

import a3q3

# Test cases
newtonraphson_tests = [
    {
        "input": [0.04],
        "expected": 0.2,
        "reason": "Square root of a smaller number between 0 and 1."
    },
    {
        "input": [0.81],
        "expected": 0.9,
        "reason": "Square root of a larger number between 0 and 1."
    },
    {
        "input": [16],
        "expected": 4.0,
        "reason": "Square root of a number greater than 1."
    },
    {
        "input": [1],
        "expected": 1.0,
        "reason": "Square root of 1."
    },
    {
        "input": [0],
        "expected": 0.0,
        "reason": "Square root of 0."
    },
]

# Test driver
for testcase in newtonraphson_tests:
    input = testcase['input']
    expected = testcase['expected']
    result = a3q3.newtonraphson(*input)
    if result != expected:
        print('Error: returned', result,
              'when given', input,
              'Reason:', testcase['reason'])
