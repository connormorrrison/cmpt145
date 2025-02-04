"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

import a3q3 as S


def close_enough(a, b, tolerance=0.0001):
    """
    Purpose:
        Check if 2 floating point values are close enough to be considered equal.
    Pre-Conditions:
        :param a: a floating point value
        :param b: a floating point value
        :param tolerance: a small positive floating point value
    Post-Conditions:
        none
    Return:
        :return: True if the difference between a and b is small
    """
    return abs(a - b) < tolerance


##### Existing tests #####

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


##### New tests #####

# Testing range() by adding no values
def test_range_no_values():
    """
    Purpose:
        Verify range() method returns None when no values have been added.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated range and expected range do not match with no values added.
    Return:
        none
    """
    test_item = 'range()'
    reason = "Expect None when no values have been added"
    stats = S.Statistics()
    expected = None
    result = stats.range()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Testing range() by adding a single value
def test_range_single_value():
    """
    Purpose:
        Test that range() method returns 0 when only a single value has been added.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated range and expected range do not match with single value added.
    Return:
        none
    """
    test_item = 'range()'
    reason = "Expect 0 range with a single value"
    stats = S.Statistics()
    stats.add(5)
    expected = 0
    result = stats.range()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Testing range() by adding only identical values
def test_range_identical_values():
    """
    Purpose:
        Confirm range() method returns 0 when all added values are identical.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated range and expected range do not match with identical values added.
    Return:
        none
    """
    test_item = 'range()'
    reason = "Expect 0 range with identical values"
    stats = S.Statistics()
    values = [4, 4, 4, 4]
    for value in values:
        stats.add(value)
    expected = 0
    result = stats.range()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Testing range with mix of positive and negative values
def test_range_positive_negative():
    """
    Purpose:
        Test range() method's ability to calculate range correctly with a mix of positive and negative values.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated range and expected range do not match with mix of positive and negative values added.
    Return:
        none
    """
    test_item = 'range()'
    reason = "Range calculation with mixed positive and negative values"
    stats = S.Statistics()
    values = [-5, 3, -2, 7, 1]
    for value in values:
        stats.add(value)
    expected = 12  # 7 - (-5)
    result = stats.range()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Testing range() with floating-point values
def test_range_floating_point():
    """
    Purpose:
        Verify range() method's accuracy with floating-point values.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated range and expected range do not match with floating-point values added.
    Return:
        none
    """
    test_item = 'range()'
    reason = "Range calculation with floating-point values"
    stats = S.Statistics()
    values = [1.1, 2.5, 3.3, 2.2, 3.1]
    for value in values:
        stats.add(value)
    expected = 2.2  # 3.3 - 1.1
    result = stats.range()
    if not close_enough(result, expected):
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Testing range() with large range from negative to positive values
def test_range_large_values():
    """
    Purpose:
        Test range() method with a large range of values from negative to positive.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated range and expected range do not match with large range from negative to positive values added.
    Return:
        none
    """
    test_item = 'range()'
    reason = "Large range from negative to positive values"
    stats = S.Statistics()
    values = [-100, 50, 0, 100, -50]  # Large range from -100 to 100
    for value in values:
        stats.add(value)
    expected = 200  # 100 - (-100)
    result = stats.range()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test mode() when no values have been added
def test_mode_no_values():
    """
    Purpose:
        Verify that the mode() method returns None when no values have been added to the statistics.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated mode and expected mode do not match when no values have been added.
    Return:
        none
    """
    test_item = 'mode()'
    reason = "Expect None when no values have been added"
    stats = S.Statistics()
    expected = None
    result = stats.mode()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test mode() with a single value
def test_mode_single_value():
    """
    Purpose:
        Test that mode() method returns single value as the mode when only one value has been added.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated mode and expected mode do not match with a single value added.
    Return:
        none
    """
    test_item = 'mode()'
    reason = "Expect the single value as mode"
    stats = S.Statistics()
    stats.add(5)  # Adding a single value
    expected = 5
    result = stats.mode()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test mode() with identical values
def test_mode_identical_values():
    """
    Purpose:
        Confirm that mode() method identifies single identical value as the mode when multiple identical values have been added.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated mode and expected mode do not match with identical values added.
    Return:
        none
    """
    test_item = 'mode()'
    reason = "Expect the identical value as mode"
    stats = S.Statistics()
    values = [4, 4, 4, 4]  # Identical values
    for value in values:
        stats.add(value)
    expected = 4
    result = stats.mode()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test mode() with multiple modes
def test_mode_multiple_modes():
    """
    Purpose:
        Test mode() method's ability to return all modes in a tuple when multiple modes exist.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated mode and expected mode do not match with multiple modes added.
    Return:
        none
    """
    test_item = 'mode()'
    reason = "Expect all modes in a tuple when multiple modes exist"
    stats = S.Statistics()
    values = [1, 2, 2, 3, 3]  # Multiple modes (2 and 3)
    for value in values:
        stats.add(value)
    expected = (2, 3)
    result = stats.mode()
    if not isinstance(result, tuple) or set(result) != set(expected):  # Checks if not tuple or if each element in 'result' and 'expected' do not match
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test mode() when all values are unique
def test_mode_all_unique():
    """
    Purpose:
        Verify that mode() method returns None when all added values are unique, indicating no mode.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated mode and expected mode do not match when all values are unique added.
    Return:
        none
    """
    test_item = 'mode()'
    reason = "Expect None when all values are unique"
    stats = S.Statistics()
    values = [1, 2, 3, 4, 5]  # All unique values
    for value in values:
        stats.add(value)
    expected = None
    result = stats.mode()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test mode() with a mix of negative and positive values
def test_mode_negative_positive():
    """
    Purpose:
        Test mode() method with a mix of negative and positive values to identify correct modes.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated mode and expected mode do not match when a mix of negative and positive values added.
    Return:
        none
    """
    test_item = 'mode()'
    reason = "Mode calculation with mixed negative and positive values"
    stats = S.Statistics()
    values = [-1, -1, 0, 1, 1, 2]  # Mode should be -1 and 1
    for value in values:
        stats.add(value)
    expected = (-1, 1)
    result = stats.mode()
    if not isinstance(result, tuple) or set(result) != set(expected):  # Checks if not tuple or if each element in 'result' and 'expected' do not match
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test mode with floating point numbers
def test_mode_floating_point():
    """
    Purpose:
        Verify mode() method's precision with floating-point values.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated mode and expected mode do not match when floating point numbers added.
    Return:
        none
    """
    test_item = 'mode() floating-point'
    reason = "Mode calculation with floating-point values"
    stats = S.Statistics()
    values = [1.1, 2.2, 2.2, 3.3]  # Mode should be 2.2
    for value in values:
        stats.add(value)
    expected = 2.2
    result = stats.mode()
    if not close_enough(result, expected):
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test max() with no values
def test_max_no_values():
    """
    Purpose:
        Confirm max() method returns None when no values have been added.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated max and expected max do not match with no values added.
    Return:
        none
    """
    test_item = 'max()'
    reason = "Expect None when no values have been added"
    stats = S.Statistics()
    expected = None
    result = stats.max()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test max() with a single value
def test_max_single_value():
    """
    Purpose:
        Test that max() method returns the single value as the maximum when only one value has been added.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated max and expected max do not match with a single value added.
    Return:
        none
    """
    test_item = 'max()'
    reason = "Expect single value as max"
    stats = S.Statistics()
    stats.add(5)  # Adding a single value
    expected = 5
    result = stats.max()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test max() with only negative values
def test_max_only_negative():
    """
    Purpose:
        Verify max() method's ability to calculate maximum among only negative values.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated max and expected max do not match with only negative values added.
    Return:
        none
    """
    test_item = 'max()'
    reason = "Max calculation with only negative values"
    stats = S.Statistics()
    values = [-5, -3, -8, -2]  # Only negative values
    for value in values:
        stats.add(value)
    expected = -2  # Least negative value
    result = stats.max()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test max() with a mix of positive and negative values
def test_max_positive_negative():
    """
    Purpose:
        Test max() method with mix of positive and negative values to identify the correct maximum.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated max and expected max do not match with a mix of positive and negative values added.
    Return:
        none
    """
    test_item = 'max()'
    reason = "Max calculation with mix of positive and negative values"
    stats = S.Statistics()
    values = [-1, 0, 3, -4, 2]  # Mix of positive and negative
    for value in values:
        stats.add(value)
    expected = 3
    result = stats.max()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test max() with floating-point values
def test_max_floating_point():
    """
    Purpose:
        Verify max() method's precision with floating-point values.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated max and expected max do not match with floating-point values added.
    Return:
        none
    """
    test_item = 'max() floating-point'
    reason = "Max calculation with floating-point values"
    stats = S.Statistics()
    values = [1.1, 2.5, 3.3, 2.2, -1.1]  # Floating-point values
    for value in values:
        stats.add(value)
    expected = 3.3
    result = stats.max()
    if not close_enough(result, expected):
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test max() with large range of values
def test_max_large_range():
    """
    Purpose:
        Test max() method with a large range of values to ensure accuracy.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated max and expected max do not match with large range of values added.
    Return:
        none
    """
    test_item = 'max() large range'
    reason = "Max calculation with a large range of values"
    stats = S.Statistics()
    values = [100, -50, 0, 200, -100]  # Large range of values
    for value in values:
        stats.add(value)
    expected = 200
    result = stats.max()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test min() with no values added
def test_min_no_values():
    """
    Purpose:
        Confirm min() method returns None when no values have been added.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated min and expected min do not match with no values added.
    Return:
        none
    """
    test_item = 'min()'
    reason = "Expect None when no values have been added"
    stats = S.Statistics()
    expected = None
    result = stats.min()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test min() with a single value
def test_min_single_value():
    """
    Purpose:
        Test that min() method returns the single value as the minimum when only one value has been added.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated min and expected min do not match with a single value added.
    Return:
        none
    """
    test_item = 'min()'
    reason = "Expect the single value as min"
    stats = S.Statistics()
    stats.add(5)  # Adding a single value
    expected = 5
    result = stats.min()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test min with only positive values
def test_min_only_positive():
    """
    Purpose:
        Verify min() method's ability to calculate minimum among only negative values.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated max and expected max do not match with only negative values added.
    Return:
        none
    """
    test_item = 'min()'
    reason = "Min calculation with only positive values"
    stats = S.Statistics()
    values = [5, 3, 8, 2, 10]  # Only positive values
    for value in values:
        stats.add(value)
    expected = 2
    result = stats.min()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test min() with mix of positive and negative values
def test_min_positive_negative():
    """
    Purpose:
        Test min() method with mix of positive and negative values to identify the correct minimum.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated min and expected min do not match with a mix of positive and negative values added.
    Return:
        none
    """
    test_item = 'min()'
    reason = "Min calculation with a mix of positive and negative values"
    stats = S.Statistics()
    values = [-1, 0, 3, -4, 2]  # Mix of positive and negative
    for value in values:
        stats.add(value)
    expected = -4  # Lowest negative value
    result = stats.min()
    if result != expected:
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test min() with floating point values
def test_min_floating_point():
    """
    Purpose:
        Verify min() method's precision with floating-point values.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated min and expected min do not match with floating-point values added.
    Return:
        none
    """
    test_item = 'min()'
    reason = "Min calculation with floating-point values"
    stats = S.Statistics()
    values = [1.1, 2.5, -3.3, 2.2, -1.1]  # Floating-point values
    for value in values:
        stats.add(value)
    expected = -3.3
    result = stats.min()
    if not close_enough(result, expected):
        print(f'Error in {test_item}: expected {expected} but obtained {result} -- {reason}')


# Test min() with large range of values
def test_min_large_range():
    """
    Purpose:
        Test min() method with a large range of values to ensure accuracy.
    Pre-Conditions:
        none
    Post-Conditions:
        Prints error message if calculated min and expected min do not match with large range of values added.
    Return:
        none
    """
    test_item = 'min()'
    reason = "Min calculation with a large range of values"
    stats = S.Statistics()
    values = [100, -50, 0, 200, -100]  # Large range of values
    for value in values:
        stats.add(value)
    expected = -100
    result = stats.min()
    if result != expected:
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
    test_range_no_values()
    test_range_single_value()
    test_range_identical_values()
    test_range_positive_negative()
    test_range_floating_point()
    test_range_large_values()
    test_mode_no_values()
    test_mode_single_value()
    test_mode_identical_values()
    test_mode_multiple_modes()
    test_mode_all_unique()
    test_mode_negative_positive()
    test_mode_floating_point()
    test_max_no_values()
    test_max_single_value()
    test_max_only_negative()
    test_max_positive_negative()
    test_max_floating_point()
    test_max_large_range()
    test_min_no_values()
    test_min_single_value()
    test_min_only_positive()
    test_min_positive_negative()
    test_min_floating_point()
    test_min_large_range()
    print('*** Test script completed ***')
