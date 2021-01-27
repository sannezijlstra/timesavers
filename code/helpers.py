import copy
import csv
import time

#constant
EMPTY = '_'

# ---------------- Combination score heuristic for Beam Search -------------------------
def combination_score(new_board):
    """
    Combines three heuristic scores for pruning the list in beam search 
    X-score consists of x-coordinates of horizontal cars, excluding the red car
    Y-score consists of y-coordinates of vertical cars, opposed to the y-coordinate of the red car
    """
    x_score = 0
    y_score = 0
    car_count_x = 0 
    car_count_y = 0

    # x-coordinates of the red car, multiplying by -1 because pruned from low to high score, here, higher is better
    red_car_score = -1 * new_board.cars_dict['X'].x_location

    # iterates over every car object
    for car in new_board.cars_dict.values():
        if car.horizontal() and car.id != 'X':
            car_count_x += 1 
            x_score += car.x_location 
        elif not car.horizontal() and car.length < 3:
            car_count_y += 1
            # the y-coordinates of the vertical cars, which need to be furthest from the y-coordinate of the red car
            y_score += y_score + abs(new_board.cars_dict['X'].y_location + 1 - (car.y_location + 1))
    
    # average x-coordinate for every horizontal car, the lower the better
    total_x_score = x_score / car_count_x 
    
    # average y-score for every vertical car, multiplying by -1 because pruned from low to high score, here, higher is better
    total_y_score = -1 * y_score / car_count_y

    return (total_x_score + total_y_score + red_car_score)

# ------------------- Functions to apply minimum cost heuristic for Beam Search algorithm -----------------
def minimum_cost(board):
    """
    Calculates an approximation of the minimum steps needed for the red car to make it to the destination.
    """
    # correcting for board size and red car length
    minimum_red_steps = board.size - 1 - board.cars_dict['X'].x_location - 1

    # find vertical cars that block the path of the red car
    cars_in_way = vehicles_before_exit(board)
    # if there are no cars in the red cars way, the distance to the destination is the minimum steps
    if not cars_in_way:
        return minimum_red_steps
    else:
        # iterate over the cars and calculate how they influence the minimum steps
        for car_in_way in cars_in_way:
            # cars of length 2 always increase the minimum steps by 1
            if board.cars_dict[car_in_way].length < 3:
                minimum_red_steps += 1
            else:
                # trucks can influence the red cars path in 3 ways
                if board.cars_dict[car_in_way].y_location == board.cars_dict['X'].y_location - 1:
                    minimum_red_steps += 2
                # special case for the 6x6 board
                elif board.cars_dict[car_in_way].y_location == board.cars_dict['X'].y_location - 2 and board.size == 6 :
                    minimum_red_steps += 3
                else:
                    minimum_red_steps += 1
                    
        # if the cars are blocked themselves, calculate a blocked score
        blocked_score = blocked_chain(set(cars_in_way), board)

        # use code below to exclude blockage in heuristic
        # blocked_score = len(cars_in_way)

    return minimum_red_steps + blocked_score

def vehicles_before_exit(board):
    """
    Determines the amount of vehicles that are in the way of the red car's destination 
    """
    redcar = board.cars_dict['X']
    red_x = redcar.x_location
    red_y = redcar.y_location
    car_ids = []
    # iterates over the grid spots on the right side of the red car
    for index in range(red_x + 2, board.size):
        # appends to a list when a car is on the right side of the red car
        if board.board[red_y][index] != EMPTY:
            car_ids.append(board.board[red_y][index])
    return car_ids

def is_v_blocked (new_board, car):
    """
    Checks whether a vertical orientated car is blocked by other cars
    """
    # car is not at the edge
    if car.y_location > 0 and car.y_location + car.length < new_board.size:
        # check if car is blocked by cars
        return new_board.board[car.y_location - 1][car.x_location] != EMPTY and new_board.board[car.y_location + car.length][car.x_location] != EMPTY
    if car.y_location > 0 and car.y_location + car.length == new_board.size:
        # check if car is blocked between car and edge
        return new_board.board[car.y_location - 1][car.x_location] != EMPTY
    # check if car is blocked between car and edge
    return new_board.board[car.y_location + car.length][car.x_location] != EMPTY

def is_h_blocked(new_board,car):
    """
    Checks whether a horizontal orientated car is blocked by other cars
    """
    # check if the car is blocked between two cars
    if car.x_location > 0 and car.x_location + car.length < new_board.size:
        return new_board.board[car.y_location][car.x_location - 1] != EMPTY and new_board.board[car.y_location][car.x_location + car.length] != EMPTY
    # check if the car is blocked between car and edge
    if car.x_location > 0 and car.x_location + car.length == new_board.size:
        return new_board.board[car.y_location][car.x_location - 1] != EMPTY
    # check if the car is blocked between car and edge
    return new_board.board[car.y_location][car.x_location + car.length] != EMPTY

def blocked_chain(pot_blocked_cars, new_board):
    """
        Checks if cars are blocked, and for vertical check if bordering cars are blocked themselves
        Needs car-id list and board as input
        Returns the amount of cars blocked
    """
    
    blocked_cars = set()
    
    # check for blocked cars as long as there are potential blocked cars 
    while pot_blocked_cars:
        for car_id in list(pot_blocked_cars):
            # the red car does not count for the blocking car score
            if car_id == 'X':
                pot_blocked_cars.remove(car_id)
                continue

            car = new_board.cars_dict[car_id] 

            # if horizontal and blocked add it to the blocked cars
            if car.horizontal() and is_h_blocked(new_board, car):
                blocked_cars.add(car.id)

            # if the car is vertical add it to the blocked cars and find bordering cars
            elif not car.horizontal() and is_v_blocked(new_board, car):
                # look above the car if car is not at the top edge
                if car.y_location > 0:
                    pot_blocked_car = new_board.board[car.y_location - 1][car.x_location]
                    # only add potential blocked car if the car is not in the blocked cars list
                    if pot_blocked_car not in blocked_cars:
                        pot_blocked_cars.add(pot_blocked_car)

                # look below the car if the car is not at the bottom edge
                if car.y_location + car.length  < new_board.size:
                    pot_blocked_car = new_board.board[car.y_location + car.length][car.x_location]
                    # only add potential blocked car if not present in blocked cars
                    if pot_blocked_car not in blocked_cars:
                        pot_blocked_cars.add(pot_blocked_car)
                    # add blocked car
                    pot_blocked_cars.add(pot_blocked_car)
                # add the current blocked car
                blocked_cars.add(car.id)
            
            pot_blocked_cars.remove(car_id)
            
    return len(blocked_cars)

# ----------- Functions concerning representation of output ----------------------
def find_solution_moves(solution_list, new_board):
    """
    Based on boardstrings, find the moves made to get the red car to the destination
    These can be used to produce the output file
    """
    moves_list = []
    # iterate over the range of the parent boardstring list
    for index in reversed(range(len(solution_list))):
        
        # load the board and copy dictionary of the current car configuration
        new_board.decode_str(solution_list[index])
        first_dict = copy.deepcopy(new_board.cars_dict)

        # if the current board contains the solution break from iteration
        if first_dict['X'].x_location == new_board.size - 2:
            break

        # decode the next boardstring and copy the next car configuration
        new_board.decode_str(solution_list[index - 1])
        second_dict = new_board.cars_dict

        # iterate over the first car dictionary and compare it with the second car dictionary
        for car_id in first_dict.keys():
            first_x =first_dict[car_id].x_location
            first_y = first_dict[car_id].y_location
            second_x = second_dict[car_id].x_location
            second_y = second_dict[car_id].y_location
            
            # for x and y, a move has been made if the subtracted result is not zero
            if first_x - second_x != 0:
                move = second_x - first_x
                moves_list.append([car_id, move])
                continue
            elif first_y - second_y != 0:
                move = second_y - first_y
                moves_list.append([car_id, move])

    return moves_list

def output(solution_list, newest_board ):
    """
    Creates a csv file consisting of all necessary moves made, when a solution is found
    """
    # get the list of all the moves that are made
    moves_list = find_solution_moves(solution_list, newest_board)
    fields = ['car', 'move']
    
    # writing the data into the file 
    with open("output/output.csv", 'w') as f: 
        wr = csv.writer(f)
        wr.writerow(fields)
        wr.writerows(moves_list)

    return f

def generate_output(result, new_board):
    """
    Handles results of algorithms: BreadthFirst, DepthFirst, BeamSearch
    """
    newest_board = copy.deepcopy(new_board)
    solution_list = result['solution']
    solve_time = result['solve_time']
    count = result['count']
    for solution in reversed(solution_list):
        newest_board.decode_str(solution)
        print()
        newest_board.print_board()
        print()
        time.sleep(0.1)

    print("solved in: {0:.3f} seconds".format(solve_time), end="")
    print(f' with {len(solution_list)} steps')
    print(f' with {count} children analysed ')

    return output(solution_list, newest_board)