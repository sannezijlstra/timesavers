from . import cars
import copy

EMPTY = '_'
HORIZONTAL_MOVES = ['LEFT', 'RIGHT']
VERTICAL_MOVES = ['UP', 'DOWN']

CRED = '\033[91m'
CEND = '\033[0m'


# eerst bord maken
# lijst met beschikbare auto's 
# welke plek staan de auto's? 
# 

class Board():
    """
        class for supporting the game of rush hour
        needs a size and list of cars to generate a new game
    """
    def __init__(self, size, cars_list):
        # size, welke auto'tjes, list van moves, archive: DICT want key in dictionary is UNIEK, string opslaan als key van dictionary, hoe groot is bord, bord laden 


        self.board = [list(EMPTY * size) for i in range(size)]
        self.size = size
        self.cars_list = cars_list
        self.cars_dict = {}
        self.load_cars_dict(cars_list)
        # cars_list een dictionary waarin je kan zoeken, elke auto uniek
        self.load_cars(self.cars_dict)
        self.is_random = False
        self.won = False
        self.empty = [] # of variabele aan car toevoegen van is_movable, waarbij we checken na de move of er nog een vakje is
        # self.valid_move = False 

    # SOURCE: https://github.com/KaKariki02/rushHour/blob/master/RushClass.py
    def string_board (self):
        self.printboard = '\n\n'.join(['      '.join(['{}'.format(item) for item in row]) for row in self.board])
        return self.printboard
    
    def __hash__(self):
        return hash(self.string_board())
        # lijst maken van hashes, gebruikte boards 
        # bord en richting opslaan in een hash, 
    
    def __eq__(self, other):
        return hash(self) == hash(other)

    def load_cars_dict(self, cars_list):
        for car in cars_list:
            self.cars_dict[car.id] = car

    def load_cars(self, cars_dict):
        """
            function to load a cars into the game field, fills in the car id letters into the grid
        """
        for car in cars_dict.values():
            # if self.is_random:
            #     car_object = car.description
            # else:
                # car_object = car.id
            car_object = car.id

            # load the board with description on initial car location
            self.board[car.y_location][car.x_location] = car_object

            # load the rest of the car object in horizontal or vertical direction
            if car.horizontal():
                self.board[car.y_location][car.x_location + 1] = car_object
                # if car is a truck load another space in grid with object
                if car.length > 2:
                    self.board[car.y_location][car.x_location + 2] = car_object
            else:
                self.board[car.y_location + 1][car.x_location] = car_object
                # if car is a truck load another space in grid with object
                if car.length > 2:
                    self.board[car.y_location + 2][car.x_location] = car_object


    # plaats dit object op positie 0,0 en 0,1 bijv. 
    # for i in range(size):
    # load board with car_objects?
    # dit is de parent staat van het bord, de staat vanuit waar het algoritme zijn werk gaat doen. 

    # def check_move_up (self, cars_list):
    # if car.orientation == 'H' and 


    def check_move_up(self, car):
        # kunnen we hier gebruik maken van de car_object?
        if car.y_location - 1 < 0:
            return False 
        if self.board[car.y_location - 1 ][car.x_location] == EMPTY:
            return True
        return False
        
    def check_move_down(self, car):
        if car.y_location + car.length > self.size - 1:
            return False 
        if self.board[car.y_location + car.length][car.x_location] == EMPTY:
            return True
        return False


    def check_move_right(self, car):
        if car.x_location + car.length > self.size - 1:
            return False
        if self.board[car.y_location][car.x_location + car.length] == EMPTY:
            return True
        return False

    def check_move_left(self, car):
        if car.x_location - 1 < 0:
            return False
        if self.board[car.y_location][car.x_location - 1] == EMPTY:
            return True
        return False

    def find_all_moves(self, cars_dict):
        all_moves = {}
        for car in cars_dict.values():
            all_moves[car] = self.check_move(car)


    def check_move (self, car):
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
        
        # if move in move_options: 
        # self.valid_move = True 
        return move_options

    def find_possible_boards(self):
        possible_boards = []
        
        for car in self.cars_list:
            move_options = self.check_move(car)

            if len(move_options) > 0:
                new_cars = copy.deepcopy(self.cars_list)
            else:
                continue
            
            for move in move_options:
                if move == 'DOWN':
                    new_car = cars.Car(car.id, car.orientation, car.x_location, car.y_location + 1, car.length)
                    # print(f'new cars list: {new_cars}')
                    # print(f'car:{car}, new car:{new_car}')
                    try:
                        new_cars.remove(car)
                    except ValueError:
                        new_cars.remove(temp)

                    new_cars.append(new_car)
                    possible_boards.append(new_cars)
                    temp = new_car
                    
                if move == 'UP':
                    new_car = cars.Car(car.id, car.orientation, car.x_location, car.y_location - 1, car.length)
                    # print(f'new cars list: {new_cars}')
                    # print(f'car:{car}, new car:{new_car}') 
                    try:
                        new_cars.remove(car)
                    except ValueError:
                        new_cars.remove(temp)

                    new_cars.append(new_car)
                    possible_boards.append(new_cars)
                    temp = new_car

                if move == 'RIGHT':
                    # print(f'car:{car}')
                    new_car = cars.Car(car.id,car.orientation, car.x_location + 1, car.y_location, car.length)
                    # print(new_car)
                    # print(f'new cars list: {new_cars}')
                    try:
                        new_cars.remove(car)
                    except ValueError:
                        new_cars.remove(temp)

                    new_cars.append(new_car)
                    possible_boards.append(new_cars)
                    temp = new_car
                    
                if move == 'LEFT':
                    new_car = cars.Car(car.id, car.orientation, car.x_location - 1, car.y_location, car.length)
                    # print(f'new cars list: {new_cars}')
                    # print(f'car:{car}, new car:{new_car}')
                    try:
                        new_cars.remove(car)
                    except ValueError:
                        new_cars.remove(temp)

                    new_cars.append(new_car)
                    possible_boards.append(new_cars)
                    temp = new_car



        return possible_boards


        
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
        
    
    def is_won (self):
        """
            Checks if the game is won by checking won flag
        """
        for car in self.cars_list:
            if car.redcar and car.x_location + 1 == self.size - 1:
                self.won = True
        return self.won
    
    #def check_won_breadth(self):
    def copy_board (self):
        pass

    def print_board(self):
        """
            iterate over the board rows and items to print the board
        """
        for row in self.board:
            for item in row:
               print(f'{item} ', end="")
            print()


