from .breadth_first import BreadthFirst
from code.classes import board, cars
from code import helpers
import queue
import copy
import time
import bisect

class BeamSearch(BreadthFirst):
    """
    The Beam Search algorithm is a heuristic based algorithm, where the queue(list) is pruned on the arbitrary count of 10.000 items. 
    """
    def __init__(self, board, heur_to_use):
        """
        Initializes the board, takes input to choose the heuristic to apply to the algorithm, and initializes the queue. 
        """
        # uses essential parts from the Breadth first algorithm
        super().__init__(board)
        self.states = []
        self.max_length = 10000
        # input from user is used to choose heuristic
        self.heuristic = heur_to_use
        
        # heuristic score depends on which heuristic is chosen
        self.heuristic_score = self.heuristic(self.board)

        # first queue item is added to queue list
        self.states.append([self.heuristic_score, self.board.string_repr()])

    def get_next_state(self):
        """
        Get next state from the queue
        """
        current_state = self.states.pop(0)
        return current_state[1]

    def insert_on_score(self, queue_item):
        """
        Sorts the queue, in order of lowest heuristic score to highest heuristic score. 
        """
        bisect.insort(self.states, queue_item)

    def build_children(self):
        """
        Creates all possible child-boards and adds them to the queue(states)
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
            else:
                self.archive[new_board_string] = parent_board_string 
                
                # adds heuristic score to board object
                self.heuristic_score = self.heuristic(new_board)

                # builds an item for the queue, connecting the board string and heuristic score
                queue_item = [self.heuristic_score, new_board_string]

                # adds item and inserts into queue, maintaining a sorted list
                self.insert_on_score(queue_item)

                del(new_board)

        # prunes queue when it contains more than 10.000 items 
        if len(self.states) > self.max_length:
            self.states = self.states[:self.max_length - 1]