import random
import copy
import time
from code import helpers
from code.classes import board, cars

def randomise(new_board):
    new_board = copy.deepcopy(new_board)
    loop_count = 0
    # last_board_string = new_board.string_repr()

    # hash hierheen krijgen en in dictionary opslaan: string als key, object als value
    # def functie(car)
    #     return f'{car}{car.x_location}{car.y_location}'
    while True:
        #ARCHIVE VULLEN MET NEW_BOARD.___
        if loop_count == 1000000:
            break
        
        if loop_count % 1000 == 0:
            print(f'count:{loop_count}')
        
        possible_boards = new_board.find_possible_boards()
        
        #last_board_string = random.choice(possible_boards.string_repr())

        # print(f'first possible boardslist {len(possible_boards)}\n{possible_boards}')
        if loop_count > 0:
            for count, cars_list  in enumerate(possible_boards):
                temp = board.Board(new_board.size, cars_list)
                
                if last_board_string == temp.string_repr():
                    #print(possible_boards[count])
                    #print()
                    #print(temp.cars_dict.values())
                    # del(possible_boards[count])
                    possible_boards.pop(count)
                    
        # print(f'second possible boardslist length {len(possible_boards)} \n {possible_boards}')

        last_board_string = new_board.string_repr()
        # print(f'possible boards:{possible_boards}')
        # hier kies je 1 bord, dit wordt de nieuwe lijst 
        next_board = random.choice(possible_boards)
        # hier onder wordt gelijk het bord veranderd, dmv next_board 
        # print(f'next_board: {next_board}')
        new_board = board.Board(new_board.size, next_board)
        new_board.print_board()
        print()
        loop_count += 1
        time.sleep(0.5)
        
        if new_board.is_won():
            print(loop_count)
            return loop_count
        
