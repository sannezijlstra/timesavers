import csv
import random
EMPTY = '_'
COLOURS = [x for x in range(8) if x != 1]
CBASE = '\033[9'
CRED = '\033[91m'
CEND = '\033[0m'

class Car():
    def __init__(self, car_id, orientation, x, y, length):
        self.car_id = car_id
        # self.orientation = orientation 
        

        # create car descriptions with colour codes with red reserved for main car
        if self.car_id != 'X':
            colour_num = random.choice(COLOURS)
            self.description = f'{CBASE}{str(colour_num)}m{self.car_id}{CEND}'
        else:
            self.description = f'{CRED}X{CEND}'

        # create orientation boolean for the car
        # DIT KAN WEG TOCH? 

        # if orientation == 'H':
        #     self.horizontal = True
        # else:
        #     self.horizontal = False

        self.location = [int(x) - 1, int(y) - 1]
        self.length = int(length)

        # set redcar boolean for checking if the game is won
        if self.car_id == 'X':
            self.redcar = True
        else:
            self.redcar = False

    def __repr__ (self):
        return self.car_id

    # ONDERSTAANDE WEG HALEN TOT DO_MOVE?
    def can_move_up(self, board):
        if self.location[1] - 1 < 0:
            return False 
        if board.board[self.location[1] - 1 ][self.location[0]] == EMPTY:
            return True
        return False
        
    def can_move_down(self, board, size):
        if self.location[1] + self.length > size - 1:
            return False 
        if board.board[self.location[1] + self.length][self.location[0]] == EMPTY:
            return True
        return False


    def can_move_right(self, board, size):
        if self.location[0] + self.length > size - 1:
            return False
        if board.board[self.location[1]][self.location[0] + self.length] == EMPTY:
            return True
        return False

    def can_move_left(self, board):
        if self.location[0] - 1 < 0:
            return False
        if board.board[self.location[1]][self.location[0] - 1] == EMPTY:
            return True
        return False

    def can_move (self, board, size):
        move_options = []

        if self.horizontal:
            if self.can_move_left(board):
                move_options.append('LEFT')
            if self.can_move_right(board, size):
                move_options.append('RIGHT')
        else: 
            if self.can_move_up(board):
                move_options.append('UP')
            if self.can_move_down(board, size):
                move_options.append('DOWN')

        return move_options

    def do_move(self, direction):
        # if self.valid_move
        if direction == 'UP':
            self.location[1] -= 1
        elif direction == 'DOWN':
            self.location[1] += 1
        elif direction == 'LEFT':
            self.location[0] -= 1
        elif direction == 'RIGHT':
            self.location[0] += 1


