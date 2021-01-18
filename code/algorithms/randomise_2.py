import random
import copy
import time
from code import helpers
from code.classes import board, cars

def randomise_better(new_board):
    new_board = copy.deepcopy(new_board)
    count = 0
    full_string_board = new_board.string_board()

    # hash hierheen krijgen en in dictionary opslaan: string als key, object als value
    # def functie(car)
    #     return f'{car}{car.x_location}{car.y_location}'
    while True:
        #ARCHIVE VULLEN MET NEW_BOARD.___
        if count == 1000000:
            break
        
        if count % 1000 == 0:
            print(f'count:{count}')
        
        possible_boards = new_board.find_possible_boards()

        
        if count > 0:
            next_string = ""
        
            compare_list = [] 
            for car in next_board:
                car_string = car.car_string()
                next_string = next_string + car_string

            for select_board in possible_boards:
                compare_string = ""
                for car in select_board:
                    car_string = car.car_string()
                    compare_string = compare_string + car_string
                compare_list.append(compare_string)
            
            # print(f'r44 compare list: {compare_list}')
            # print()
            # print(f'r45 next string: {next_string}')
            for count, compare_board in enumerate(compare_list):
                if compare_board == next_string:
                    possible_boards.pop(count)
                # print(f'second possible boards: {possible_boards}')

        # print(f'r40: updated possible board: {possible_boards}')

        # hier kies je 1 bord, dit wordt de nieuwe lijst 
        next_board = random.choice(possible_boards)
        # hier onder wordt gelijk het bord veranderd, dmv next_board 
        
        new_board = board.Board(new_board.size, next_board)
        new_board.print_board()
        count += 1
        # time.sleep(0.5)
        
        if new_board.is_won():
            return count
        
def car_string (car):
    return f'{car}{car.x_location}{car.y_location}'