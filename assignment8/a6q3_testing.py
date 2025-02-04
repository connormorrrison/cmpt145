"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

from node import node
from a6q3 import to_string, copy, replace


# TO_STRING FUNCTION TESTS
def test_to_string_empty():
    result = to_string(None)
    assert result == "EMPTY", f"Expected 'EMPTY' for an empty node chain, got '{result}'"


def test_to_string_single_node():
    single_node = node(1)
    result = to_string(single_node)
    assert result == "[ 1 | / ]", f"Expected '[ 1 | / ]' for a single node, got '{result}'"


def test_to_string_multiple_nodes():
    chain_end = node(3)
    middle_node = node(2, chain_end)
    start_node = node(1, middle_node)
    result = to_string(start_node)
    expected = "[ 1 | * -]-->[ 2 | * -]-->[ 3 | / ]"
    assert result == expected, f"Expected '{expected}' for a node chain, got '{result}'"


# COPY FUNCTION TESTS
def test_copy_empty_chain():
    empty_chain = None
    copied_chain = copy(empty_chain)
    assert copied_chain is None, "Expected None for copying an empty chain"


def test_copy_single_node():
    single_node_chain = node(1)
    copied_chain = copy(single_node_chain)
    assert to_string(copied_chain) == "[ 1 | / ]", "Copied chain does not match original for a single-node chain"


def test_copy_identical_structure():
    start_node = node(1, node(2, node(3)))
    copied_chain = copy(start_node)
    assert to_string(copied_chain) == to_string(start_node), "Copied chain does not match original"


def test_copy_independent_copy():
    start_node = node(1, node(2, node(3)))
    copied_chain = copy(start_node)
    copied_chain.set_data(100)  # Modify copy
    assert to_string(start_node) != to_string(copied_chain), "Modification in copy affected the original"


# REPLACE FUNCTION TESTS
def test_replace_empty_chain():
    empty_chain = None
    result = replace(empty_chain, 1, 100)
    assert result is None, "Expected None when trying to replace in an empty chain"


def test_replace_no_match():
    start_node = node(1, node(2, node(3)))
    replace(start_node, 4, 100)  # Value not in chain
    assert to_string(start_node) == "[ 1 | * -]-->[ 2 | * -]-->[ 3 | / ]", "Replace modified the chain unexpectedly"


def test_replace_with_match():
    start_node = node(1, node(2, node(3)))
    replace(start_node, 2, 200)
    expected = "[ 1 | * -]-->[ 200 | * -]-->[ 3 | / ]"
    assert to_string(start_node) == expected, f"Expected '{expected}' after replacement, got '{to_string(start_node)}'"


def test_replace_multiple_matches():
    chain = node(1, node(2, node(2, node(3))))
    replace(chain, 2, 200)
    expected = "[ 1 | * -]-->[ 200 | * -]-->[ 200 | * -]-->[ 3 | / ]"
    assert to_string(chain) == expected, "Expected all '2's to be replaced with '200'"


def main():
    test_to_string_empty()
    test_to_string_single_node()
    test_to_string_multiple_nodes()
    test_copy_empty_chain()
    test_copy_single_node()
    test_copy_identical_structure()
    test_copy_independent_copy()
    test_replace_empty_chain()
    test_replace_no_match()
    test_replace_with_match()
    test_replace_multiple_matches()
    print("All tests passed successfully!")


if __name__ == "__main__":
    main()

