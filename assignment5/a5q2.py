"""
Name: Connor Morrison
NSID: tvi340
Student Number: 11374770
Course Number: CMPT 145
Lecture Section: 04
Laboratory Section: L02
"""

import Queue as Queue


def read_file(file_path):
    """
    Purpose:
        Read monster names from file and store them in a list.
    Pre-conditions:
        file_path: String representing path to file containing monster names.
    Post-conditions:
        none
    Return:
        List of strings, each representing a monster name read from the file.
    """
    monsters = []
    with open(file_path, "r") as file:
        for line in file:
            formatted_line = line.strip()
            monsters.append(formatted_line)

    return monsters


def simulate_battle(monsters):
    """
    Purpose:
        Simulate battle between monsters, Godzilla and Mothra defeat the monsters in a queue.
    Pre-conditions:
        monsters: List of strings representing monsters, including "Godzilla" and "Mothra" which defeat first monster in
         queue.
    Post-conditions:
        Modifies queue of monsters, removing monsters defeated by Godzilla or Mothra.
        Updates dictionaries to count number of monsters defeated by Godzilla and Mothra.
    Return:
        Tuple containing two dictionaries mapping defeated monsters and times defeated, and modified queue of monsters.
    """
    queue = Queue.Queue()
    godzilla_defeated_dict = {}
    mothra_defeated_dict = {}

    for monster in monsters:
        if monster not in ["Godzilla", "Mothra"]:
            queue.enqueue(monster)
        else:
            if not queue.is_empty():
                first_monster = queue.dequeue()
                if monster == "Godzilla":
                    godzilla_defeated_dict[first_monster] = godzilla_defeated_dict.get(first_monster, 0) + 1
                elif monster == "Mothra":
                    mothra_defeated_dict[first_monster] = mothra_defeated_dict.get(first_monster, 0) + 1

    return godzilla_defeated_dict, mothra_defeated_dict, queue


def display_results(godzilla_defeated, mothra_defeated, queue):
    """
    Purpose:
        Display results of monster battles, including monsters defeated by Godzilla and Mothra, and which monsters
        remain undefeated.
    Pre-conditions:
        godzilla_defeated: Dictionary of monster names and number of times defeated by Godzilla.
        mothra_defeated: Dictionary of monster names and number of times defeated by Mothra.
        queue: Queue object containing any remaining monsters not defeated.
    Post-conditions:
        Prints battle outcomes to console, including names and defeat counts of monsters defeated by Godzilla and Mothra,
        and the names of any remaining monsters.
    Return:
        none
    """
    if queue.is_empty():
        print("The space monsters were beaten!")
        print("\n")
        if godzilla_defeated:
            for monster, count in godzilla_defeated.items():
                print(f"Godzilla defeated: {monster}: {count}")
            print("\n")
        if mothra_defeated:
            for monster, count in mothra_defeated.items():
                print(f"Mothra defeated: {monster}: {count}")
    else:
        remaining_monsters = []
        while not queue.is_empty():
            remaining_monsters.append(queue.dequeue())
        print("Oh no! The space monsters won thanks to", ', '.join(remaining_monsters))


if __name__ == "__main__":
    file_name = "monsters1.txt"
    monsters_list = read_file(file_name)
    godzilla_results, mothra_results, remaining_queue = simulate_battle(monsters_list)
    display_results(godzilla_results, mothra_results, remaining_queue)
