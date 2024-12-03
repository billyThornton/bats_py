import pytest


class TestReport:
    def __init__(self, filename):
        self.filename = filename
        # Create the file in the initializer
        with open(self.filename, 'w') as f:
            f.write("Test Report\n")
            f.write("===========\n\n")

    def add_message(self, message):
        # Open the file in append mode and add the message
        with open(self.filename, 'a') as f:
            f.write(message + "\n")


def is_list_of_lists(obj, subtype):
    """
    Used to test if an object is a list of lists of a certain type
    """
    if not isinstance(obj, list):
        return False
    for sublist in obj:
        if not isinstance(sublist, list):
            return False
        if not all(isinstance(item, subtype) or item is None for item in sublist):
            return False
    return True


def is_dict_of_type(obj, key_type, value_type):
    """
    Used to test if an object is a dictionary of a certain type
    """
    if not isinstance(obj, dict):
        return False
    for key, value in obj.items():
        if not isinstance(key, key_type) or not isinstance(value, value_type):
            return False
    return True


def tuple_of_type(obj, type1, type2):
    """
    Used to test if an object is a tuple of a certain type
    """
    if not isinstance(obj, tuple):
        return False
    for item in obj:
        if not isinstance(item, type1) and not isinstance(item, type2):
            return False
    return True


def ships_are_continuous(board, ships):
    """
    Checks if the ship is continuous and returns True if all the square are present in the line.
    Checks for both vertical and horizontal orientation and also returns a second boolean True if the ship is horizontal.
    :param board:
    :param starting_coord:
    :param ship_length:
    :return:
    """

    orientaitons = []
    continuous = []
    try:
        for ship, length in ships.items():
            ships_start_x = 0
            ships_start_y = 0
            # Get the starting coord of the ship = first time the ship appears on the board
            for y, row in enumerate(board):
                if ship in row:
                    x = row.index(ship)
                    ships_start_x = x
                    ships_start_y = y
                    break

            horizontal_spaces = [board[ships_start_y][ships_start_x + i] for i in range(length)]
            if all([space == ship for space in horizontal_spaces]):
                orientaitons.append(True)
                continuous.append(True)

            vertical_spaces = [board[ships_start_y + i][ships_start_x] for i in range(length)]
            if all([space == ship for space in vertical_spaces]):
                orientaitons.append(False)
                continuous.append(True)
        return continuous, orientaitons

    except IndexError:
        return [], []
