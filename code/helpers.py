# TODO nog nodig???
def reverse_move(direction):
    if direction == 'UP':
        return 'DOWN'
    elif direction == 'DOWN':
        return 'UP'
    elif direction == 'RIGHT':
        return 'LEFT'
    else:
        return 'RIGHT'

# TODO nog nodig???
def find_cars_that_can(cars_list, new_board):
    cars_that_can = {}
    
    for car in cars_list:
        ## TODO can_move functie size oplossen
        result = car.can_move(new_board, new_board.size)
        if result:
            cars_that_can[car] = result
    return cars_that_can


def x_score(board):
    """
    Determines the x score of a car, by adding all x-coordinates of the horizontal cars
    This is used in the heuristic in breadth first search where we keep taking the possible board where the x-score is the lowest
    """
    x_score = 0
    # iterates over all cars
    for car in board.cars_dict.values():
        if car.horizontal() and car.id != 'X':
            x_score += car.x_location 
            return x_score  


def red_car_score(board):
    # red_car_score = 0
    return board.cars_dict['X'].x_location
    # if car.id == 'X':
        # red_car_score = car.x_location
    # return red_car_score

def y_score(board):
    y_score = 0
    for car in board.cars_dict.values():
        if not car.horizontal() and car.length < 3:
            # je wil de y locatie van een verticaal auto'tje zo ver mogelijk van de x locatie van 'X' hebben
            y_score += y_score + abs(board.cars_dict['X'].y_location + 1 - (car.y_location + 1))
    return y_score