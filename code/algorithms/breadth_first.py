from code.classes import board, cars
from code import helpers
from collections import deque
import queue
import copy
import time

class BreadthFirst():
    """
    The Breadth First search starts in the 'parent' board. 
    Then, all the 'children' boards (possible boards) are searched, and put into the back of a queue. 
    This way, the tree is flattened out, as every single 'child' board is searched until finding a solution.
    """
    def __init__(self, board):
        """
        Initialize the board, the queue, the archive, and the string representation of the parent board.
        """
        self.size = board.size
        self.board = copy.deepcopy(board)
        self.count = 0

        # string representation of parent board
        self.default_string = self.board.string_repr()
        self.archive = {}
        
        # initialize queue 
        self.states = deque()
        self.solution_strings = []

        # add string representation of board to queue
        # TODO IS HET NOU GOED DAT HIER APPENDLEFT STAAT?
        self.states.appendleft(self.board.string_repr())

        # initialize the archive
        self.archive[self.default_string] = 0


    def append_first(self, queue_item):
        """
        Adds item to queue
        """
        self.states.appendleft(queue_item)
    

    def get_next_state(self):
        """
        Removes first item out of queue
        """
        return self.states.pop()


    def build_children(self):
        """
        First takes all possible boards, and determines the parent board string representation
        Then iterates over every possible board, creating board objects, turning them into strings, and adding them to the archive
        """
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
     
                self.archive[new_board_string] = parent_board_string 
                self.append_first(new_board_string)

                del(new_board)


    def run(self):
        """
        Runs the algorithm until shortest solution is found
        """
        start_time = time.time()

        # runs as long as there are items in the queue
        while len(self.states) > 0:
            
            # get first state out of the queue
            current_board = self.get_next_state()
            
            # decodes the string representation of the board back into a board object
            self.board.decode_str(current_board)

            # break out of loop when solution is found
            if self.board.is_won():
                print("you won")
                # loads all the strings of the parent boards
                self.load_solution_strings(self.board.string_repr())
                return {'count': self.count, 'solution': self.solution_strings, 'solve_time': time.time() - start_time, 'steps': len(self.solution_strings)}
 
            self.build_children()
            # counts amount of children boards analyzed
            self.count += 1
            if self.count % 1000 == 0:
                print(f'children count:{self.count}')
    

    def load_solution_strings(self, parent_string):
        """
        Uses recursion to load all the string representations of the parent boards, to count amount of necessary moves
        """
        while self.default_string not in self.solution_strings:
            self.solution_strings.append(parent_string)
            #TODO NOG EEN COMMENT?
            self.load_solution_strings(self.archive[parent_string])