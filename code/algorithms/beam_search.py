from .breadth_first import BreadthFirst
from code.classes import board, cars
from code import helpers
import queue
import copy
import time
import bisect

class BeamSearch(BreadthFirst):
    def __init__(self, board, heur_to_use):
        super().__init__(board)
        self.states = []
        self.max_length = 10000
        print(f'empty states? {self.states}')
        self.heuristic = heur_to_use
        self.heuristic_score = self.heuristic(self.board)

        self.states.append([self.heuristic_score, self.board.string_repr()])
        
    def get_next_state(self):
        current_state = self.states.pop(0)
        return current_state[1]

    def insert_on_score(self, queue_item):
        # insert score
        bisect.insort(self.states, queue_item)

    def build_children(self):
        """
        First takes all possible boards, and determines the parent board string representation
        Then iterates over every possible board, creating board objects, turning them into strings, and adding them to the archive
        Applies different heuristics
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

                self.heuristic_score = self.heuristic(new_board)
                queue_item = [self.heuristic_score, new_board_string]
                self.insert_on_score(queue_item)

                del(new_board)

        if len(self.states) > self.max_length:
            self.states = self.states[:self.max_length - 1]
