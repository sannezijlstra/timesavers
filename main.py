from code.classes import board, cars
from code.algorithms import randomise, breadth_first, depth_first, depth_first2
from code import helpers
import csv
import copy
import time
import random
import os
import sys

import sys
sys.setrecursionlimit(1500)

# TODO 12x12 grid auto's hebben 2 letterige id
############################ RANDOM #############################
def run_random(board, cars_list):
    new_board = board.Board(size, cars_list)
    solution_count = randomise.randomise(new_board)
    print(f'board {for_6} solved pseudorandomly in {solution_count} steps')

############################ BREADTH FIRST #############################
def run_breadth_first(new_board, cars_list):
    new_board = board.Board(size, cars_list)
    
    breadth = breadth_first.BreadthFirst(new_board)
    print('begin run')
    result = breadth.run()
    # print(result)
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

############################# DEPTH FIRST #############################
def run_depth_first(board, cars_list):
    new_board = board.Board(size, cars_list)
    # print(result)

    newest_board = copy.deepcopy(new_board)
    depth_obj = depth_first2.DepthFirst(new_board)
    print('begin run')
    result = depth_obj.run()
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
    print(f' number of children analysed: {count}')

if __name__ == "__main__":
    # prompt user for data file size and select file from data folder
    while True:
        try:
            size = int(input("> what size (6, 9 or 12) grid would you like? "))
        except ValueError:
            print("invalid input")
            continue

        # for_6 = random.randint(1,3)
        for_6 = random.randint(1,3)
        for_9 = random.randint(4,6)
        
        try:
            file_nr = int(input("> type file number if you'd like "))
        except ValueError:
            file_nr = None
        
        
            


        # save file path depending on the size
        if size == 6:
            if file_nr and file_nr in range(1,3):
                for_6 = file_nr
                print(f'file {for_6} for size {size} is loaded')
            else:
                print(f'file {for_6} was selected randomly for size {size}')
            file_to_open = f'data/6x6_grids/Rushhour6x6_{for_6}.csv'
            break
        elif size == 9:
            if file_nr and file_nr in range(4,6):
                for_9 = file_nr
                print(f'file {for_9} for size {size} is loaded')
            else:
                print(f'file {for_9} was selected randomly for size {size}')
            file_to_open = f'data/9x9_grids/Rushhour9x9_{for_9}.csv'
            break
        elif size == 12:
            print('file with grid size 12 is loaded')
            file_to_open = f'data/12x12_grids/Rushhour12x12_7.csv'
            break
        else:
            print('invalid size')
    # create empty list to fill with cars
    cars_list = []

    # open data folder to create car objects
    if os.path.isfile(file_to_open) and os.path.getsize(file_to_open) > 0:
        with open(file_to_open, 'r') as in_file:
            car_file = csv.DictReader(in_file)
            for line in car_file:
                # create new car object and append it to list
                new_car = cars.Car(line['car'], line['orientation'],int(line['row']) - 1 ,int(line['col']) - 1,line['length'])
                cars_list.append(new_car)
    else:
        sys.exit("data file is empty or does not exist")

    # create initial board 
    algorithm_choices = {'run random': run_random, 'breadth_first': run_breadth_first, 'depth_first': run_depth_first}

    alg_choice = input(f'select algrorithm from {algorithm_choices.keys()}')
    algorithm_choices[alg_choice](board, cars_list)






############################# NIET WERKENDE DEPTH FIRST #############################
    # new_board = board.Board(size, cars_list)
    
    # depth_obj = depth_first.DepthFirst(new_board)
    # print('begin run')
    # result = depth_obj.run()
    # # print(result)
    # newest_board = copy.deepcopy(new_board)
    # solution_list = result['solution']
    # solve_time = result['solve_time']
    # count = result['count']

    # for solution in reversed(solution_list):
    #     newest_board.decode_str(solution)
    #     print()
    #     newest_board.print_board()
    #     print()
    #     time.sleep(0.1)
    
    # print("solved in: {0:.3f} seconds".format(solve_time), end="")
    # print(f' with {len(solution_list)} steps')
    # print(f'total amount of children analysed: {count}')


    
    


############################# michaels play corner #############################
    # new_board = board.Board(size, cars_list)
    # # car_to_move = new_board.cars_dict['A']
    # move_dict = {}
    # for car in new_board.cars_dict.values():
    #     if car.horizontal():
    #         location = car.x_location
    #     else:
    #         location = car.y_location
        
    #     positive_moves = new_board.positive_moves(car, location)
    #     negative_moves = new_board.negative_moves(car, location)
    #     print(f'{car.id} positive: {positive_moves}, negative {negative_moves}')
    #     move_dict[car] = list(range(positive_moves + 1)) + list(x for x in range(0,negative_moves -1, -1))
    # new_board.print_board()
    # for car in new_board.cars_dict.values():
    #     print(f'{car.id} with {move_dict[car]} options')
