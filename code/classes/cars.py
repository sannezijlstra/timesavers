import csv

class Car():
    def __init__(self, car_id, orientation, x, y, length):
        self.car_id = car_id
        if orientation == 'H':
            self.horizontal = True
        else:
            self.horizontal = False

        self.location = (int(x), int(y))
        self.length = length

        if self.car_id == 'X':
            self.redcar = True
        else:
            self.redcar = False

    def __repr__ (self):
        return self.car_id