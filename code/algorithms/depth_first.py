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


    #TODO QUEUE ITEM NAAM VERANDEREN NAAR STACK_ITEM? OF KAN DAT NIET?
    def append_first(self, queue_item):
        """
        Adds item to stack 
        """
        self.states.append(queue_item)
       
        
    def run(self):
        """
        Runs the algorithm until a solution is found
        """
        start_time = time.time()

        # runs as long as there are items in the queue
        while len(self.states) > 0:
            
            # takes the first item out of the stack
            current_board = self.states.pop()

            # decode the string representation of the board back into a board object
            self.board.decode_str(current_board)

            # break out of loop when solution is found
            if self.board.is_won():
                print("you won")
                # 
                self.load_solution_strings(self.board.string_repr())
                return {'count': self.count, 'solution': self.solution_strings, 'solve_time': time.time() - start_time, 'steps': len(self.solution_strings)}
 
            # calls build_children function from Breadth First algorithm
            self.build_children()

            # TODO WILLEN WE ONDERSTAANDE HOUDEN? RELEVANT?
            self.count += 1
            if self.count % 100 == 0:
                 print(f'children count:{self.count}')