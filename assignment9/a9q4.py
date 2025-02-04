"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

from treenode import treenode


def good_complete(tnode):
    """
    Purpose:
        Determines if tree is a "complete tree".
    Pre-conditions:
        'tnode': Treenode object representing root of tree or None if the tree is empty.
    Post-conditions:
        None
    Return:
        Boolean: True if the binary tree is "complete tree" and False otherwise.
    """
    def cmplt(tnode):
        """
        Purpose:
            Used by 'good_complete' to check each subtree for 'completeness' by checking flag and height of subtree.
        Pre-conditions:
            'tnode': Treenode object representing root of subtree or None if the subtree is empty.
        Post-conditions:
            None
        Return:
            Tuple (flag, height) where 'flag' is a boolean indicating if the subtree is complete, and 'height' is
            integer height of subtree. If subtree is not complete, 'height' is returned as None.
        """
        if tnode is None:
            return True, 0

        left_flag, left_height = cmplt(tnode.left)
        right_flag, right_height = cmplt(tnode.right)

        if not left_flag or not right_flag:
            return False, None

        if left_height == right_height or left_height == right_height + 1:
            return True, max(left_height, right_height) + 1
        else:
            return False, None

    if tnode is None:
        return False

    flag, height = cmplt(tnode)
    return flag


def main():
    """
    Purpose:
        Main function, demonstrates functions and displays results.
    Pre-conditions:
        None
    Post-conditions:
        Outputs to console the result of checking 'completeness' for each tree.
    Return:
        None
    """
    # Empty tree
    empty_tree = None
    print(f"An empty tree is complete: {good_complete(empty_tree)}")

    # Single-node tree
    single_node = treenode(1)
    print(f"A single-node tree is complete: {good_complete(single_node)}")

    # Incomplete binary tree
    incomplete_tree = treenode(1,
                               treenode(2, None, treenode(5)),
                               treenode(3, None, treenode(6))
                               )
    print(f"An incomplete binary tree is complete: {good_complete(incomplete_tree)}")

    # Complete binary tree
    full_tree = treenode(1,
                         treenode(2, treenode(4), treenode(5)),
                         treenode(3, treenode(6), treenode(7))
                         )
    print(f"A complete binary tree is complete: {good_complete(full_tree)}")


if __name__ == "__main__":
    main()
