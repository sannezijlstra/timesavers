from code.classes import board, cars
from code import helpers
import queue
import copy

class BreadthFirst():
    def __init__(self, board, cars_list):
        self.size = board.size
        self.board = board
        self.cars_list = copy.deepcopy(cars_list)
        self.archive = {}
        self.states = queue.Queue(copy.deepcopy(self.cars_list))
        self.best_solution = None
        self.count = 0


    def get_next_state(self):
        return self.states.get()

    def build_children(self, cars_list, board):
        # Add an instance of the graph to the stack, with each unique value assigned to the node.
        # values = node.get_possibilities(self.transmitters)
       
       # staat van het bord moet in een string vorm --> encoden en decoden: bord naar de staat en staat naar het bord 

       # 12A 456B 89C ?
       
        new_cars = copy.deepcopy(cars_list)
        for car in new_cars:
            # we moeten iets vinden om de dictionary met 2 mogelijke keuzes op te splitsen en na elkaar te kunnen gebruiken 
            if car.horizontal:
                if car.can_move_left(board):
                    car.do_move('LEFT')
                    self.add_to_queue(new_cars, cars_list) # uiteindelijk een string???????
                    car.do_move('RIGHT')

                if car.can_move_right(board, self.size):
                    car.do_move('RIGHT')
                    self.add_to_queue(new_cars, cars_list)
                    car.do_move('LEFT')

            if not car.horizontal:
                if car.can_move_down(board, self.size):
                    car.do_move('DOWN')
                    self.add_to_queue(new_cars, cars_list)
                    car.do_move('UP')
                if car.can_move_up(board):
                    car.do_move('UP')
                    self.add_to_queue(new_cars, cars_list)
                    car.do_move('DOWN')

    # aparte add to queue functie, waarbij alles wat wordt toegevoegd in een archief wordt gezet, dus als dezelfde staat nog een keer langs komt, weet het bord dat die al is geweest?
    def add_to_queue(self, new_cars, old_list):
        if new_cars in self.archive:
            pass
        else:
            archive[new_cars] = old_list
            self.states.put(new_cars)
            self.board.check_won(new_cars)

    def run(self):
        while self.states:
            current_list = self.states.get()
            build_children(current_list, self.board)
            if self.board.is_won():
                print("we won")
                break
            print(current_list)
            self.count += 1
            if self.count % 100 == 0:
                 print(f'children count:{self.count}')




