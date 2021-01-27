from . import cars
import copy

# constant
EMPTY = '_'

class Board():
    """
        Class for supporting the game board of Rush Hour
        Needs a size and list of cars to generate a new game
        (De)serializes the board, loads the cars, checks for possible moves, checks if game is won, and prints current board
    """
    def __init__(self, size, cars_list):
        """
        Initialize the board, determine the size, load list of car objects
        """
        # initialize empty board
        self.board = [list(EMPTY * size) for i in range(size)]
        self.size = size
        self.cars_dict = {}

        # loads cars dictionary out of cars list
        self.load_cars_dict(cars_list)

        # loads cars on board using cars dictionary
        self.load_cars(self.cars_dict)
        self.won = False

    # SOURCE: https://github.com/KaKariki02/rushHour/blob/master/RushClass.py
    def print_board (self):
        """
        Creates a visual representation of the board
        """
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

    def check_move(self, car, max_steps = None):
        """
        Creates a list for every car object, consisting of their possible moves
        """
        # store relevant location depending on car orientation
        if car.horizontal():
            location = car.x_location
        else:
            location = car.y_location
        
        # find positive and negative moves for the car
        positive_moves = self.positive_moves(car, location)
        negative_moves = self.negative_moves(car, location)

        if max_steps:
            positive_moves = min(max_steps, positive_moves)
            negative_moves = min(max_steps, negative_moves)
        
        # combine and return positive and negative move lists for the car object
        return list(range(positive_moves + 1)) + list(x for x in range(0,negative_moves -1, -1))

    def find_possible_boards(self, max_steps = None):
        """
        Finds all possible boards going from the current board
        """
        possible_boards = []
        
        # iterates over the cars in the cars dictionary 
        for car in self.cars_dict.values():
            
            # find all possible moves for the current car
            move_options = self.check_move(car, max_steps)

            # iterates over every possible move
            for move_option in move_options:
                # if the current move option is valid create new board configurations
                if move_option != 0:
                    # create new cars dict to make the move
                    new_cars_dict = copy.deepcopy(self.cars_dict)

                    # find the current car in the copied dictionary and make the move
                    car_to_move = new_cars_dict[car.id]
                    car_to_move.do_move(move_option)

                    # current configuration to the possible boards
                    possible_boards.append(new_cars_dict.values())
        return possible_boards

    def positive_moves(self, car, location, possible_move=0):
        """
        Returns all possible moves going either to the right or downwards in the grid 

        """
        # making sure move does not exceed grid size 
        while location + car.length <= self.size -1:
            # check if the grid location is empty
            if car.horizontal() and self.board[car.y_location][location + car.length] != EMPTY:
                break
            elif not car.horizontal() and self.board[location + car.length][car.x_location] != EMPTY:
                break
            # only adding a possible move when an empty spot is found
            possible_move += 1
            # keep track of the hypothetical car location
            location += 1
            
        return possible_move

    def negative_moves(self, car, location, possible_move=0):
        """
        Returns all possible moves either going left or upwards in the grid
        """
        while location - 1 >= 0:
            # check if the grid location is empty
            if car.horizontal() and self.board[car.y_location][location - 1] != EMPTY:
                break
            elif not car.horizontal() and self.board[location - 1][car.x_location] != EMPTY:
                break
            
            # only adding a negative possible move when an empty spot is found
            possible_move -= 1
            # keep track of the hypothetical car location
            location -= 1
        return possible_move

    def is_won(self):
        """
        Checks whether the red car has found the exit, thus the game has been won
        """
        return self.cars_dict['X'].x_location + 1 == self.size - 1

    def print_board(self):
        """
        Iterate over the board rows and items to print the board
        """
        for row in self.board:
            for item in row:
                if item != "_":
                    item = self.cars_dict[item].description
                print(f'{item} ', end="")
            print()    