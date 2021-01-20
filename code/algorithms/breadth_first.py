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
        # self.cars_list = self.board.cars_dict.values()
        self.archive = {}
        self.states = deque()
        self.solution_strings = []
        self.rec_count = 0
        # self.states = queue.Queue()
        # self.states.put(self.board.string_repr())
        self.best_solution = None

        self.count = 0
        self.archive[self.default_string] = 0

# variabel aanmaken 


    # def get_next_state(self):
    #     return self.states.get()

    def build_children(self): # parent board toevoegen en linken
        # find all possible boards,
        # put into archive
        # queue 
        cars_lists = self.board.find_possible_boards()
        parent_board_string = self.board.string_repr()
        # wat is hier mis mee??
        # self.next_children += possible_boards_result[1]


        # possibleboards = [[A,B,C][A,B,C]
        #print(f'\n r28 board strings: {board_strings} \n')
        for cars_list in cars_lists:
            # make board from car_list [A,B,C]
            new_board = board.Board(self.size, cars_list)
            
            # zet bord om in string
            new_board_string = new_board.string_repr()
            # if board in archive: pass

            if new_board_string in self.archive.keys():
                continue
            # if board not in archive: add to archive and add to queue
            else:
                # heuristiek mogelijk toepassen, score, hoe goed?
                self.archive[new_board_string] = parent_board_string 
                # queue_input = [new_board_string, score] -> order queue op score
                # heuristieken toepassen
                # vb 1: alle x coordinaten van de auto's zo veel naar links
                # vb 2: alle verticale auto's zo veel mogelijk naar de boven/onder rand
                # als er een empty kan komen op een plek rechts van de auto, move maken
                # plekken rechts tot uitgang minimaliseren
                # x_score = helpers.x_score(new_board)
                # verwijder het bord
                del(new_board)
                # checken wat de value is van de eerste in de rij is 
                # als x_value lager is dan wordt huidige string achteraan gezet
                # anders vooraan
                
                # ############ MET HEURISTIEK X ZO VEEL MOGELIJK NAAR LINKS #############
                # queue_item = [new_board_string, x_score]

                # if len(self.states) < 1:
                #     self.states.appendleft(queue_item)

                # if self.states[0][1] <= queue_item[1]:
                #     self.states.append(queue_item)
                # else:
                #     self.states.appendleft(queue_item)

                ############# MET HEURISTIEK VERTICALE AUTO'S NIET OP RIJ VAN REDCAR ###########
                # TODO
                # je weet waar rode auto zit en waar ie heen moet, hoe veel plekken tot uitgang, hoe veel auto's in de weg? 
                # met andere woorden, y = 2 is fout, if not car.horizontal() and y = 2 -> append right (achteraan) rekening houden met lengte auto

                ############# ZONDER HEURESTIEK #############
                self.states.appendleft([new_board_string])


    def run(self):
        start_time = time.time()
        x_score = helpers.x_score(self.board)
        self.states.appendleft([self.board.string_repr(), x_score])
        # zolang er items in de queue staan
        while len(self.states) > 0:
            
            # haal het eerste element uit de queue
            
            current_item = self.states.pop()
            current_board = current_item[0]
            

            # print(f'current_board: {current_board}')
            # pak de informatie uit, uit de string
            self.board.decode_str(current_board)
            # print()
            # self.board.print_board()
            # break uit loop wanneer er een oplossing is gevonden (breadth first, eerste oplossing altijd het beste)
            if self.board.is_won():
                print("you won")
                self.load_solution_strings(self.board.string_repr())
                # print(self.solution_strings)
                # print(f'solution string length: {len(self.solution_strings)}')
                return {'count': self.count, 'solution': self.solution_strings, 'solve_time': time.time() - start_time, 'steps': len(self.solution_strings)}

 
            self.build_children()

            self.count += 1
            if self.count % 100 == 0:
                 print(f'children count:{self.count}')
    
    def load_solution_strings(self, parent_string):
        # solution_strings.append(self.board.string_repr())
        # print(f'\nparent string: {parent_string}')
        # print(f'\n solution list:{self.solution_strings}\n')
        # print(f'default string {self.default_string}')

        while self.default_string not in self.solution_strings and self.rec_count < 100:
            self.rec_count += 1
            self.solution_strings.append(parent_string)
            self.load_solution_strings(self.archive[parent_string])

        
       