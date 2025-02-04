"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

from a6q2 import fibonacci, moosonacci, substr


# FIBONACCI FUNCTION TESTS
def test_fibonacci_base_case_0():
    result = fibonacci(0)
    assert result == 0, f"Expected 0, got {result}"


def test_fibonacci_base_case_1():
    result = fibonacci(1)
    assert result == 1, f"Expected 1, got {result}"


def test_fibonacci_recursive_case():
    result = fibonacci(10)
    assert result == 55, f"Expected 55, got {result}"


def test_fibonacci_negative_number():
    try:
        fibonacci(-1)
        assert False, "fibonacci(-1) should raise ValueError"
    except ValueError:
        pass  # Test passes
    except Exception as e:
        assert False, f"fibonacci(-1) raised an unexpected exception type: {e}"


# MOOSONACCI FUNCTION TESTS
def test_moosonacci_base_case_0():
    result = moosonacci(0)
    assert result == 0, f"Expected 0, got {result}"


def test_moosonacci_base_case_1():
    result = moosonacci(1)
    assert result == 1, f"Expected 1, got {result}"


def test_moosonacci_base_case_2():
    result = moosonacci(2)
    assert result == 2, f"Expected 2, got {result}"


def test_moosonacci_recursive_case_3():
    result = moosonacci(3)
    assert result == 3, f"Expected 3, got {result}"


def test_moosonacci_recursive_case_9():
    result = moosonacci(9)
    assert result == 125, f"Expected 125, got {result}"


def test_moosonacci_negative_number():
    try:
        moosonacci(-1)
        assert False, "moosonacci(-1) should raise ValueError"
    except ValueError:
        pass  # Test passes
    except Exception as e:
        assert False, f"moosonacci(-1) raised an unexpected exception type: {e}"


# SUBSTR FUNCTION TESTS
def test_substr_replace_single_occurrence():
    result = substr('Hello, world!', 'o', 'i')
    assert result == 'Helli, wirld!', f"Expected 'Helli, wirld!', got {result}"


def test_substr_replace_all_occurrences():
    result = substr('aaaa', 'a', 'b')
    assert result == 'bbbb', f"Expected 'bbbb', got {result}"


def test_substr_replace_in_mixed_string():
    result = substr('xyz', 'y', 'a')
    assert result == 'xaz', f"Expected 'xaz', got {result}"


def test_substr_target_not_present():
    result = substr("Hello, world!", "z", "q")
    assert result == "Hello, world!", f"Expected 'Hello, world!', got {result}"


def main():
    test_fibonacci_base_case_0()
    test_fibonacci_base_case_1()
    test_fibonacci_recursive_case()
    test_fibonacci_negative_number()
    test_moosonacci_base_case_0()
    test_moosonacci_base_case_1()
    test_moosonacci_base_case_2()
    test_moosonacci_recursive_case_3()
    test_moosonacci_recursive_case_9()
    test_moosonacci_negative_number()
    test_substr_replace_single_occurrence()
    test_substr_replace_all_occurrences()
    test_substr_replace_in_mixed_string()
    test_substr_target_not_present()
    print("All tests passed!")


if __name__ == "__main__":
    main()
