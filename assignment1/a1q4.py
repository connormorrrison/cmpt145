"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Laboratory Section: L02
"""


# Read file
def read_file(file_path):
    """
    Purpose:
        Read a file containing matrix configuration and rotation commands.
    Pre-conditions:
        file_path: a string path to the file. First three lines represent a 3x3 matrix,
        and subsequent lines represent rotation commands.
    Post-conditions:
        None
    Return:
        List containing a 3x3 matrix of integers and a list of rotation commands.
    """
    with open(file_path, 'r') as file:

        # Process initial matrix
        matrix = []  # Initialize empty list
        for file_row in range(3):
            row = []
            for num in file.readline().strip().split():
                row.append(int(num))
            matrix.append(row)

        # Read number of rotations
        num_rotations = int(file.readline().strip())

        # Read rotation commands
        rotations = []
        for file_row in range(num_rotations):
            rotation_command = file.readline().strip().split()
            rotations.append(rotation_command)

    return matrix, rotations


# Rotate "right"
def rotate_right(matrix, row):
    """
    Purpose:
        Rotate elements of a row in the matrix to the right by one position.
    Pre-conditions:
        matrix: list of lists representing a matrix.
        row: an integer representing the row number in the matrix to be rotated.
    Post-conditions:
        Specified row of matrix is modified by shifting each element to the right.
    Return:
        Modified matrix list.
    """
    matrix[row] = [matrix[row][-1]] + matrix[row][:-1]
    return matrix


# Rotate "left"
def rotate_left(matrix, row):
    """
    Purpose:
        Rotate elements of a row in the matrix to the left by one position.
    Pre-conditions:
        matrix: list of lists representing a matrix.
        row: an integer representing the row number in the matrix to be rotated.
    Post-conditions:
        Specified row of matrix is modified by shifting each element to the left.
    Return:
        Modified matrix list.
    """
    matrix[row] = matrix[row][1:] + [matrix[row][0]]
    return matrix


# Rotate "up"
def rotate_up(matrix, column):
    """
    Purpose:
        Rotate elements of a row in the matrix upwards by one position.
    Pre-conditions:
        matrix: list of lists representing a matrix.
        row: an integer representing the column number in the matrix to be rotated.
    Post-conditions:
        Specified column of matrix is modified by shifting each element upwards.
    Return:
        Modified matrix list.
    """
    top_element = matrix[0][column]
    for i in range(2):
        matrix[i][column] = matrix[i + 1][column]
    matrix[2][column] = top_element
    return matrix


# Rotate "down"
def rotate_down(matrix, column):
    """
    Purpose:
        Rotate elements of a row in the matrix downwards by one position.
    Pre-conditions:
        matrix: list of lists representing a matrix.
        row: an integer representing the column number in the matrix to be rotated.
    Post-conditions:
        Specified column of matrix is modified by shifting each element downwards.
    Return:
        Modified matrix list.
    """
    bottom_element = matrix[2][column]
    for i in range(2, 0, -1):
        matrix[i][column] = matrix[i - 1][column]
    matrix[0][column] = bottom_element
    return matrix


# Compute rotations
def perform_rotation(matrix, rotation):
    """
    Purpose:
        Perform rotation operation on matrix based on given rotation command.
    Pre-conditions:
        matrix: list of lists representing matrix.
        rotation: list where the first element is a string representing direction of rotation, "R", "L", "U", "D"
        and second element is an integer representing the row or column index.
    Post-conditions:
        Matrix is modified based on the rotation command.
    Return:
        None
    """
    direction, index = rotation[0], int(rotation[1])
    if direction == 'R':
        rotate_right(matrix, index)
    elif direction == 'L':
        rotate_left(matrix, index)
    elif direction == 'U':
        rotate_up(matrix, index)
    elif direction == 'D':
        rotate_down(matrix, index)
    else:
        print(f"Error: Invalid rotation")


# Apply rotations
def apply_rotations(matrix, rotations):
    """
    Purpose:
        Apply rotation operations on the matrix.
    Pre-conditions:
        matrix: list of lists representing matrix.
        rotations: list of rotation commands, each command is a list where first element represents
        direction of rotation and second element represents row or column index.
    Post-conditions:
        Matrix is modified based on rotation commands.
    Return:
        None
    """
    for rotation in rotations:
        perform_rotation(matrix, rotation)


# Display matrix
def display_matrix(matrix):
    """
    Purpose:
        Display matrix, with proper formatting.
    Pre-conditions:
        matrix: list of lists representing matrix.
    Post-conditions:
        Matrix is printed to the console.
    Return:
        None
    """
    for row in matrix:
        row_string = []
        for num in row:
            row_string.append(str(num))
        row_string = ' '.join(row_string)
        print(row_string)


# Main function
def main():
    """
    Purpose:
        Main function to execute program. It reads a file, performs rotations based on the commands
        from the file, and displays the final matrix.
    Pre-conditions:
        None
    Post-conditions:
        Program reads a file, updates the matrix based on rotation commands, and prints the final matrix configuration.
    Return:
        None
    """
    file_name = input(f"File to load: ")
    matrix_configuration, matrix_rotations = read_file(file_name)
    apply_rotations(matrix_configuration, matrix_rotations)
    display_matrix(matrix_configuration)


if __name__ == "__main__":
    main()
