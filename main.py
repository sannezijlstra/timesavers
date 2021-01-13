from code.classes import board, cars
from code.algorithms import randomise
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

        #for_6 = random.randint(1,3)
        for_6 = 3
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
                new_car = cars.Car(line['car'], line['orientation'],line['row'],line['col'],line['length'])
                cars_list.append(new_car)
    else:
        sys.exit("data file is empty or does not exist")

    First_move = True
    # create initial board 
    new_board = board.Board(size, cars_list)
    count = 0

    while True:
        new_board.print_board()

        cars_that_can = {}
        # select car from list of cars using the user input
        for car in cars_list:
            result = car.can_move(new_board, size)
            if result:
                cars_that_can[car] = result
            

        if not First_move:
            if len(cars_that_can[reversed_move[0]]) == 2:
                cars_that_can[reversed_move[0]].remove(reversed_move[1])
            else:
                del cars_that_can[reversed_move[0]]

        last_move = randomise.random_move(new_board, cars_that_can)
        
        reversed_move = [last_move[0], randomise.reverse_move(last_move[1])]
        
        
        # move car if possible -> waarschijnlijk in random.py
        # if not new_board.do_move(direction, car_to_move):
        #     print('illegal move')
        #     continue
        
        # if game is won break out of loop
        if new_board.is_won():
            print('congrats you won')
            print(f'Count: {count}')
            new_board = board.Board(size, cars_list, True)
            new_board.print_board()
            break

        # reload the board
        new_board = board.Board(size, cars_list)
        
        count += 1
        if count == 1000000:
            break
        First_move = False
    
    print(f'Bord: {for_6}')