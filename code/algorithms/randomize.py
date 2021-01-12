import random

HORIZONTAL_MOVES = ['LEFT', 'RIGHT']
VERTICAL_MOVES = ['UP', 'DOWN']


def random_move(board, cars_list):
    """
        Choose a random car that can move and make a random move
    """
    cars_that_can = []
    for car in cars_list:
        if car.can_move:
            cars_that_can.append(car)

    car_to_move = random.choice(cars_that_can)
    
    if car_to_move.horizontal:
        direction = random.choice(HORIZONTAL_MOVES)
    else:
        direction = random.choice(VERTICAL_MOVES)
    print(f'{car_to_move} to {direction}')
    board.do_move(car_to_move, direction)
