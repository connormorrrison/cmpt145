"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

import Statistics as S


def close_enough(a, b, tolerance=0.0001):
    """
    Purpose:
        Determine if two floating point numbers are close enough to each other.
    Pre-Conditions:
        :param a: a floating point value
        :param b: a floating point value
        :param tolerance: a small positive floating point value
    Post-Conditions:
        none
    Return:
        :return: True if a and b are within tolerance of each other, False otherwise.
    """
    return abs(a - b) < tolerance


# Test adding multiple values and checking mean
def test_add_and_mean_multiple_values():
    """
    Purpose:
        Test add() and mean() functions with multiple values.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated mean does not match expected mean.
    Return:
        none
    """
    test_item = 'add() + mean()'
    reason = "Adding multiple values and checking for correct mean calculation"
    stats = S.Statistics()
    values = [1, 2, 3, 4, 5]
    expected = sum(values) / len(values)
    for value in values:
        stats.add(value)
    result = stats.mean()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test adding a large quantity of values and checking mean
def test_add_and_mean_large_quantity():
    """
    Purpose:
        Test add() and mean() functions with a large quantity of values.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated mean does not match expected mean for a large set of values.
    Return:
        none
    """
    test_item = 'add() + mean()'
    reason = "Adding a large quantity of values and checking for correct mean"
    stats = S.Statistics()
    values = [1] * 10000
    expected = sum(values) / len(values)
    for value in values:
        stats.add(value)
    result = stats.mean()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test adding zero and checking mean
def test_add_and_mean_with_zero():
    """
    Purpose:
        Test add() and mean() functions with all zero values.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated mean is not zero.
    Return:
        none
    """
    test_item = 'add() + mean()'
    reason = "Adding zeros and checking if mean is calculated as zero"
    stats = S.Statistics()
    values = [0, 0, 0]
    expected = sum(values) / len(values)
    for value in values:
        stats.add(value)
    result = stats.mean()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test mean with negative values
def test_mean_negative_values():
    """
    Purpose:
        Test mean() function with negative values.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated mean does not match expected mean with negative values.
    Return:
        none
    """
    test_item = 'add() + mean()'
    reason = "Checking mean calculation with negative values"
    stats = S.Statistics()
    values = [-5, -4, -3, -2, -1]
    expected = sum(values) / len(values)
    for value in values:
        stats.add(value)
    result = stats.mean()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test mean with floating-point values
def test_mean_floating_point_values():
    """
    Purpose:
        Test mean() function with floating-point values.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated mean does not match expected mean with floating-point values.
    Return:
        none
    """
    test_item = 'add() + mean()'
    reason = "Checking mean calculation with floating-point values"
    stats = S.Statistics()
    values = [0.1, 0.2, 0.3]
    expected = sum(values) / len(values)
    for value in values:
        stats.add(value)
    result = stats.mean()
    if not close_enough(result, expected):
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test mean with no values
def test_mean_no_values():
    """
    Purpose:
        Test mean() function with no values added to ensure it returns correct default value.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if mean is not the expected value when no values are added.
    Return:
        none
    """
    test_item = 'mean()'
    reason = "Ensuring mean is zero when no values are added"
    stats = S.Statistics()
    expected = 0
    result = stats.mean()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test mean with mixed positive and negative floating-point values
def test_mean_mixed_floating_point_values():
    """
    Purpose:
        Test mean() function with a mix of positive and negative floating-point values.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated mean does not match expected mean with mixed floating-point values.
    Return:
        none
    """
    test_item = 'add() + mean()'
    reason = "Checking mean calculation with a mix of positive and negative floating-point values"
    stats = S.Statistics()
    values = [-0.5, 0.2, -0.3]
    expected = sum(values) / len(values)
    for value in values:
        stats.add(value)
    result = stats.mean()
    if not close_enough(result, expected):
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test driver
if __name__ == "__main__":
    """
    Purpose:
        Driver function to execute all test cases.
    Pre-Conditions:
        none
    Post-Conditions:
        Executes all test functions and prints completion message.
    Return:
        none
    """
    test_add_and_mean_multiple_values()
    test_add_and_mean_large_quantity()
    test_add_and_mean_with_zero()
    test_mean_negative_values()
    test_mean_floating_point_values()
    test_mean_no_values()
    test_mean_mixed_floating_point_values()
    print('*** Test script completed ***')
