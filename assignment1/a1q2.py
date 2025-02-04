"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Laboratory Section: L02
"""

from isfloat import isfloat


# Read file and return a list of commands
def read_file(file_path):
    """
    Purpose:
        Read file and return a list of strings, each representing a line in the file.
    Pre-conditions:
        file_path: a string representing the path to the file.
    Post-conditions:
        The file at file_path is read, contents are not modified.
    Return:
        A list of strings, each string is a line from the file.
    """
    with open(file_path, "r") as file:
        script_commands = file.readlines()
    return script_commands


# Process each command
def process_commands(script_commands, script_constants):
    """
    Purpose:
        Process a list of script commands, processing arithmetic and operations.
    Pre-conditions:
        script_commands: a list of strings, each representing a script command.
        script_constants: a dictionary containing named constants used in the script commands.
    Post-conditions:
        Depending on commands in script_commands, function may modify script_constants and output to the console.
    Return:
        Final value of the register R after processing all commands.
    """
    R = 0
    for command in script_commands:
        command = command.strip()
        if command:  # Check if command is not empty
            R = execute_command(command, R, script_constants)
    return R


# Execute a single command
def execute_command(script_commands, R, script_constants):
    """
    Purpose:
        Execute a single script command, updating the register R or performing operations.
    Pre-conditions:
        script_command: a string representing the script command to execute.
        R: the current value of the register R.
        script_constants: a dictionary containing named constants used in the script commands.
    Post-conditions:
        Depending on script_command, function may update script_constants, output to the console or update value of R.
    Return:
        New value of register R after executing script command.
    """
    components = script_commands.split()
    if len(components) == 0:
        return R  # Skip if command empty

    if components[0] == "ASK":
        ask_command(components[1], script_constants)
    elif components[0] == "TELL":
        tell_command(R)
    else:
        R = arithmetic_command(components[0], components[1], R, script_constants)
    return R


# Process "ASK" command
def ask_command(name, script_constants):
    """
    Purpose:
        Prompt user for input and store in script_constants.
    Pre-conditions:
        name: name of the constant to prompt for.
        script_constants: dictionary where the value will be stored.
    Post-conditions:
        script_constants may be modified to include the new value provided by the user.
        Function may output to the console.
    Return:
        None
    """
    value = input(f"{name}? ")
    if isfloat(value):
        script_constants[name] = float(value)
    else:
        print("Error: Enter a floating point number.")


# Process "TELL" command
def tell_command(R):
    """
    Purpose:
        Output value of register R to the console.
    Pre-conditions:
        R: value to be output.
    Post-conditions:
        Function outputs to the console, the value of R.
    Return:
        None
    """
    print(R)


# Process arithmetic computations
def arithmetic_command(operation, operand, R, script_constants):
    """
    Purpose:
        Perform an arithmetic operation on the register R and an operand.
    Pre-conditions:
        operation: a string arithmetic operation to perform, "ADD", "SUB", "MUL", "DIV".
        operand: a string operand, either a constant or a numeric value.
        R: current value of the register R.
        script_constants: dictionary containing named constants, which may be used as the operand.
    Post-conditions:
        Function may produce output to the console, error messages.
    Return:
        New value of register R after the arithmetic operation.
    """
    if operand in script_constants:
        operand_value = script_constants[operand]
    elif isfloat(operand):
        operand_value = float(operand)
    else:
        print("Invalid operand: {operand}")
        return R

    if operation == "ADD":
        return R + operand_value
    elif operation == "SUB":
        return R - operand_value
    elif operation == "MUL":
        return R * operand_value
    elif operation == "DIV":
        if operand_value != 0:
            return R / operand_value
        else:
            print(f"Error: Division by zero.")
    else:
        print(f"Invalid operation: {operation}")


# Main function
def main():
    """
    Purpose:
        Main function of the program, to load a file of commands and process them.
    Pre-conditions:
        None, the function will prompt for the file to load.
    Post-conditions:
        Function will output to the console and prompt for user input.
    Return:
        None
    """
    file_name = input(f"File to load: ")
    commands = read_file(file_name)
    constants = {}
    process_commands(commands, constants)


if __name__ == "__main__":
    main()
