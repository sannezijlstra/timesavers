import random
import copy
import time
from code import helpers
from code.classes import board, cars

def randomise(new_board):
    """
    Algorithm that solves the Rush Hour game by randomly choosing possible boards.
    Excludes the board that had been chosen in the last move.
    """
    new_board = copy.deepcopy(new_board)
    loop_count = 0
    
    # starting board has no previous board string yet
    last_board_string = None

    while True:
        # TODO MAG DIT WEG?
        # if loop_count == 1000000:
        #     break
        
        # if loop_count % 1000 == 0:
        #     print(f'count:{loop_count}')

        # gives all possible boards from the current board
        possible_boards = new_board.find_possible_boards()

        # a random board out of the possible boards is chosen  
        next_board = random.choice(possible_boards)

        # a board object is created for the chosen possible board
        next_board = board.Board(new_board.size, next_board)


        # if the newly chosen board is the same as the last board, a new random choice is made 
        while next_board.string_repr() == last_board_string:
            next_board = random.choice(possible_boards)
            next_board = board.Board(new_board.size, next_board)


        last_board_string = new_board.string_repr()
        new_board = next_board
        # new board object is made, with next_board

        # TODO ONDERSTAANDE ALLEMAAL LATEN STAAN?
        print(f'active_board:')
        new_board.print_board()
        print()
        loop_count += 1
        time.sleep(0.2)
        
        # end while True loop when game is won and return the number of moves made
        if new_board.is_won():
            print(loop_count)
            return loop_count