from code.classes import board, cars
from code import helpers
from collections import deque
import queue
import copy
import time
#from collections import deque

class BreadthFirst():
    def __init__(self, board):
        self.size = board.size
        self.board = copy.deepcopy(board)
        self.default_string = self.board.string_repr()
        self.archive = {}
        self.states = deque()
        self.solution_strings = []
        self.rec_count = 0
        self.best_solution = None

        self.count = 0
        self.archive[self.default_string] = 0


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

                del(new_board)

                # ############ HEURISTIC 1: X COORDINATES OF HORIZONTAL VEHICLES AS SMALL AS POSSIBLE #############
                # queue_item = [new_board_string, x_score]

                # if len(self.states) < 1:
                #     self.states.appendleft(queue_item)

                # if self.states[0][1] <= queue_item[1]:
                #     self.states.append(queue_item)
                # else:
                #     self.states.appendleft(queue_item)

                ############# HEURISTIC 2: VERTICAL CARS AS TO UPPER OR LOWER BOUND AS MUCH AS POSSIBLE #############
                # TODO
                # je weet waar rode auto zit en waar ie heen moet, hoe veel plekken tot uitgang, hoe veel auto's in de weg? 
                # met andere woorden, y = 2 is fout, if not car.horizontal() and y = 2 -> append right (achteraan) rekening houden met lengte auto

                ############# WITHOUT HEURISTICS #############
                self.states.appendleft([new_board_string])


    def run(self):
        """
        """
        start_time = time.time()
        x_score = helpers.x_score(self.board)
        self.states.appendleft([self.board.string_repr(), x_score])
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

        while self.default_string not in self.solution_strings and self.rec_count < 100:
            self.rec_count += 1
            self.solution_strings.append(parent_string)
            self.load_solution_strings(self.archive[parent_string])

        
       