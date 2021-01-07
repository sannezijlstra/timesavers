from code.classes import board, cars
import csv

if __name__ == "__main__":

    # create empty list to fill with cars
    cars_list = []

    with open('data/6x6_grids/Rushhour6x6_1.csv', 'r') as in_file:
        car_file = csv.DictReader(in_file)
        for line in car_file:
            # create new car object
            new_car = cars.Car(line['car'], line['orientation'],line['row'],line['col'],line['length'])
            cars_list.append(new_car)
    
    new_board = board.Board(6, cars_list)

    new_board.print_board()