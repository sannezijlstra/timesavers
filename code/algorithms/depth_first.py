from .breadth_first import BreadthFirst
from code.classes import board, cars
from code import helpers
import queue
import copy
import time

class DepthFirst(BreadthFirst):
    """
    Class for the Depth First algorithm. In this search, the game starts in the parent board.
    Then, one child is completely searched (in depth), before moving on to the next child, thus creating a stack. 
    """
    def __init__(self, board):
        """
        Initialize the board, the stack, the archive, and the string representation of the parent board.
        """
        # uses essential parts from the Breadth first algorithm
        super().__init__(board)
        self.states = []
        self.states.append(self.board.string_repr())


    def append_first(self, queue_item):
        """
        Adds item to stack 
        """
        self.states.append(queue_item)