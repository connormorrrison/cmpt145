"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""


def read_file(file_path):
    """
    Purpose:
        Reads maze map from text file and represents it as a list of lists.
    Pre-conditions:
        'file_path': String representing the path to the file.
    Post-conditions:
        None
    Return:
        List of lists representing the maze.
    """
    maze = []
    with open(file_path, "r") as file:
        for line in file.readlines():
            stripped_line = line.strip().replace(" ", "")
            line_as_list = list(stripped_line)
            maze.append(line_as_list)
    return maze


def display_results(maze):
    """
    Purpose:
        Prints maze for user.
    Pre-conditions:
        'maze': List of lists representing maze.
    Post-conditions:
        Maze is printed to console.
    Return:
        None
    """
    for row in maze:
        print(''.join(row))


def valid_move(maze, position):
    """
    Purpose:
        Checks if a move is valid.
    Pre-conditions:
        'maze': List of lists representing maze.
        'position': Tuple (r, c) representing row and column to check within the maze.
    Post-conditions:
        None
    Return:
        True if the move is valid, otherwise False.
    """
    r, c = position  # Tuple for row, column
    if 0 <= r < len(maze) and 0 <= c < len(maze[0]) and maze[r][c] == '0':  # In bounds and open cell
        return True
    return False


def SolveMaze(m, s, g, visited=None):
    """
    Purpose:
        Attempts to find path from a start position 's' to a goal position 'g', marking traveled path with 'P'.
    Pre-conditions:
        'm': List of lists representing maze.
        's': Tuple (r, c) representing start position.
        'g': Tuple (r, c) representing goal position.
        'visited': Set of tuples representing positions that have already been visited. Default is None.
    Post-conditions:
        Maze may be modified to include path marked by 'P' from the start position to the goal position if a path exists.
    Return:
        True if path from start to goal was found, otherwise False.
    """
    if visited is None:
        visited = set()

    if s == g:  # If current position is the goal
        m[s[0]][s[1]] = 'P'
        return True  # Path found

    r, c = s
    if not valid_move(m, (r, c)) or (r, c) in visited:
        return False

    visited.add(s)  # Add current position to visited set

    directions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
    for next_s in directions:
        if SolveMaze(m, next_s, g, visited):  # Recursive function call with next position
            m[r][c] = 'P'  # Mark current position as part of path
            return True

    return False


def main():
    """
    Purpose:
        Main function, reads maze from a file, attempts to find path using recursion, and displays results.
    Pre-conditions:
        None
    Post-conditions:
        Outputs solution to the maze if found. If no path is found, it prints message indicating no path was found.
    Return:
        None
    """
    file_name = "Maze1.txt"
    maze_map = read_file(file_name)

    # Execute
    if SolveMaze(maze_map, (0, 3), (4, 5)):
        print("Maze 1 Solution:")
        display_results(maze_map)
    else:
        print("No path found in maze.")


if __name__ == "__main__":
    main()
