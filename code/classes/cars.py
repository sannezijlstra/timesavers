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

    # def load_description(self, cars_list):
    #     colour_count = 0

    #     # iterate over the cars in the list and create a coloured description for each car
    #     for car in cars_list:
    #         # skip number 1 because the colour red is reserved for the main car
    #         if colour_count % 7 == 1:
    #             colour_count += 1
            
    #         # assign colour red if the current car is the main car
    #         if car.car_id == 'X':
    #             car.description = f'{CRED}X{CEND}'
    #         else:
    #             # dynamicly assign colour to the current car
    #             car.description = f'{CBASE}{str(colour_count % 7)}m{car.car_id}{CEND}'