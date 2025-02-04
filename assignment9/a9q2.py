"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

from treenode import treenode
from exampletrees import atree, mtree, ctree, xtree, fibonatree, expr_tree


def subst(tnode, t, r):
    """
    Purpose:
        Substitute all occurrences of specified value with another value.
    Pre-conditions:
        'tnode': Treenode object representing the root of the tree.
        't': Value to be replaced.
        'r': New value to substitute for 't'.
    Post-conditions:
        Modifies tree by replacing all instances of 't' with 'r'.
    Return:
        None
    """
    if tnode is None:
        return None

    if tnode.data == t:
        tnode.data = r

    subst(tnode.left, t, r)
    subst(tnode.right, t, r)


def copy(tnode):
    """
    Purpose:
        Creates copy of a tree.
    Pre-conditions:
        'tnode': Treenode object representing root of tree to copy.
    Post-conditions:
        New binary tree is created as a copy of the original.
    Return:
        Root treenode of the copied tree.
    """
    if tnode is None:
        return None

    new_node = treenode(tnode.data)
    new_node.left = copy(tnode.left)
    new_node.right = copy(tnode.right)

    return new_node


def collect_data_inorder(tnode):
    """
    Purpose:
        Collects and returns data from all nodes in tree in an inorder traversal.
    Pre-conditions:
        'tnode': Treenode object representing the root of tree.
    Post-conditions:
        None
    Return:
        List of data values from tree collected in an inorder sequence.
    """
    if tnode is None:
        return []

    # Collect data from the left subtree, current node, then right subtree
    data_list = collect_data_inorder(tnode.left)
    data_list.append(tnode.data)
    data_list.extend(collect_data_inorder(tnode.right))

    return data_list


def count_smaller(tnode, target):
    """
    Purpose:
        Counts number of nodes in tree that contain value smaller than target value.
    Pre-conditions:
        'tnode': Treenode object representing root of tree.
        'target': Numeric value against which nodes' values will be compared.
    Post-conditions:
        None
    Return:
        Integer representing count of nodes in tree with values less than 'target'.
    """
    if tnode is None:
        return 0

    count = 0
    if tnode.data < target:
        count = 1

    return count + count_smaller(tnode.left, target) + count_smaller(tnode.right, target)


def main():
    """
    Purpose:
        Main function, demonstrates functions and displays results.
    Pre-conditions:
        None
    Post-conditions:
        Outputs results to console.
    Return:
        None
    """
    # Sample tree 'xtree'
    xtree = treenode(5,
                        treenode(1, None,
                                    treenode(4,
                                                treenode(3, treenode(2, None, None), None),
                                                None)),
                        treenode(9, treenode(8, treenode(7, treenode(6, None, None), None), None),
                                    treenode(1, treenode(3, None, None), treenode(3, None, None))))

    # Display original tree
    print("Original tree:")
    print(collect_data_inorder(xtree))

    # subst function
    t = 1
    r = 99
    subst(xtree, t, r)  # Example: substitute all 1 with 99
    print(f"\n'subst' Function: tree after substituting {t} with {r}:")
    print(collect_data_inorder(xtree))

    # copy function
    copied_xtree = copy(xtree)
    print("\n'copy' Function: Copied tree:")
    print(collect_data_inorder(copied_xtree))

    # collect_data_inorder function
    print("\n'collect_data_inorder' Function: Data in copied tree:")
    print(collect_data_inorder(copied_xtree))

    # count_smaller function
    target = 10
    count_smaller_result = count_smaller(xtree, target)
    print(f"\n'count_smaller' Function: Number of nodes with values smaller than {target}: {count_smaller_result}")


if __name__ == "__main__":
    main()
