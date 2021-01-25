from code.classes import board, cars
from code import helpers
from collections import deque
import queue
import copy
import time

#from collections import deque

class BreadthFirst():
    def __init__(self, board):
        """
        Initialize the board 
        """
        self.size = board.size
        self.board = copy.deepcopy(board)
        self.count = 0

        # string representation of beginning board
        self.default_string = self.board.string_repr()
        self.archive = {}
        self.states = deque()
        self.solution_strings = []
        #self.best_solution = None
        self.x_score = helpers.x_score(self.board)
        self.red_car_score = helpers.red_car_score(self.board)

        # add to queue
        self.states.appendleft([self.board.string_repr(), self.x_score])

        #self.states.appendleft([self.board.string_repr(), self.red_car_score])

        # initialize the archive
        self.archive[self.default_string] = 0

    def append_last(self, queue_item):
        self.states.append(queue_item)
    
    def append_first(self, queue_item):
        self.states.appendleft(queue_item)

    def build_children(self):
        """
        First takes all possible boards, and determines the parent board string representation
        Then iterates over every possible board, creating board objects, turning them into strings, and adding them to the archive
        Applies different heuristics
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

                # if self.states[0][1] >= new_board.cars_dict['X'].x_location:
                #     continue
                # heuristiek mogelijk toepassen, score, hoe goed?
                self.archive[new_board_string] = parent_board_string 
                # queue_item = [new_board_string]

                # ############ HEURISTIC 1: X COORDINATES OF HORIZONTAL VEHICLES AS SMALL AS POSSIBLE #############
                # self.x_score = helpers.x_score(new_board)
                # # new_score = self.x_score / red_car_score
                # queue_item.append(self.x_score)
                # queue_item = [new_board_string, self.x_score]

                # if len(self.states) < 1:
                #     self.append_first(queue_item)

                # if self.states[0][1] >= queue_item[1]:
                #     self.append_last(queue_item)
                # else:
                #     self.append_first(queue_item)

                ############# HEURISTIC 2: VERTICAL CARS AS TO UPPER OR LOWER BOUND AS MUCH AS POSSIBLE #############
                # TODO
                # je weet waar rode auto zit en waar ie heen moet, hoe veel plekken tot uitgang, hoe veel auto's in de weg? 
                # met andere woorden, y = 2 is fout, if not car.horizontal() and y = 2 -> append right (achteraan) rekening houden met lengte auto
                # y_score = helpers.y_score(new_board)
                # # queue_item = [new_board_string, y_score]
                # queue_item.append(y_score)

                # # if len(self.states) < 1:
                #     # self.states.appendleft(queue_item)

                # # if self.states[0][1] <= queue_item[1]:
                #     # self.append_last(queue_item)
                # # else:
                #     # self.append_first(queue_item)
                # ############ HEURISTIC 3: MAKE SURE RED CAR SCORE IS ALWAYS THE BIGGEST -> minder goeie variant van heuristiek 4############
                # # red car met kleinste x wordt altijd achteraan gezet 
                # self.red_car_score = new_board.cars_dict['X'].x_location
                # # self.red_car_score = helpers.red_car_score(new_board)

                # # #board string van nieuwe board die een red car score bevat 
                # # queue_item = [new_board_string, self.red_car_score]
                # queue_item.append(self.red_car_score)
                ############ HEURISTIC 4: MAKE path redcar = empty ############
                # y = new_board.cars_dict['X'].y_location
                # empty_path_red = 0
                # for x in range(new_board.size - new_board.cars_dict['X'].x_location):
                #     if new_board.board[x][y] == board.EMPTY:
                #         empty_path_red += 1
                
                # queue_item.append(empty_path_red)

                # if len(self.states) < 1:
                #     self.states.appendleft(queue_item)

                # if self.states[0][1] <= queue_item[1] and self.states[0][2] >= queue_item[2]:
                #     self.append_last(queue_item)
                # else:
                #     self.append_first(queue_item)


                # if len(self.states) < 1:
                    #  self.append_first(queue_item)
                # # als de huidige queue een red car score bevat die hoger is dan de queue item, dan zet je de queue item vooraan de queue
                # # dit werkt niet want je wil alleen de red car score steeds zo groot mogelijk, dus werkt niet hetzelfde als de x_score...
                # if self.states[0][1] <= queue_item[1] and self.states[0][2] <= queue_item[2] and self.states[0][3] >= queue_item[3]:
                #      self.append_last(queue_item)
                # else:
                #      self.append_first(queue_item)
                ############# WITHOUT HEURISTICS #############
                self.append_first([new_board_string])
                ############# don't remove #############

                del(new_board)


    def run(self):
        """
        Runs the algorithm until shortest solution is found
        """
        start_time = time.time()

        # runs as long as there are items in the queue
        while len(self.states) > 0:
            
            # takes the first element out of the queue
            current_item = self.states.pop()

            # takes the string representation of the current board
            current_board = current_item[0]
            
            # decodes the string representation of the board back into a board object
            self.board.decode_str(current_board)

            # break out of loop when solution is found
            if self.board.is_won():
                print("you won")
                # loads all the strings of the parent boards
                self.load_solution_strings(self.board.string_repr())
                return {'count': self.count, 'solution': self.solution_strings, 'solve_time': time.time() - start_time, 'steps': len(self.solution_strings)}
 
            self.build_children()

            self.count += 1
            if self.count % 1000 == 0:
                 print(f'children count:{self.count}')
    
    def load_solution_strings(self, parent_string):
        """
        Loads all the string representations of the parent boards 
        """

        while self.default_string not in self.solution_strings:
            self.solution_strings.append(parent_string)
            self.load_solution_strings(self.archive[parent_string])

    def iterate_solution_strings(self, parent_string):
        # iets anders fixen dan recursion?
        pass
        
       