from code.classes import board, cars
import csv

# TODO GET_INT
size = 6

if __name__ == "__main__":

    # create empty list to fill with cars
    cars_list = []

    with open('data/6x6_grids/Rushhour6x6_1.csv', 'r') as in_file:
        car_file = csv.DictReader(in_file)
        for line in car_file:
            # create new car object
            new_car = cars.Car(line['car'], line['orientation'],line['row'],line['col'],line['length'])
            cars_list.append(new_car)
    
    new_board = board.Board(size, cars_list)
    while True:


        new_board.print_board()
        command = input("> select car and direction (Up, Down, Left, Right) ").upper()
        command = command.split()

        for car in cars_list:
            if car.car_id == command[0]:
                car_to_move = car
        direction = command[1]
        
        if not new_board.move(direction, car_to_move):
            print('illegal move')
            continue

        new_board = board.Board(size, cars_list)

        if new_board.is_won(size, cars_list):
            break

    print('congrats you won')