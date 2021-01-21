from . import cars
import copy

EMPTY = '_'

# CRED = '\033[91m'
# CEND = '\033[0m'

class Board():
    """
        Class for supporting the game of rush hour,
        needs a size and list of cars to generate a new game
    """
    def __init__(self, size, cars_list):
        # initialize empty board
        self.board = [list(EMPTY * size) for i in range(size)]
        self.size = size
        self.cars_dict = {}
        self.load_cars_dict(cars_list)
        self.load_cars(self.cars_dict)
        self.won = False

    # SOURCE: https://github.com/KaKariki02/rushHour/blob/master/RushClass.py
    def print_board (self):
        """TODO kijken in git history voor hoe we dit deden met kleur"""
        self.printboard = '\n\n'.join(['      '.join(['{}'.format(item) for item in row]) for row in self.board])
        return self.printboard
    
    def string_repr(self):
        """
        Serializes board object into string
        """
        string_repr = ""

        # iterates over every row in board grid
        for row in range(self.size):
            # iterates over every column in board grid
            for column in range(self.size):
                # string keeps extending with every spot in the grid, splitting based on location, description and item
                string_repr = string_repr + str(column) + ',' + str(row) + '.' + self.board[row][column] + '-'
        return string_repr

    def decode_str(self, string_repr):
        """
        Decodes serialized board object
        """
        self.board = [list(EMPTY * self.size) for i in range(self.size)]
        
        # set all car location values to None to be able to create new locations for the car objects
        for car in self.cars_dict.values():
            car.x_location = None
            car.y_location = None

        found_cars = []
        # separates every item from one another
        locations = string_repr.split('-')

        for location in locations:
            # separates every location from its description
            filled = location.split('.')

            # fills board with newly located cars
            if len(filled) > 1 and filled[1] != EMPTY:
                coordinates = filled[0].split(',')
                x = int(coordinates[0])
                y = int(coordinates[1])
                self.board[y][x] = filled[1]

                # fills the rest of the board with the existing empty lower dashes
                if filled[1] not in found_cars:
                    found_cars.append(filled[1])
                    self.cars_dict[filled[1]].x_location = x
                    self.cars_dict[filled[1]].y_location = y

    def load_cars_dict(self, cars_list):
        """
        Fills dictionary with car objects
        """
        for car in cars_list:
            self.cars_dict[car.id] = car

    def load_cars(self, cars_dict):
        """
        Function to load cars into the game grid, fills the grid with the letters belonging to the cars
        """
        for car in cars_dict.values():

            # load the board with description on initial car location
            self.board[car.y_location][car.x_location] = car.id

            # load the rest of the car object in horizontal or vertical direction
            if car.horizontal():
                self.board[car.y_location][car.x_location + 1] = car.id
                # if car is a truck load another space in grid with object
                if car.length > 2:
                    self.board[car.y_location][car.x_location + 2] = car.id
            else:
                self.board[car.y_location + 1][car.x_location] = car.id
                if car.length > 2:
                    self.board[car.y_location + 2][car.x_location] = car.id

    def check_move_up(self, car):
        # TODO! DEZE FUNCTIES OMSCHRIJVEN TOT 1
        """
        Checks whether the location one step above the car is empty
        """
        # kunnen we hier gebruik maken van de car_object?
        if car.y_location - 1 < 0:
            return False 
        return self.board[car.y_location - 1 ][car.x_location] == EMPTY
        
    def check_move_down(self, car):
        """
        Checks whether the location one step below the car is empty
        """
        if car.y_location + car.length > self.size - 1:
            return False 
        return self.board[car.y_location + car.length][car.x_location] == EMPTY

    def check_move_right(self, car):
        """
        Checks whether the location one step right of the car is empty
        """
        if car.x_location + car.length > self.size - 1:
            return False
        return self.board[car.y_location][car.x_location + car.length] == EMPTY

    def check_move_left(self, car):
        """
        Checks whether the location one step left of the car is empty
        """
        if car.x_location - 1 < 0:
            return False
        return self.board[car.y_location][car.x_location - 1] == EMPTY

    def check_move(self, car):
        """
        Creates a list for every car object, consisting of their possible moves
        """
        move_options = []
        
        if car.horizontal():
            if self.check_move_left(car):
                move_options.append('LEFT')
            if self.check_move_right(car):
                move_options.append('RIGHT')
        else: 
            if self.check_move_up(car):
                move_options.append('UP')
            if self.check_move_down(car):
                move_options.append('DOWN')
        return move_options

    def find_possible_boards(self):
        """
        Finds all possible boards going from the current board
        """
        possible_boards = []
        
        # iterates over the cars in the cars dictionary 
        for car in self.cars_dict.values():

            move_options = self.check_move(car)

            # check if car can move 
            if len(move_options) > 0:
                # make a copy of the existing cars dictionary 
                new_cars_dict = copy.deepcopy(self.cars_dict)
            else:
                continue
            
            # vind de huidige auto in de kopie dictionary en beweeg deze
            # find the 
            new_cars_dict[car.id].do_move(move_options[0])

            # voeg de lijst met bewogen auto's hier aan toe
            possible_boards.append(new_cars_dict.values())

            # als de auto twee kanten op kan maak nieuwe kopie aan
            if len(move_options) > 1:
                other_cars_dict = copy.deepcopy(self.cars_dict)
                # beweeg de auto en voeg lijst met auto's toe aan possible boards
                other_cars_dict[car.id].do_move(move_options[1])
                possible_boards.append(other_cars_dict.values())

        return possible_boards
        
    def is_won(self):
        """
        """
        return self.cars_dict['X'].x_location + 1 == self.size - 1

    def print_board(self):
        """
            iterate over the board rows and items to print the board
        """
        # checken of item _ is
        # anders print item = carid (description heeft kleur)
        for row in self.board:
            for item in row:
                print(item)
                #print(f'{item} ', end="")
            print()
    

    def positive_moves(self, car, location, possible_move=0):
        while location + car.length <= self.size -1:
            if car.horizontal() and self.board[car.y_location][location + car.length] != EMPTY:
                break
            elif not car.horizontal() and self.board[location + car.length][car.x_location] != EMPTY:
                break
            possible_move += 1
            location += 1
            self.positive_moves(car, location, possible_move)
            # can move right or down
        return possible_move

    
    def negative_moves(self, car, location, possible_move=0):

        while location - 1 >= 0:
            if car.horizontal() and self.board[car.y_location][location - 1] != EMPTY:
                break
            elif not car.horizontal() and self.board[location - 1][car.x_location] != EMPTY:
                break
            possible_move -= 1
            location -= 1
            self.negative_moves(car, location, possible_move)
        return possible_move



