"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

# a3q3_dup.py

import a3q3

# Test cases
remdup_tests = [
    {
        "input": [],
        "expected": [],
        "reason": "Boundary case with empty list."
    },
    {
        "input": [1, 2, 3],
        "expected": [1, 2, 3],
        "reason": "No duplicates."
    },
    {
        "input": [1, 2, 3, 1],
        "expected": [1, 2, 3],
        "reason": "One duplicated item."
    },
    {
        "input": [1, 2, 2, 2, 3],
        "expected": [1, 2, 3],
        "reason": "One duplicated item with sequential duplicates."
    },
    {
        "input": [1, 2, 1, 3, 2, 3],
        "expected": [1, 2, 3],
        "reason": "Multiple duplicated items appearing anywhere in the list."
    },
]

# Test driver
for testcase in remdup_tests:
    input = testcase['input']
    expected = testcase['expected']
    result = a3q3.remdup(input)
    if result != expected:
        print('Error: returned', result,
              'when given', input,
              'Reason:', testcase['reason'])
