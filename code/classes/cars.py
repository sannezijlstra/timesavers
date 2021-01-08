import csv
import colorama
from colorama import Fore, Back, Style
from stringcolor import * 
colorama.init(autoreset=True)
BLUE = '\033[94m'
ENDC = '\033[0m'

CRED = '\033[91m'
CEND = '\033[0m'

class Car():
    def __init__(self, car_id, orientation, x, y, length):
        self.car_id = car_id
        if orientation == 'H':
            self.horizontal = True
        else:
            self.horizontal = False

        self.location = [int(x) - 1, int(y) - 1]
        self.length = int(length)

        if self.car_id == 'X':
            self.redcar = True
            #print(Fore.RED + 'X')
            # self.car_id = CRED + 'X' + CEND
            
            #self.car_id = BLUE + 'X' + ENDC
        else:
            self.redcar = False

    def __repr__ (self):
        return self.car_id