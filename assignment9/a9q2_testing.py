"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

from treenode import treenode
from a9q2 import subst, copy, collect_data_inorder, count_smaller


# 'SUBST' FUNCTION TESTS
def test_subst_empty_tree():
    empty_tree = None
    modified_empty_tree = copy(empty_tree)
    subst(modified_empty_tree, 'any_value', 'new_value')
    assert modified_empty_tree is None, "subst() should not modify an empty tree"


def test_subst_single_node_tree():
    single_node_tree = treenode('si')
    modified_single_node_tree = copy(single_node_tree)
    subst(modified_single_node_tree, 'si', 'no')
    assert collect_data_inorder(modified_single_node_tree) == ['no'], "subst() failed to replace 'si' with 'no'"


def test_subst_multi_node_tree():
    multi_node_tree = treenode(5, treenode(3), treenode(1))
    modified_multi_node_tree = copy(multi_node_tree)
    subst(modified_multi_node_tree, 1, 99)
    assert 99 in collect_data_inorder(modified_multi_node_tree), "subst() failed to replace '1' with '99'"


# 'COPY' FUNCTION TESTS
def test_copy_empty_tree():
    empty_tree = None
    copied_empty_tree = copy(empty_tree)
    assert copied_empty_tree is None, "copy() of an empty tree should return None"


def test_copy_single_node_tree():
    single_node_tree = treenode('si')
    copied_single_node_tree = copy(single_node_tree)
    assert collect_data_inorder(copied_single_node_tree) == ['si'], "copy() failed with a single-node tree"
    assert copied_single_node_tree is not single_node_tree, "copy() of a single-node tree returned the same instance"


def test_copy_multi_node_tree():
    multi_node_tree = treenode(5, treenode(3), treenode(1))
    copied_multi_node_tree = copy(multi_node_tree)
    assert collect_data_inorder(copied_multi_node_tree) == collect_data_inorder(multi_node_tree), "copy() failed to replicate the tree correctly"
    assert copied_multi_node_tree is not multi_node_tree, "copy() of a multi-node tree returned the same instance"


# 'COLLECT_DATA_INORDER' FUNCTION TESTS
def test_collect_data_inorder_empty_tree():
    empty_tree = None
    assert collect_data_inorder(empty_tree) == [], "collect_data_inorder() on an empty tree should return an empty list"


def test_collect_data_inorder_single_node_tree():
    single_node_tree = treenode('si')
    assert collect_data_inorder(single_node_tree) == ['si'], "collect_data_inorder() failed with a single-node tree"


def test_collect_data_inorder_multi_node_tree():
    multi_node_tree = treenode(5, treenode(3), treenode(1))
    assert collect_data_inorder(multi_node_tree) == [3, 5, 1], "collect_data_inorder() failed with a multi-node tree"


# 'COUNT_SMALLER' FUNCTION TESTS
def test_count_smaller_empty_tree():
    empty_tree = None
    assert count_smaller(empty_tree, 10) == 0, "count_smaller() on an empty tree should return 0"


def test_count_smaller_single_node_tree_numerical():
    single_node_tree = treenode(5)
    assert count_smaller(single_node_tree, 10) == 1, "count_smaller() failed with a single-node numerical tree"


def test_count_smaller_multi_node_tree():
    multi_node_tree = treenode(5, treenode(3), treenode(7))
    assert count_smaller(multi_node_tree, 10) == 3, "count_smaller() failed with a multi-node tree"


def main():
    test_subst_empty_tree()
    test_subst_single_node_tree()
    test_subst_multi_node_tree()
    test_copy_empty_tree()
    test_copy_single_node_tree()
    test_copy_multi_node_tree()
    test_collect_data_inorder_empty_tree()
    test_collect_data_inorder_single_node_tree()
    test_collect_data_inorder_multi_node_tree()
    test_count_smaller_empty_tree()
    test_count_smaller_single_node_tree_numerical()
    test_count_smaller_multi_node_tree()
    print("All tests passed!")


if __name__ == "__main__":
    main()
