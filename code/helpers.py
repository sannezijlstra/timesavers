import copy
EMPTY = '_'
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
            # alleen door horizontale auto's delen!!! 
            return x_score / len(board.cars_dict.values()) 


def red_car_score(board):
    # red_car_score = 0
    return -1 * board.cars_dict['X'].x_location
    # if car.id == 'X':
        # red_car_score = car.x_location
    # return red_car_score

def y_score(board):
    y_score = 0
    car_count = 0
    for car in board.cars_dict.values():
        if not car.horizontal() and car.length < 3:
            car_count += 1
            # je wil de y locatie van een verticaal auto'tje zo ver mogelijk van de x locatie van 'X' hebben
            y_score += y_score + abs(board.cars_dict['X'].y_location + 1 - (car.y_location + 1))
    return -1 * y_score / car_count

def vehicles_before_exit(board):
    redcar = board.cars_dict['X']
    red_x = redcar.x_location
    red_y = redcar.y_location
    car_ids = []
    for index in range(red_x + 2, board.size):
        if board.board[red_y][index] != EMPTY:
            car_ids.append(board.board[red_y][index])
    return car_ids

def minimum_cost(board):
    # correcting for board size and red car length
    minimum_red_steps = board.size - 1 - board.cars_dict['X'].x_location - 1
    
    cars_in_way = vehicles_before_exit(board)
    if not cars_in_way:
        return minimum_red_steps
    elif len(cars_in_way) == 1:
        return minimum_red_steps + 1
    else:
        for car_in_way in cars_in_way:
            if board.cars_dict[car_in_way].length < 3:
                minimum_red_steps += 1
            else:
                if board.cars_dict[car_in_way].y_location == board.cars_dict['X'].y_location - 1:
                    minimum_red_steps += 2
                elif board.cars_dict[car_in_way].y_location == board.cars_dict['X'].y_location - 2 and board.size < 9:
                    minimum_red_steps += 3
                else:
                    minimum_red_steps += 1
    return minimum_red_steps
                    



def find_moves(solution_list, new_board):
    moves_list = []
    for index in reversed(range(len(solution_list))):
        
        new_board.decode_str(solution_list[index])
        first_dict = copy.deepcopy(new_board.cars_dict)
        if first_dict['X'].x_location == 4:
            break

        new_board.decode_str(solution_list[index - 1])
        second_dict = new_board.cars_dict

        for car_id in first_dict.keys():
            first_x =first_dict[car_id].x_location
            first_y = first_dict[car_id].y_location
            second_x = second_dict[car_id].x_location
            second_y = second_dict[car_id].y_location

            if first_x - second_x != 0:
                move = second_x - first_x
                moves_list.append([car_id, move])
                continue
            elif first_y - second_y != 0:
                move = second_y - first_y
                moves_list.append([car_id, move])

    return moves_list

            
            
        

