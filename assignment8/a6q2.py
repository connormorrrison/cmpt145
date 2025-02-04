"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""


def fibonacci(n):
    """
    Purpose:
        Computes the nth Fibonacci number.
    Pre-conditions:
        'n': An integer representing position in Fibonacci sequence.
    Post-conditions:
        None
    Return:
        An integer.
    """
    # Error handling
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def moosonacci(n):
    """
    Purpose:
        Computes the nth Moosonacci number.
    Pre-conditions:
        'n': An integer representing position in Moosonacci sequence.
    Post-conditions:
        None
    Return:
        An integer.
    """
    # Error handling
    if n < 0:
        raise ValueError("Input must be a non-negative integer")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return moosonacci(n - 1) + moosonacci(n - 2) + moosonacci(n - 3)


def substr(s, c, r):
    """
    Purpose:
        Replaces all occurrences of a character 'c' with another character 'r' in a given string 's'.
    Pre-conditions:
        's': String where replacement is made.
        'c': Single character to be replaced.
        'r': Single character that will replace every occurrence of 'c'.
    Post-conditions:
        None
    Return:
        A string with replaced characters.
    """
    # Error handling
    if len(c) != 1 or len(r) != 1:
        raise ValueError("c and r must be single characters")

    if not s:
        return ""
    else:
        head = s[0]
        tail = s[1:]
        if head == c:
            return r + substr(tail, c, r)
        else:
            return head + substr(tail, c, r)


def main():
    """
    Purpose:
        Main function, collects input and displays results.
    Pre-conditions:
        None
    Post-conditions:
        Prints the results of the Fibonacci, Moosonacci, or substr functions.
    Return:
        None
    """
    # Fibonacci function
    try:
        print("Fibonacci")
        fibonacci_number = int(input("n: "))
        print(f"Result: {fibonacci(fibonacci_number)}")
    except ValueError as e:
        print(e)

    # Moosonacci function
    try:
        print("Moosonacci")
        moosonacci_number = int(input("n: "))
        print(f"Result: {moosonacci(moosonacci_number)}")
    except ValueError as e:
        print(e)

    # substr function
    try:
        print("substr")
        input_string = input("s: ")
        input_character = input("c: ")
        replacement = input("r: ")
        print(f"Result: {substr(input_string, input_character, replacement)}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
