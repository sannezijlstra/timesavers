from code.classes import board, cars
from code.algorithms import randomise, randomise_2, breadth_first
from code import helpers
import csv
import random
import os
import sys

# TODO 12x12 grid auto's hebben 2 letterige id

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

        # save file path depending on the size
        if size == 6:
            file_to_open = f'data/6x6_grids/Rushhour6x6_{for_6}.csv'
            break
        elif size == 9:
            file_to_open = f'data/9x9_grids/Rushhour9x9_{for_9}.csv'
            break
        elif size == 12:
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
                new_car = cars.Car(line['car'], line['orientation'], int(line['row']) - 1, int(line['col']) - 1, line['length'])
                cars_list.append(new_car)
    else:
        sys.exit("data file is empty or does not exist")

    # create initial board 
    new_board = board.Board(size, cars_list)
    # next_possible_boards = new_board.find_possible_boards(cars_list)
    # print(next_possible_boards)
    # for lst in next_possible_boards:
    #     print(lst)

    # print(new_board)
    
    #print(new_board.string_board)


    solution_count = randomise_2.randomise_better(new_board)
    print(f'board {for_6} solved pseudorandomly in {solution_count} steps')
############################# RANDOM #############################
    # new_board = board.Board(size, cars_list, True)
    # solution_count = randomise.run_random(new_board, cars_list)
    # print(f'board {for_6} solved pseudorandomly in {solution_count} steps')

############################# BREADTH FIRST #############################
    # new_board = board.Board(size, cars_list)
    # breadth = breadth_first.BreadthFirst(new_board, cars_list)
    # breadth.run()
