"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""


def MothraCount(a, b):
    """
    Purpose:
        Calculates number of unique paths from a 'a' x 'b' grid.
    Pre-conditions:
        'a': Integer representing number of rows in grid.
        'b': Integer representing number of columns in grid.
    Post-conditions:
        None
    Return:
        Integer representing total number of unique paths.
    """
    if a == 1 or b == 1:
        return 1

    return MothraCount(a - 1, b) + MothraCount(a, b - 1)


def main():
    """
    Purpose:
        Main function, demonstrates MothraCount function, and prints results.
    Pre-conditions:
        None
    Post-conditions:
        Prints number of unique paths for 3x3, 4x4, and 10x12 rooms.
    Return:
        None
    """
    print("Number of paths for a 3x3 room:", MothraCount(3, 3))
    print("Number of paths for a 4x4 room:", MothraCount(4, 4))
    print("Number of paths for a 10x12 room:", MothraCount(10, 12))


if __name__ == "__main__":
    main()
