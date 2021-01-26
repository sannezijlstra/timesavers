from .breadth_first import BreadthFirst
from code.classes import board, cars
from code import helpers
import queue
import copy
import time
import bisect

class BeamSearch(BreadthFirst):
    def __init__(self, board):
        super().__init__(board)
        self.states = []
        self.max_length = 10000
        self.x_score = helpers.x_score(self.board)
        self.red_car_score = helpers.red_car_score(self.board)
        self.min_red_steps = helpers.minimum_cost(self.board)
        print(f'empty states? {self.states}')

        self.states.append([self.x_score, self.board.string_repr()])
        
    def get_next_state(self):
        return self.states.pop(0)
    
    def insert_on_score(self, queue_item):
        # insert score
        bisect.insort(self.states, queue_item)

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

<<<<<<< HEAD
                # ############ HEURISTIC 1: X COORDINATES OF HORIZONTAL VEHICLES AS SMALL AS POSSIBLE #############
                # self.x_score = helpers.x_score(new_board)
                # new_score = self.x_score / red_car_score
                # queue_item = [self.x_score, new_board_string]
                # queue_item.append(self.x_score)
                

                # if self.states[0][1] >= queue_item[1]:
                #     self.append_last(queue_item)
                # else:
                #     self.append_first(queue_item)
                self.min_red_steps = helpers.minimum_cost(new_board)
                queue_item = [self.min_red_steps, new_board_string]
                self.insert_on_score(queue_item)
                ############# HEURISTIC 2: VERTICAL CARS AS TO UPPER OR LOWER BOUND AS MUCH AS POSSIBLE #############
                # TODO
                # je weet waar rode auto zit en waar ie heen moet, hoe veel plekken tot uitgang, hoe veel auto's in de weg? 
                # met andere woorden, y = 2 is fout, if not car.horizontal() and y = 2 -> append right (achteraan) rekening houden met lengte auto
                # y_score = helpers.y_score(new_board)
                # queue_item[0] += y_score

                # ############ HEURISTIC 3: MAKE SURE RED CAR SCORE IS ALWAYS THE BIGGEST -> minder goeie variant van heuristiek 4############
                # red car met kleinste x wordt altijd achteraan gezet 
                # self.red_car_score = helpers.red_car_score(new_board)
                # self.red_car_score = helpers.red_car_score(new_board)
                # queue_item[0] += self.red_car_score
                # # #board string van nieuwe board die een red car score bevat 
=======
                # ############ HEURISTIC 1:  #############
                # x coordinates of horizontal vehicles as small as possible
                self.x_score = helpers.x_score(new_board)
                new_score = self.x_score / red_car_score
                queue_item = [self.x_score, new_board_string]
                queue_item.append(self.x_score)

                if self.states[0][1] >= queue_item[1]:
                    self.append_last(queue_item)
                else:
                    self.append_first(queue_item)

                # vertical cars to upper or lower bound as much as possible 
                y_score = helpers.y_score(new_board)
                queue_item[0] += y_score

                # red car always situated to the right as much as possible 
                self.red_car_score = helpers.red_car_score(new_board)
                self.red_car_score = helpers.red_car_score(new_board)
                queue_item[0] += self.red_car_score

                ############### HEURISTIC 2:  ##########

                self.min_red_steps = helpers.minimum_cost(new_board)
                queue_item = [self.min_red_steps, new_board_string]
                self.insert_on_score(queue_item)


>>>>>>> 4d300ddc904f0fa82a3c53019bdf31668a1d38a0
                ############ HEURISTIC 4: MAKE path redcar = empty ############
                # y = new_board.cars_dict['X'].y_location
                # empty_path_red = 0
                # for x in range(new_board.size - new_board.cars_dict['X'].x_location):
                #     if new_board.board[x][y] == board.EMPTY:
                #         empty_path_red += 1


                # # als de huidige queue een red car score bevat die hoger is dan de queue item, dan zet je de queue item vooraan de queue
                # # dit werkt niet want je wil alleen de red car score steeds zo groot mogelijk, dus werkt niet hetzelfde als de x_score...
                ############# don't remove #############


                del(new_board)

        if len(self.states) > self.max_length:
            self.states = self.states[:self.max_length - 1]


# idee van een vaste breedte toevoegen
# dingen wegharken die niet bij je heuristieken passen

# A star:
# voorkeur voor bepaalde borden: minimaal en consistent 
# altijd onderschalen: consistent. 
# geen radomness 
# je gaat je borden rangschikken op voorkeur en aantal zetten dat nodig is om op het bord te komen 
# bord steeds minste aantal zetten naar doel en 
# altijd onderschattig, dus realiteit is altijd minder goed 
# kortste om er te komen + goeie schatting dat volgende zet oplossing is
# minimale kosten en minimale schatting --> garantie dat alles daarna slechter is 
# alles daarna heeft niet allebei van bovenstaande 
# slechtste schatting: 0 stappen: precies breadth first search!!! 
# betere schatting: iig 1 zet: voorkeur aan bord waar auto wel voor t bord staat 
# beter: als auto hier, 2 auto's daarvoor, 2 auto's aan de kant dus 2 zetten nodig --> minimale consistente onderschatting
# minimale heuristiek is heel lastig 
