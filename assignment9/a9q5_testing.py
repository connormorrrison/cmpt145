"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

from treenode import treenode
from a9q5 import ordered


# 'ORDERED' FUNCTION TESTS
def test_ordered_empty_tree():
    assert ordered(None) == True, "Empty tree should be considered ordered"


def test_ordered_single_node():
    root = treenode(1)
    assert ordered(root) == True, "Single node tree should be considered ordered"


def test_ordered_ordered_tree():
    root = treenode(2, treenode(1), treenode(3))
    assert ordered(root) == True, "Properly ordered tree was not recognized as ordered"


def test_ordered_unordered_tree():
    unordered_tree = treenode(5,
                              treenode(3, None, treenode(6)),
                              treenode(7, treenode(4), treenode(8))
                              )
    assert ordered(unordered_tree) == False, "Unordered tree was incorrectly marked as ordered"


def test_ordered_left_violation():
    root = treenode(3, treenode(4), None)
    assert ordered(root) == False, "Tree with left node violation was incorrectly marked as ordered"


def test_ordered_right_violation():
    root = treenode(1, None, treenode(0))
    assert ordered(root) == False, "Tree with right node violation was incorrectly marked as ordered"


def main():
    test_ordered_empty_tree()
    test_ordered_single_node()
    test_ordered_ordered_tree()
    test_ordered_unordered_tree()
    test_ordered_left_violation()
    test_ordered_right_violation()
    print("All tests passed!")


if __name__ == "__main__":
    main()
