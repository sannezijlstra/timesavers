from code.classes import board, cars
from code import helpers
from collections import deque
import queue
import copy
#from collections import deque

class BreadthFirst():
    def __init__(self, board):
        self.size = board.size
        self.board = copy.deepcopy(board)
        self.cars_list = self.board.cars_list
        self.archive = {}
        self.states = deque()
        # self.states = queue.Queue()
        # self.states.put(self.board.string_repr())
        self.best_solution = None

        self.count = 0
        self.depth = 0
        self.current_children = 0
        self.next_children = 0
        self.archive[self.board.string_repr()] = 0

# variabel aanmaken 


    # def get_next_state(self):
    #     return self.states.get()

    def build_children(self): # parent board toevoegen en linken
        # find all possible boards,
        # put into archive
        # queue 
        possible_boards_result = self.board.find_possible_boards()

        cars_lists = possible_boards_result[0]
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
                self.archive[new_board_string] = 0 
                # queue_input = [new_board_string, score] -> order queue op score
                # heuristieken toepassen
                # vb 1: alle x coordinaten van de auto's zo veel naar links
                # vb 2: alle verticale auto's zo veel mogelijk naar de boven/onder rand
                # als er een empty kan komen op een plek rechts van de auto, move maken
                # plekken rechts tot uitgang minimaliseren

                        

                x_score = helpers.x_score(new_board)
                # verwijder het bord
                del(new_board)
                # checken wat de value is van de eerste in de rij is 
                # als x_value lager is dan wordt huidige string achteraan gezet
                # anders vooraan

                #self.states.append(new_board_string)
                queue_item = [new_board_string, x_score]

                if self.states[0][1] <= queue_item[1]:
                    self.states.append(queue_item)
                else:
                    self.states.appendleft(queue_item)


    def run(self):
        self.states.appendleft(self.board.string_repr())
        # zolang er items in de queue staan
        while len(self.states) > 0:
            
            # haal het eerste element uit de queue
            current_board = self.states.pop()
            

            # print(f'current_board: {current_board}')
            # pak de informatie uit, uit de string
            self.board.decode_str(current_board)
            # print()
            # self.board.print_board()
            # break uit loop wanneer er een oplossing is gevonden (breadth first, eerste oplossing altijd het beste)
            if self.board.is_won():
                print("you won")
                break

            # wat is mis met deze logica?

            # if self.current_children < 1:
            #     self.current_children = self.next_children
            #     self.next_children = 0
            #     self.depth += 1
            # else:
            #     self.current_children -= 1
            # build children en zet ze eventueel in de queue
            self.build_children()

            self.count += 1
            if self.count % 100 == 0:
                 print(f'children count:{self.count}')
        print(f'finished with {self.count} boards')
        print(f'depth: {self.depth}')
        




