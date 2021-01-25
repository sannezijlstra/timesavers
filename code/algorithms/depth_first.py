from .breadth_first import BreadthFirst
from code.classes import board, cars
from code import helpers
import queue
import copy
import time

class DepthFirst(BreadthFirst):
    def __init__(self, board):
        super().__init__(board)
        self.states = []


    def append_last(self, queue_item):
        self.states.insert(0, queue_item)
    
    def append_first(self, queue_item):
        self.states.append(queue_item)
        
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