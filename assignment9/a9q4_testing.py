"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

from treenode import treenode
from a9q4 import good_complete


# 'GOOD_COMPLETE' FUNCTION TESTS
def test_empty_tree():
    root = None
    assert good_complete(root) == False, "Failed: Empty tree should not be considered complete."


def test_single_node_tree():
    root = treenode(1)
    assert good_complete(root) == True, "Failed: Single-node tree should be considered complete."


def test_complete_binary_tree():
    root = treenode(1, treenode(2), treenode(3))
    assert good_complete(root) == True, "Failed: Tree is complete but was not recognized as such"


def test_incomplete_binary_tree():
    root = treenode(1, treenode(2, None, treenode(5)), treenode(3, None, treenode(6)))
    assert good_complete(root) == False, "Failed: Tree missing node at the left not considered complete."


def test_incomplete_binary_tree2():
    root = treenode(1, treenode(2, None, treenode(3)), None)
    assert good_complete(root) == False, "Failed: Tree is incomplete but was incorrectly recognized as complete"


def test_full_binary_tree():
    root = treenode(1, treenode(2, treenode(4), treenode(5)), treenode(3, treenode(6), treenode(7)))
    assert good_complete(root) == True, "Failed: Full binary tree should be considered complete."


def main():
    test_empty_tree()
    test_single_node_tree()
    test_incomplete_binary_tree()
    test_incomplete_binary_tree2()
    test_full_binary_tree()
    print("All tests passed!")


if __name__ == "__main__":
    main()
