from code.classes import board, cars
from code.algorithms import randomise, breadth_first, depth_first, beam_search
from code import helpers
import csv
import copy
import time
import random
import os
import sys

import sys
sys.setrecursionlimit(1500)

# --------------------------- Random reassignment --------------------------
def run_random(new_board, cars_list):
    """
    Runs the random algorithm, and shows the needed amount of steps to find the solution
    """
    result = randomise.randomise(new_board)
    solve_steps = result['loop_count']
    print("solved pseudorandomly in {0:.3f} seconds: ".format(result['solve_time']), end="")
    print(f'board {for_6} with {solve_steps} steps')

# --------------------------- Beam Search --------------------------
def run_beam_search(new_board, cars_list):
    """
    Runs the beam search algorithm with the heuristic chosen by the user, then generates the output 
    """
    heur_dict = {'min_steps': helpers.minimum_cost, 'combination': helpers.combination_score}
    dict_string = [str(key) for key in heur_dict.keys()]
    dict_string = ', '.join(dict_string)

    heur_choice = input(f'select heuristic: {dict_string} ')
    heur_to_use = heur_dict[heur_choice]
    
    beam = beam_search.BeamSearch(new_board, heur_to_use)
    print('begin run')
    result = beam.run()
    helpers.generate_output(result, new_board)
    
# --------------------------- Breadth First  --------------------------
def run_breadth_first(new_board, cars_list):
    """
    
    """
    breadth = breadth_first.BreadthFirst(new_board)
    result = breadth.run()
    helpers.generate_output(result, new_board)

# --------------------------- Depth First  --------------------------
def run_depth_first(new_board, cars_list):
    """ 
    """
    depth_obj = depth_first.DepthFirst(new_board)
    result = depth_obj.run()
    helpers.generate_output(result, new_board)

    print('begin run')

def test_corner(new_board, cars_list):
    minimum_steps = helpers.minimum_cost(new_board)
    print(f'minimum steps: {minimum_steps}')
    new_board.print_board()

# --------------- User Interface ---------------------
if __name__ == "__main__":
    # prompt user for data file size and select file from data folder
    while True:
        try:
            size = int(input("> what size (6, 9 or 12) grid would you like? "))
        except ValueError:
            print("invalid input")
            continue

        for_6 = random.randint(1,3)
        for_9 = random.randint(4,6)
        
        try:
            file_nr = int(input(f"> choose a file number if you'd like "))
        except ValueError:
            file_nr = None

        # load file path depending on the supplied size
        if size == 6:
            if file_nr and file_nr in range(1,4):
                for_6 = file_nr
                print(f'file {for_6} for size {size} is loaded')
            else:
                print(f'file {for_6} was selected randomly for size {size}')
            file_to_open = f'data/6x6_grids/Rushhour6x6_{for_6}.csv'
            break
        elif size == 9:
            if file_nr and file_nr in range(4,7):
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
        # open csv file consisting of the information of the board
        with open(file_to_open, 'r') as in_file:
            car_file = csv.DictReader(in_file)
            for line in car_file:
                # create new car object and append it to list
                new_car = cars.Car(line['car'], line['orientation'],int(line['row']) - 1 ,int(line['col']) - 1,line['length'])
                cars_list.append(new_car)
    else:
        sys.exit("data file is empty or does not exist")
    new_board = board.Board(size, cars_list)

    # create initial board 
    algorithm_choices = {'run_random': run_random, 'breadth_first': run_breadth_first, 'depth_first': run_depth_first, 'beam_search': run_beam_search, 'test_corner': test_corner}
    while True:
        try:
            dict_string = [str(key) for key in algorithm_choices.keys()]
            dict_string = ', '.join(dict_string)
            alg_choice = input(f'select algorithm from: {dict_string} ')
            algorithm_choices[alg_choice](new_board, cars_list)
            break
        except KeyError:
            print('invalid algorithm selection')