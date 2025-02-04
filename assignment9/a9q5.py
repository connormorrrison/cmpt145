"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

from treenode import treenode


def ordered(tnode):
    """
    Purpose:
        Determines whether binary tree is ordered.
    Pre-conditions:
        'tnode': Treenode object representing root of binary tree or None if the tree is empty.
    Post-conditions:
        None
    Return:
        Boolean value: True if binary tree is ordered, otherwise returns False.
    """
    def check_ordered(tnode):
        """
        Purpose:
            Used by 'ordered' to recursively check if subtree is ordered. Also determines minimum and maximum values of
            each subtree to aid in ordering check.
        Pre-conditions:
            'tnode': Treenode object representing root of subtree or None if the subtree is empty.
        Post-conditions:
            None
        Return:
            A tuple (is_ordered, minimum_value, maximum_value):
            - 'is_ordered' is a boolean indicating if the subtree is ordered correctly.
            - 'minimum_value' is the smallest value found in subtree or None if the subtree is empty.
            - 'maximum_value' is the largest value found in subtree or None if the subtree is empty.
        """
        if tnode is None:
            return True, None, None

        left_ordered, left_minimum, left_maximum = check_ordered(tnode.left)

        # Checks if left subtree ordered and if all values less than current nodes
        if not left_ordered:
            return False, None, None
        if left_maximum is not None:
            if left_maximum >= tnode.data:
                return False, None, None

        right_ordered, right_minimum, right_maximum = check_ordered(tnode.right)

        # Checks if right subtree ordered and if all values greater than current nodes
        if not right_ordered:
            return False, None, None
        if right_minimum is not None:
            if right_minimum <= tnode.data:
                return False, None, None

        # Calculate minimum and maximum for current subtree
        if left_minimum is not None:
            minimum_value = left_minimum
        else:
            minimum_value = tnode.data

        if right_maximum is not None:
            maximum_value = right_maximum
        else:
            maximum_value = tnode.data

        return True, minimum_value, maximum_value

    is_ordered, min_val, max_val = check_ordered(tnode)

    return is_ordered


def main():
    """
    Purpose:
        Main function, demonstrates functions and displays results.
    Pre-conditions:
        None
    Post-conditions:
        Outputs to console whether each tested binary tree is ordered.
    Return:
        None
    """
    # Ordered tree
    ordered_tree = treenode(5,
                            treenode(3, treenode(2), treenode(4)),
                            treenode(7, None, treenode(8))
                            )
    print(f"Ordered tree is ordered: {ordered(ordered_tree)}")

    # Unordered tree
    unordered_tree = treenode(5,
                              treenode(3, None, treenode(6)),
                              treenode(7, treenode(4), treenode(8))
                              )
    print(f"Unordered tree is ordered: {ordered(unordered_tree)}")


if __name__ == "__main__":
    main()
