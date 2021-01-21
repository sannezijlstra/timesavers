import csv
import random
EMPTY = '_'
COLOURS = [x for x in range(8) if x != 1]
CBASE = '\033[9'
CRED = '\033[91m'
CEND = '\033[0m'

class Car():
    """
    Class for creating all car objects
    """

    def __init__(self, car_id, orientation, x, y, length):
        """
        Initialize car objects
        """
        self.id = car_id
        self.orientation = orientation

        # create car descriptions with colour codes with red reserved for main car
        if self.id != 'X':
            colour_num = random.choice(COLOURS)
            self.description = f'{CBASE}{str(colour_num)}m{self.id}{CEND}'
        else:
            self.description = f'{CRED}X{CEND}'

        self.x_location = x
        self.y_location = y

        self.locations = [] 

        self.length = int(length)

        # set redcar boolean for checking if the game is won
        if self.id == 'X':
            self.redcar = True
        else:
            self.redcar = False
    def __repr__(self):
            """
            Returns string representation of car object
            """
            return "'{0}{1}{2}{3}{4}'".format(self.id, self.orientation, self.x_location, self.y_location, self.length)

    def horizontal(self):
        """
        Checks whether car is in horizontal orientation
        """
        return self.orientation == 'H'

    def do_move(self, move):
        """
        The car objects do the actual moves 
        """
        if self.horizontal():
            self.x_location += move
        else:
            self.y_location += move


