import random
import copy
import time
from code import helpers
from code.classes import board, cars

def randomise(new_board):
    """
    Algorithm that solves the Rush Hour game by randomly choosing possible boards, excluding the board that had been chosen last
    
    """
    new_board = copy.deepcopy(new_board)
    loop_count = 0
    last_board_string = None

    while True:
        # TODO MAG DIT WEG?
        # if loop_count == 1000000:
        #     break
        
        # if loop_count % 1000 == 0:
        #     print(f'count:{loop_count}')

        # gives all possible boards from the current board
        possible_boards = new_board.find_possible_boards()

        # if loop_count > 0:
        #     # iterates over all possible boards 
        #     for count, cars_list  in enumerate(possible_boards):
        #         temp = board.Board(new_board.size, cars_list)
                
        #         # excludes the last board, so that cars don't jump forward and backward
        #         if last_board_string == temp.string_repr():
        #             # print(f'last board:')
        #             # new_board.decode_str(last_board_string)
        #             # new_board.print_board()
        #             # print(f'current board:')

        #             # new_board.decode_str(temp.string_repr())
        #             # print()
        #             # new_board.print_board()
        #             check_pop = possible_boards.pop(count)
        #     else:
        #         print('\n no same board found? \n')

        # makes the string representation of the last board


        # a random board out of the possible boards is chosen  
        next_board = random.choice(possible_boards)
        next_board = board.Board(new_board.size, next_board)


        while next_board.string_repr() == last_board_string:
            next_board = random.choice(possible_boards)
            next_board = board.Board(new_board.size, next_board)


        last_board_string = new_board.string_repr()
        new_board = next_board
        # new board object is made, with next_board

        print(f'active_board:')
        new_board.print_board()
        print()
        loop_count += 1
        time.sleep(0.2)
        
        if new_board.is_won():
            print(loop_count)
            return loop_count
        
