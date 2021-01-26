from code.classes import board, cars
from code import helpers
from collections import deque
import queue
import copy
import time
#from collections import deque

class DepthFirst():
    def __init__(self, board):
        self.size = board.size
        self.board = copy.deepcopy(board)
        self.default_string = self.board.string_repr()
        self.archive = {}
        self.states = []
        self.solution_strings = []

        self.x_score = helpers.x_score(self.board)
        self.states.append([self.board.string_repr(), self.x_score])
        self.count = 0
        self.archive[self.default_string] = 0

    def append_last(self, queue_item):
        self.states.insert(0,queue_item)
    
    def append_first(self, queue_item):
        self.states.append(queue_item)

    def build_children(self):
        """
        """

        # parent board toevoegen en linken
        # find all possible boards,
        # put into archive
        # queue 
        cars_lists = self.board.find_possible_boards()
        parent_board_string = self.board.string_repr()

        # iterates over every possible board
        for cars_list in cars_lists:
            # create board object for the possible board
            new_board = board.Board(self.size, cars_list)
            
            # turn board object into string representation
            new_board_string = new_board.string_repr()

            if new_board_string in self.archive.keys():
                continue
            # if board not in archive, add to archive and add to queue
            else:
                # heuristiek mogelijk toepassen, score, hoe goed?
                self.archive[new_board_string] = parent_board_string 
                self.append_first([new_board_string])
                ############# don't remove #############

                del(new_board)

    def run(self):
        """
        """
        start_time = time.time()

        # as long as there are items in the queue
        while len(self.states) > 0:
            
            # haal het eerste element uit de queue
            
            current_item = self.states.pop()
            current_board = current_item[0]
            

            # decode the string representation of the board back into a board object
            self.board.decode_str(current_board)

            # break out of loop when solution is found
            if self.board.is_won():
                print("you won")
                # 
                self.load_solution_strings(self.board.string_repr())
                return {'count': self.count, 'solution': self.solution_strings, 'solve_time': time.time() - start_time, 'steps': len(self.solution_strings)}

 
            self.build_children()

            self.count += 1
            if self.count % 100 == 0:
                 print(f'children count:{self.count}')

    
    
    def load_solution_strings(self, parent_string):
        """
        """

        while self.default_string not in self.solution_strings:
            self.solution_strings.append(parent_string)
            self.load_solution_strings(self.archive[parent_string])

        
       