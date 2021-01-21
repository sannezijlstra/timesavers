Board.py TODOS:   vanaf regel 113, regel 148, regel 186, regel 210



def move(self, direction, car):
        """
            checks if move suggested is possible depending on orientation and space in the grid
            if move is possible make the move by updating the car object location
        """
        # check if suggested move is inherently impossible due to car orientation
        if car.horizontal == True and direction not in HORIZONTAL_MOVES:
            return False
        elif car.horizontal == False  and direction not in VERTICAL_MOVES:
            return False
        
        # moving a car is only possible in 4 directions and the field in grid has to be empty
        try:
            if direction == 'UP' and self.board[car.location[1] - 1 ][car.location[0]] == EMPTY:
                car.location[1] -= 1
                return True
            elif direction == 'DOWN' and self.board[car.location[1] + car.length][car.location[0]] == EMPTY:
                car.location[1] += 1
                return True
            elif direction == 'LEFT' and self.board[car.location[1]][car.location[0] - 1] == EMPTY:
                car.location[0] -= 1
                return True 
            elif direction == 'RIGHT' and self.board[car.location[1]][car.location[0] + car.length] == EMPTY:
                car.location[0] += 1
                # update the won flag is the red car reaches the right end
                if car.redcar == True and car.location[0] + 1 == self.size - 1:
                    self.won = True
            
                return True
        
            # direction is illegal or another object is blocking the path
            return False
            # moving out of bounds generates an index error so return false
        except IndexError:
            return False
    



    # main.py voor commands 
    while True:

        new_board.print_board()

        # algoritme komt hier
        # functie die bord object krijgt
        command = input("> select car and direction (Up, Down, Left, Right) ").upper()
        command = command.split()

        if len(command) != 2:
            print('invalid command')
            continue

        # select car from list of cars using the user input
        for car in cars_list:
            if car.car_id == command[0]:
                car_to_move = car

        direction = command[1]
        
        # move car if possible 
        if not new_board.move(direction, car_to_move):
            print('illegal move')
            continue

        # if game is won break out of loop
        if new_board.is_won():
            new_board = board.Board(size, cars_list, True)
            new_board.print_board()
            break

        # reload the board
        new_board = board.Board(size, cars_list)

    print('congrats you won')

    def can_move(self, car):
        """
            checks if move suggested is possible depending on orientation and space in the grid
            if move is possible make the move by updating the car object location
        """
        # moving a car is only possible in 4 directions and the field in grid has to be empty
        if car.horizontal == False and self.board[car.location[1] - 1 ][car.location[0]] == EMPTY or self.board[car.location[1] + car.length][car.location[0]] == EMPTY:
            car.can_move = True
        elif car.horizontal == True and self.board[car.location[1]][car.location[0] - 1] == EMPTY or self.board[car.location[1]][car.location[0] + car.length] == EMPTY:
            car.can_move = True
        else: 
            # direction is illegal or another object is blocking the path
            car.can_move = False

            # moving out of bounds generates an index error so return false
            # TODO GAAT MISSCHIEN PROBLEMEN OPLEVEREN

   
    # def can_move(self, board, size):
    #     """
    #         checks if move suggested is possible depending on orientation and space in the grid
    #         if move is possible make the move by updating the car object location
    #     """
    #     #print(f'car {car} locatino:x:{car.location[0]}, y:{car.location[1]},')
    #     # moving a car is only possible in 4 directions and the field in grid has to be empty
    #     if not car.horizontal and  car.location[1] >= 0 and car.location[1] + car.length - 1 <= size - 1 : # not omdraaien?
    #         if self.board[car.location[1] - 1 ][car.location[0]] == EMPTY or self.board[car.location[1] + car.length - 1][car.location[0]] == EMPTY:
    #             car.can_move = True 

    #     elif car.horizontal and  car.location[0]  >= 0 and car.location[0] + car.length - 1 <= size - 1:
    #         if self.board[car.location[0] - 1 ][car.location[1]] == EMPTY or self.board[car.location[0] + car.length - 1][car.location[1]] == EMPTY:
    #             car.can_move = True 

    #     else: 
    #         # direction is illegal or another object is blocking the path
    #         car.can_move = False

    #         # moving out of bounds generates an index error so return false
    #         # TODO GAAT MISSCHIEN PROBLEMEN OPLEVEREN


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


            if len(move_options) > 1:
                other_cars = copy.deepcopy(new_cars)
                if car.horizontal():
                    new_car = cars.Car(car.id, car.orientation, car.x_location - 1, car.y_location, car.length)
                    new_cars.remove(car)
                    new_cars.append(new_car)
                    possible_boards.append(new_cars)

                    other_car = cars.Car(car.id, car.orientation, car.x_location + 1, car.y_location, car.length)
                    other_cars.remove(car)
                    other_cars.append(other_car)
                    possible_boards.append(other_cars)

                else:
                    new_car = cars.Car(car.id, car.orientation, car.x_location, car.y_location - 1, car.length)
                    new_cars.remove(car)
                    new_cars.append(new_car)
                    possible_boards.append(new_cars)

                    other_car = cars.Car(car.id, car.orientation, car.x_location, car.y_location + 1, car.length)
                    other_cars.remove(car)
                    other_cars.append(other_car)
                    possible_boards.append(other_cars)
            else:
                for move in move_options:
                    if move == 'DOWN':
                        new_car = cars.Car(car.id, car.orientation, car.x_location, car.y_location + 1, car.length)
                        # print(f'new cars list: {new_cars}')
                        # print(f'car:{car}, new car:{new_car}')
                        new_cars.remove(car)

                        new_cars.append(new_car)
                        possible_boards.append(new_cars)
                        
                    if move == 'UP':
                        new_car = cars.Car(car.id, car.orientation, car.x_location, car.y_location - 1, car.length)
                        # print(f'new cars list: {new_cars}')
                        # print(f'car:{car}, new car:{new_car}') 
                        new_cars.remove(car)

                        new_cars.append(new_car)
                        possible_boards.append(new_cars)

                    if move == 'RIGHT':
                        # print(f'car:{car}')
                        new_car = cars.Car(car.id,car.orientation, car.x_location + 1, car.y_location, car.length)
                        # print(new_car)
                        # print(f'new cars list: {new_cars}')
                        new_cars.remove(car)

                        new_cars.append(new_car)
                        possible_boards.append(new_cars)

                    if move == 'LEFT':
                        new_car = cars.Car(car.id, car.orientation, car.x_location - 1, car.y_location, car.length)
                        # print(f'new cars list: {new_cars}')
                        # print(f'car:{car}, new car:{new_car}')
                        new_cars.remove(car)

                        new_cars.append(new_car)
                        possible_boards.append(new_cars)




for car in next_board:
                car_string = car.car_string()
                next_string = next_string + car_string

            for select_board in possible_boards:
                compare_string = ""
                for car in select_board:
                    car_string = car.car_string()
                    compare_string = compare_string + car_string
                compare_list.append(compare_string)
            
            # print(f'r44 compare list: {compare_list}')
            # print()
            # print(f'r45 next string: {next_string}')
            for count, compare_board in enumerate(compare_list):
                if compare_board == next_string:
                    possible_boards.pop(count)
                # print(f'second possible boards: {possible_boards}')

        # print(f'r40: updated possible board: {possible_boards}')


import random
from code import helpers
from code.classes import board, cars

HORIZONTAL_MOVES = ['LEFT', 'RIGHT']
VERTICAL_MOVES = ['UP', 'DOWN']


def random_move(board, cars_that_can):
    """
        Choose a random car that can move and make a random move
    """

    car_to_move = random.choice(list(cars_that_can.keys()))

    
    if car_to_move.horizontal:
        direction = random.choice(cars_that_can[car_to_move])
    else:
        direction = random.choice(cars_that_can[car_to_move])

    print(f'{car_to_move} to {direction}')
    car_to_move.do_move(direction)
    return [car_to_move, direction]

def run_random(new_board, cars_list):
    count = 0
    while True:
        new_board.print_board()

        cars_that_can = helpers.find_cars_that_can(cars_list, new_board)

        if count > 0:
            if len(cars_that_can[reversed_move[0]]) == 2:
                cars_that_can[reversed_move[0]].remove(reversed_move[1])
            else:
                del cars_that_can[reversed_move[0]]
                
        last_move = random_move(new_board, cars_that_can)
        
        reversed_move = [last_move[0], helpers.reverse_move(last_move[1])]

        # move car if possible -> waarschijnlijk in random.py
        # if not new_board.do_move(direction, car_to_move):
        #     print('illegal move')
        #     continue
        
        # if game is won break out of loop
        new_board.check_won(cars_list)

        if new_board.is_won():
            print('congrats you won')
            print(f'Count: {count}')
            new_board = board.Board(new_board.size, cars_list, True)
            new_board.print_board()
            break

        # reload the board
        new_board = board.Board(new_board.size, cars_list)
        
        count += 1
        if count == 1000000:
            break
        if count % 100 == 0:
            print(count)
    return count

Board.py:
    # def __hash__(self):
    #     return hash(self.string_repr())
    #     # lijst maken van hashes, gebruikte boards 
    #     # bord en richting opslaan in een hash, 

        # #TODO gebruiken we deze??
    # def __eq__(self, other):
    #     return hash(self) == hash(other)

# plaats dit object op positie 0,0 en 0,1 bijv. 
    # for i in range(size):
    # load board with car_objects?
    # dit is de parent staat van het bord, de staat vanuit waar het algoritme zijn werk gaat doen. 

    # def check_move_up (self, cars_list):
    # if car.orientation == 'H' and 

# IF MOVE IN MOVE_OPTIONS: MOVE = VALID


        # kopie van het huidige bord maken en met move 1 aanpassing maken
        # move moet een nieuwe instantie aanmaken in plaats van zichzelf aanpassen
        # kijken naar het bord ipv naar de auto's
        # steeds opnieuw een bord aanmaken 

        # HIER CHECKEN OF DE MOVE GEDAAN KAN WORDEN, 
        # IS HET VALID MOVE? DAN MOVEN 
        # serializen: archief bijhouden
        # het bord waar je mee bezig bent is parent, en children opslaan in list van parent 
        # begin staat van bord: bord is parent
        # op basis van heuristiek ga je alle bordjes aanmaken
        # voorbeelden: eerst alle auto's 1 plek, daarna naar links, daarna zo veel mogelijk 
        # sla alle borden op in queue 
        # je maakt alle staten van het bord aan, elk object heeft eigen locatie, maar omdat het string is zijn het geen echte objecten: representatie van bord in woorden 
        # pas bij het echt uitpakken van een string verander je pas echt de locaties ad hand van de string en gooi je de parent weg 
        # auto A heeft nu locatie x,y 
        # voor auto in string: 
        # auto objecten aangepast naar staat van het bord 
        # dus je checkt steeds of het voordeliug is (heuristiek!!!) hoe ver auto van finish of hoe weinig obstakels precies, en 
        # je wil de lijst met strings van bordjes kunnen sorteren, wat is nou een goed bord??? Dat kan je bepalen met een goede heuristiek!!!
        # laagste waarde van random gebruiken!! 

        # is dit een valid move? is het H of V? zit er een plekje omheen? --> niet valid? ga naar ander auto'tje 


        # AUTO CLASS: UITVOEREN VAN MOVE MET INFORMATIE VANAF BOARD
        # krijg stapruimte vanuit bord
        # kijk eerst horizontaal of verticaal, 
        # if self.orientation = "H" --> x + of - 1 en anders y +1 of - 1 
        # return possible_boards
     
        # if self.redcar and self.location[0] + 1 == board.size - 1:
        #     board.won = True

Board.py: 

def check_move_up(self, car):
        # TODO! DEZE FUNCTIES OMSCHRIJVEN TOT 1
        """
        Checks whether the location one step above the car is empty
        """
        # kunnen we hier gebruik maken van de car_object?
        if car.y_location - 1 < 0:
            return False 
        return self.board[car.y_location - 1 ][car.x_location] == EMPTY
        
    def check_move_down(self, car):
        """
        Checks whether the location one step below the car is empty
        """
        if car.y_location + car.length > self.size - 1:
            return False 
        return self.board[car.y_location + car.length][car.x_location] == EMPTY

    def check_move_right(self, car):
        """
        Checks whether the location one step right of the car is empty
        """
        if car.x_location + car.length > self.size - 1:
            return False
        return self.board[car.y_location][car.x_location + car.length] == EMPTY

    def check_move_left(self, car):
        """
        Checks whether the location one step left of the car is empty
        """
        if car.x_location - 1 < 0:
            return False
        return self.board[car.y_location][car.x_location - 1] == EMPTY

def find_all_moves(self, cars_dict):
        # TODO is dit niet dubbel met check_move?
        """
        Creates a dictionary where all possible moves are connected to the car objects? 
        """
        all_moves = {}
        # 
        for car in cars_dict.values():
            all_moves[car] = self.check_move(car)

            def check_move(self, car):
        """
        Creates a list for every car object, consisting of their possible moves
        """
        move_options = []
        
        if car.horizontal():
            if self.check_move_left(car):
                move_options.append('LEFT')
            if self.check_move_right(car):
                move_options.append('RIGHT')
        else: 
            if self.check_move_up(car):
                move_options.append('UP')
            if self.check_move_down(car):
                move_options.append('DOWN')
        return move_options


    def do_move(self, direction):
        # if self.valid_move
        if direction == 'UP':
            self.y_location -= 1
        elif direction == 'DOWN':
            self.y_location += 1
        elif direction == 'LEFT':
            self.x_location -= 1
        elif direction == 'RIGHT':
            self.x_location += 1

cars.py:
   # def __hash__(self):
    #     return hash(self.__repr__())

    # def __eq__(self, other):
    #     return hash(self) == hash(other)

# def car_string(self):
    #     """
    #     Returns string representation of car object
    #     """
    #     return "'{0}{1}{2}{3}{4}'".format(self.id, self.orientation, self.x_location, self.y_location, self.length)

randomise.py
# def car_string (car):
    return f'{car}{car.x_location}{car.y_location}'