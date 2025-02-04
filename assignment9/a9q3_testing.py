"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

from treenode import treenode
from a9q3 import expression


# 'EXPRESSION' FUNCTION TESTS
def test_expression_empty_tree():
    root = None
    result = expression(root)
    assert result == "", f"Expected an empty string for an empty tree, got '{result}'"


def test_expression_single_node():
    root = treenode(42)
    result = expression(root)
    assert result == "42", f"Expected '42' for a single node tree, got '{result}'"


def test_expression_simple_tree():
    # Expression: (3 + 4)
    root = treenode('+', treenode(3), treenode(4))
    result = expression(root)
    assert result == "(3 + 4)", f"Expected '(3 + 4)' for a simple addition, got '{result}'"


def test_expression_complex_tree():
    # Expression: ((4 + 13) * (9 - 5))
    root = treenode('*',
                    treenode('+', treenode(4), treenode(13)),
                    treenode('-', treenode(9), treenode(5)))
    result = expression(root)
    assert result == "((4 + 13) * (9 - 5))", f"Expected '((4 + 13) * (9 - 5))' for a complex expression, got '{result}'"


def test_expression_unbalanced_tree():
    # Expression: (2 * (3 + (4 * 5)))
    root = treenode('*',
                    treenode(2),
                    treenode('+',
                             treenode(3),
                             treenode('*', treenode(4), treenode(5))))
    result = expression(root)
    assert result == "(2 * (3 + (4 * 5)))", f"Expected '(2 * (3 + (4 * 5)))', got '{result}'"


def main():
    test_expression_empty_tree()
    test_expression_single_node()
    test_expression_simple_tree()
    test_expression_complex_tree()
    test_expression_unbalanced_tree()
    print("All tests passed!")


if __name__ == "__main__":
    main()
