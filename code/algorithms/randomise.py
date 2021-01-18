import random

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
    car_to_move.do_move(board, direction)
    return [car_to_move, direction]
