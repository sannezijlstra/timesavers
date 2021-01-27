#############################################################
# Minor programmeren
#
# Michael van Gompel, Ahmed Moenna, Sanne Zijlstra
#
# Group: Time Savers
# Rush Hour case
#
# Contains logic for multiple algorithms solving Rush Hour 
# Randomise, breadth first, depth first, beam search 
#############################################################

from code.classes import board, cars
from code.algorithms import randomise, breadth_first, depth_first, beam_search
from code import helpers
import csv
import copy
import time
import random
import os
import sys
<<<<<<< HEAD

import sys
sys.setrecursionlimit(500)
=======
sys.setrecursionlimit(1500)
>>>>>>> de5eae323fb4a9fdd09ea42559a872c30bc56a99

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

    heur_choice = input(f'select heuristic: {dict_string} \n')
    heur_to_use = heur_dict[heur_choice]
    
    beam = beam_search.BeamSearch(new_board, heur_to_use)
    print('begin run')
    result = beam.run()
    helpers.generate_output(result, new_board)
    
# --------------------------- Breadth First  ------------------------
def run_breadth_first(new_board, cars_list):
    """
    Runs Breadth first algorithm and ensures the shortest solution
    """
    breadth = breadth_first.BreadthFirst(new_board)
    result = breadth.run()
    helpers.generate_output(result, new_board)

# --------------------------- Depth First  --------------------------
def run_depth_first(new_board, cars_list):
    """ 
    Runs the depth first algorithm and generates the output
    """
    depth_obj = depth_first.DepthFirst(new_board)
    result = depth_obj.run()
    helpers.generate_output(result, new_board)

# ------------------------- User Interface -------------------------
if __name__ == "__main__":
    # prompt user for data file size and select file from data folder
    while True:
        try:
            size = int(input("> What size (6, 9 or 12) grid would you like? "))
        except ValueError:
            print("invalid input")
            continue

        for_6 = random.randint(1,3)
        for_9 = random.randint(4,6)
        
        
        try:
            if size == 6:
                file_nr = int(input(f"> Choose a file number (1,2,3) if you'd like otherwise a random will be generated "))
            elif size == 9:
                file_nr = int(input(f"> Choose a file number (4,5,6) if you'd like, otherwise a random will be generated "))

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
    algorithm_choices = {'random': run_random, 'breadth first': run_breadth_first, 'depth first': run_depth_first, 'beam search': run_beam_search}
    while True:
        try:
            dict_string = [str(key) for key in algorithm_choices.keys()]
            dict_string = ', '.join(dict_string)
            alg_choice = input(f'Select algorithm from: {dict_string} \n')
            algorithm_choices[alg_choice](new_board, cars_list)
            break
        except KeyError:
            print('Invalid algorithm selection')