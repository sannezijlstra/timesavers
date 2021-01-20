def reverse_move(direction):
    if direction == 'UP':
        return 'DOWN'
    elif direction == 'DOWN':
        return 'UP'
    elif direction == 'RIGHT':
        return 'LEFT'
    else:
        return 'RIGHT'


def find_cars_that_can(cars_list, new_board):
    cars_that_can = {}
    
    for car in cars_list:
        ## TODO can_move functie size oplossen
        result = car.can_move(new_board, new_board.size)
        if result:
            cars_that_can[car] = result
    return cars_that_can


def x_score(board):
    x_score = 0
    for car in board.cars_dict.values():
        if car.horizontal() and car.id != 'X':
            x_score += car.x_location 
    return x_score