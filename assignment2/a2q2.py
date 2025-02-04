"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""


# Calculate final position
def calculate_position(directions):
    """
    Purpose:
        Calculate the final (x, y) position based on a series of directions.
    Pre-conditions:
        - directions: iterable string, each representing a series of directions (N, S, E, W).
    Post-conditions:
        - None.
    Return:
        A tuple (x, y) representing the final position.
    """
    # Initialize starting (x, y) position
    x, y = 0, 0

    # Calculate position change
    for direction in directions:
        if direction == "N":
            y = y + 1
        elif direction == "S":
            y = y - 1
        elif direction == "E":
            x = x + 1
        elif direction == "W":
            x = x - 1
        else:
            x, y = 0, 0  # If no directions or invalid directions, return starting position

    return x, y


# Read file
def read_file(file_path):
    """
    Purpose:
        Read a file containing lines of directions and return a list of final positions.
    Pre-conditions:
        - file_path: a string representing the path to the text file.
    Post-conditions:
        - A file at file_path is opened and read. No changes made to the file.
    Return:
        A list of tuples, each tuple represents the final (x, y) position.
    """
    # Initialize empty list for coordinate pairs
    ordered_pairs_list = []

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            ordered_pair = calculate_position(line)
            ordered_pairs_list.append(ordered_pair)

    return ordered_pairs_list


# Display results
def display_results(ordered_pairs):
    """
    Purpose:
        Print each ordered pair of coordinates to the console.
    Pre-conditions:
        - ordered_pairs: a list of tuples, where each tuple represents an (x, y) position.
    Post-conditions:
        - Positions are printed to the console.
    Return:
        None.
    """
    for ordered_pair in ordered_pairs:
        print(ordered_pair)


# Main function
def main():
    """
    Purpose:
        Main function to run the program. Handles user input, file reading, and displaying results.
    Pre-conditions:
        - None.
    Post-conditions:
        - Reads user input, reads a file, and prints the final positions to console.
    Return:
        None.
    """
    file_name = input(f"File name: ")
    final_ordered_pairs_list = read_file(file_name)
    display_results(final_ordered_pairs_list)


if __name__ == "__main__":
    main()
