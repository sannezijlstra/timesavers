from code.classes import board, cars
from code import helpers
import queue
import copy
#from collections import deque

class BreadthFirst():
    def __init__(self, board):
        self.size = board.size
        self.board = copy.deepcopy(board)
        self.cars_list = self.board.cars_list
        self.archive = {}
        self.test_states = [self.board.string_repr()]
        self.states = queue.Queue()
        self.states.put(self.board.string_repr())
        self.best_solution = None
        self.count = 0

        self.archive[self.board.string_repr()] = 0


    # def get_next_state(self):
    #     return self.states.get()

    def build_children(self):
        # find all possible boards,
        # put into archive
        # queue 
        board_strings = self.board.find_possible_boards()
        # possibleboards = [[A,B,C][A,B,C]
        #print(f'\n r28 board strings: {board_strings} \n')
        for board_string in board_strings:
            # make board from car_list [A,B,C]
            new_board = board.Board(self.size, board_string)
            # zet bord om in string
            new_board_string = new_board.string_repr()
            # verwijder het bord
            del(new_board)
            # if board in archive: pass

            if new_board_string in self.archive.keys():
                continue
            # if board not in archive: add to archive and add to queue
            else:
                # heuristiek mogelijk toepassen, score, hoe goed?
                self.archive[new_board_string] = 0
                # heuristieken toepassen
                self.states.put(new_board_string)
                # self.test_states.append(new_board_string)


    def run(self):
        # zolang er items in de queue staan
        while self.states.qsize() > 0:
            print('test')
            print(self.states.qsize())
            
            # haal het eerste element uit de queue
            current_board = self.states.get()
            # current_board = self.test_states.pop(0)

            print(f'current_board: {current_board}')
            # pak de informatie uit, uit de string
            self.board.decode_str(current_board)
            print()
            self.board.print_board()
            # break uit loop wanneer er een oplossing is gevonden (breadth first, eerste oplossing altijd het beste)
            if self.board.is_won():
                print("we won")
                break

            # build children en zet ze eventueel in de queue
            self.build_children()

            self.count += 1
            if self.count % 100 == 0:
                 print(f'children count:{self.count}')
        print('hallo states is leeg denk ik')
        print(f'finished with {self.count} boards')
        




