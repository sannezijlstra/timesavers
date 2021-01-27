import copy
import csv
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

def combination_score(new_board):
    x_score = 0
    y_score = 0
    car_count_x = 0 
    car_count_y = 0
    red_car_score = -1 * new_board.cars_dict['X'].x_location

    for car in new_board.cars_dict.values():
        if car.horizontal() and car.id != 'X':
            car_count_x += 1 
            x_score += car.x_location 
            # alleen door horizontale auto's delen!!! 
        elif not car.horizontal() and car.length < 3:
            car_count_y += 1
            # je wil de y locatie van een verticaal auto'tje zo ver mogelijk van de x locatie van 'X' hebben
            y_score += y_score + abs(new_board.cars_dict['X'].y_location + 1 - (car.y_location + 1))
    
    total_x_score = x_score / car_count_x 
    total_y_score = -1 * y_score / car_count_y

    return (total_x_score + total_y_score + red_car_score)


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
    print(f'red steps to make to exit{minimum_red_steps}')
    if not cars_in_way:
        return minimum_red_steps
    elif len(cars_in_way) == 1:
        if board.is_blocked(board.cars_dict[cars_in_way[0]]):
            print(f'car/truck is blocked {minimum_red_steps + 1}')
            minimum_red_steps += 1
        print(f'car in front red{ minimum_red_steps + 1}')
        return (minimum_red_steps + 1)
    else:
        for car_in_way in cars_in_way:
            if board.cars_dict[car_in_way].length < 3:
                minimum_red_steps += 1
                print(f'one of few cars in front {minimum_red_steps + 1} ')
            else:
                if board.cars_dict[car_in_way].y_location == board.cars_dict['X'].y_location - 1:
                    print(f'one of truck type 1 {minimum_red_steps +1} ')
                    minimum_red_steps += 2
                elif board.cars_dict[car_in_way].y_location == board.cars_dict['X'].y_location - 2 and board.size < 9:
                    print(f'one of truck type 2 {minimum_red_steps +1} ')
                    minimum_red_steps += 3
                else:
                    print(f'one of truck type 3 {minimum_red_steps +1} ')
                    minimum_red_steps += 1
            if board.is_blocked(board.cars_dict[car_in_way]):
                print(f' blocked penalty {minimum_red_steps + 1}')
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
    
def output(solution_list, newest_board ):
    moves_list = find_moves(solution_list, newest_board)
    #print(moves_list)      
    fields = ['car', 'move']
    # writing the data into the file 
    with open('output.csv','w') as f:
    # with open  file:     
        wr = csv.writer(f)
        wr.writerow(fields)
        wr.writerows(moves_list)        

    return f  

            
        

