import random
from code import helpers
from code.classes import board, cars

HORIZONTAL_MOVES = ['LEFT', 'RIGHT']
VERTICAL_MOVES = ['UP', 'DOWN']


def random_move(board, cars_that_can):
    """
        Choose a random car that can move and make a random move
    """

    car_to_move = random.choice(list(cars_that_can.keys()))

    
    if car_to_move.horizontal:
        direction = random.choice(cars_that_can[car_to_move])
    else:
        direction = random.choice(cars_that_can[car_to_move])

    print(f'{car_to_move} to {direction}')
    car_to_move.do_move(direction)
    return [car_to_move, direction]

def run_random(new_board, cars_list):
    count = 0
    while True:
        new_board.print_board()

        cars_that_can = helpers.find_cars_that_can(cars_list, new_board)

        if count > 0:
            if len(cars_that_can[reversed_move[0]]) == 2:
                cars_that_can[reversed_move[0]].remove(reversed_move[1])
            else:
                del cars_that_can[reversed_move[0]]
                
        last_move = random_move(new_board, cars_that_can)
        
        reversed_move = [last_move[0], helpers.reverse_move(last_move[1])]

        # move car if possible -> waarschijnlijk in random.py
        # if not new_board.do_move(direction, car_to_move):
        #     print('illegal move')
        #     continue
        
        # if game is won break out of loop
        new_board.check_won(cars_list)

        if new_board.is_won():
            print('congrats you won')
            print(f'Count: {count}')
            new_board = board.Board(new_board.size, cars_list, True)
            new_board.print_board()
            break

        # reload the board
        new_board = board.Board(new_board.size, cars_list)
        
        count += 1
        if count == 1000000:
            break
        if count % 100 == 0:
            print(count)
    return count
