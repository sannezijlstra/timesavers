from .breadth_first import BreadthFirst

class DepthFirst(BreadthFirst):
    super(DepthFirst, self).__init__:
    self.states = []

    # RECHT UIT BREADTH FIRST MISSCHIEN MET SUPER EN EEN REGEL AANPASSEN?
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