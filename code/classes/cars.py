import csv
import random

BLUE = '\033[94m'
ENDC = '\033[0m'

COLOURS = [x for x in range(8) if x != 1]
CBASE = '\033[9'
CRED = '\033[91m'
CEND = '\033[0m'

class Car():
    def __init__(self, car_id, orientation, x, y, length):
        self.car_id = car_id

        if self.car_id != 'X':
            colour_num = random.choice(COLOURS)
            self.description = f'{CBASE}{str(colour_num)}m{self.car_id}{CEND}'
        else:
            self.description = f'{CRED}X{CEND}'


        if orientation == 'H':
            self.horizontal = True
        else:
            self.horizontal = False

        self.location = [int(x) - 1, int(y) - 1]
        self.length = int(length)

        if self.car_id == 'X':
            self.redcar = True
        else:
            self.redcar = False

    def __repr__ (self):
        return self.car_id