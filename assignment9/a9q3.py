"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

from treenode import treenode


def expression(t):
    """
    Purpose:
        Converts tree representing an expression into a string representation.
    Pre-conditions:
        't': Treenode object representing root of tree. Non-leaf represents operators and leafs represent operands.
    Post-conditions:
        None
    Return:
        String that represents expression contained within tree. Returns empty string if input is None.
    """
    if t is None:
        return ''

    # Leaf node: return its value
    if t.left is None and t.right is None:
        return str(t.data)

    # Internal node: return operation on children with brackets
    left_expr = expression(t.left)
    right_expr = expression(t.right)
    return f"({left_expr} {t.data} {right_expr})"


def main():
    """
    Purpose:
        Main function, demonstrates functions and displays results.
    Pre-conditions:
        None
    Post-conditions:
        Outputs string representation of expression to console.
    Return:
        None
    """
    # Expression: ((4 + 13) * (9 - 5))
    root = treenode('*',
                    treenode('+', treenode(4), treenode(13)),
                    treenode('-', treenode(9), treenode(5)))

    print("Result:", expression(root))


if __name__ == "__main__":
    main()
