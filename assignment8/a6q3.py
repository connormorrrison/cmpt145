"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

from node import node


def to_string(node_chain):
    """
    Purpose:
        Converts chain of nodes into string.
    Pre-conditions:
        'node_chain': Head node of the chain.
    Post-conditions:
        None
    Return:
        String representation of the node chain. Returns "EMPTY" if the node chain is None.
    """
    if node_chain is None:
        return "EMPTY"
    else:
        if node_chain.get_next() is None:
            return f"[ {node_chain.get_data()} | / ]"
        else:
            next_part = to_string(node_chain.get_next())
            return f"[ {node_chain.get_data()} | * -]-->{next_part}"


def copy(node_chain):
    """
    Purpose:
        Creates a copy of a given chain.
    Pre-conditions:
        'node_chain': Head node of chain to be copied. Can be 'None' if the chain is empty.
    Post-conditions:
        New chain of nodes is created that is a copy of the original. Original chain is not modified.
    Return:
        Head node of the copied chain. Returns 'None' if the input chain is empty.
    """
    if node_chain is None:
        return None
    else:
        return node(node_chain.get_data(), copy(node_chain.get_next()))


def replace(node_chain, target, replacement):
    """
    Purpose:
        Replaces occurrences of a value within the nodes of a chain with another value.
    Pre-conditions:
        'node_chain': Head node of the chain. Can be 'None' if the chain is empty.
        'target': Value to be replaced within the nodes of the chain.
        'replacement': Value to replace all occurrences of the target value.
    Post-conditions:
        All nodes in chain that contained the target value will be modified to contain replacement value.
    Return:
        Head node of the modified chain. Returns 'None' if input chain is empty.
    """
    if node_chain is None:
        return None
    else:
        current_data = node_chain.get_data()
        if current_data == target:
            node_chain.set_data(replacement)
        replace(node_chain.get_next(), target, replacement)
        return node_chain


def main():
    """
    Purpose:
        Main function, demonstrates above functions, and prints results.
    Pre-conditions:
        None
    Post-conditions:
        Outputs original node chain, a copy, and original chain after performing a value replacement.
    Return:
        None
    """
    node_chain = node(1, node(2, node(3)))

    # to_string function
    print("Original node chain:")
    print(to_string(node_chain))

    # copy function
    copied_chain = copy(node_chain)
    print("Copied node chain:")
    print(to_string(copied_chain))

    # replace function
    replace(node_chain, 2, 200)
    print("Node chain after replacement (2 replaced with 200):")
    print(to_string(node_chain))


if __name__ == "__main__":
    main()
