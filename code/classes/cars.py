import csv
import random
EMPTY = '_'
COLOURS = [x for x in range(8) if x != 1]
CBASE = '\033[9'
CRED = '\033[91m'
CEND = '\033[0m'

class Car():
    def __init__(self, car_id, orientation, x, y, length):
        self.id = car_id
        self.orientation = orientation

        # create car descriptions with colour codes with red reserved for main car
        if self.id != 'X':
            colour_num = random.choice(COLOURS)
            self.description = f'{CBASE}{str(colour_num)}m{self.id}{CEND}'
        else:
            self.description = f'{CRED}X{CEND}'

        # create orientation boolean for the car
        # DIT KAN WEG TOCH? 

        # if orientation == 'H':
        #     self.horizontal = True
        # else:
        #     self.horizontal = False
        self.x_location = x
        self.y_location = y

        self.length = int(length)

        # set redcar boolean for checking if the game is won
        if self.id == 'X':
            self.redcar = True
        else:
            self.redcar = False

    # def __repr__ (self):
    #      return self.id

    def __repr__(self):
        return "'{0}{1}{2}{3}{4}'".format(self.id, self.orientation, self.x_location, self.y_location, self.length)
    
    def car_string(self):
        return "'{0}{1}{2}{3}{4}'".format(self.id, self.orientation, self.x_location, self.y_location, self.length)

    def __hash__(self):
        return hash(self.__repr__())

    def __eq__(self, other):
        return hash(self) == hash(other)

    def horizontal(self):
        return self.orientation == 'H'

    # ONDERSTAANDE WEG HALEN TOT DO_MOVE?
    # def can_move_up(self, board):
    #     if self.y_location - 1 < 0:
    #         return False 
    #     if board.board[self.y_location - 1 ][self.x_location] == EMPTY:
    #         return True
    #     return False
        
    # def can_move_down(self, board, size):
    #     if self.y_location + self.length > size - 1:
    #         return False 
    #     if board.board[self.y_location + self.length][self.x_location] == EMPTY:
    #         return True
    #     return False


    # def can_move_right(self, board, size):
    #     if self.x_location + self.length > size - 1:
    #         return False
    #     if board.board[self.y_location][self.x_location + self.length] == EMPTY:
    #         return True
    #     return False

    # def can_move_left(self, board):
    #     if self.x_location - 1 < 0:
    #         return False
    #     if board.board[self.y_location][self.x_location - 1] == EMPTY:
    #         return True
    #     return False

    # def can_move (self, board, size):
    #     move_options = []
        
    #     if self.horizontal:
    #         if self.can_move_left(board):
    #             move_options.append('LEFT')
    #         if self.can_move_right(board, size):
    #             move_options.append('RIGHT')
    #     else: 
    #         if self.can_move_up(board):
    #             move_options.append('UP')
    #         if self.can_move_down(board, size):
    #             move_options.append('DOWN')

    #     return move_options

    def do_move(self, direction):
        # if self.valid_move
        if direction == 'UP':
            self.y_location -= 1
        elif direction == 'DOWN':
            self.y_location += 1
        elif direction == 'LEFT':
            self.x_location -= 1
        elif direction == 'RIGHT':
            self.x_location += 1


