import csv
import random

<<<<<<< HEAD
=======
COLOURS = [x for x in range(8) if x != 1]
CBASE = '\033[9'
CRED = '\033[91m'
CEND = '\033[0m'

>>>>>>> b39af9eb14bb7f9dd1d24855459445340157d395
class Car():
    def __init__(self, car_id, orientation, x, y, length):
        self.car_id = car_id
        self.can_move = False

        # create car descriptions with colour codes with red reserved for main car
        if self.car_id != 'X':
            colour_num = random.choice(COLOURS)
            self.description = f'{CBASE}{str(colour_num)}m{self.car_id}{CEND}'
        else:
            self.description = f'{CRED}X{CEND}'

        # create orientation boolean for the car
        if orientation == 'H':
            self.horizontal = True
        else:
            self.horizontal = False

        self.location = [int(x) - 1, int(y) - 1]
        self.length = int(length)

        # set redcar boolean for checking if the game is won
        if self.car_id == 'X':
            self.redcar = True
        else:
            self.redcar = False

    def __repr__ (self):
        return self.car_id