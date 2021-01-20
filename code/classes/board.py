from . import cars
import copy

EMPTY = '_'

# CRED = '\033[91m'
# CEND = '\033[0m'

class Board():
    """
        Class for supporting the game of rush hour,
        needs a size and list of cars to generate a new game
    """
    def __init__(self, size, cars_list):
        # initialize empty board
        self.board = [list(EMPTY * size) for i in range(size)]
        self.size = size
        self.cars_dict = {}
        self.load_cars_dict(cars_list)
        self.load_cars(self.cars_dict)
        self.won = False

    # SOURCE: https://github.com/KaKariki02/rushHour/blob/master/RushClass.py
    def print_board (self):
        """TODO kijken in git history voor hoe we dit deden met kleur"""
        self.printboard = '\n\n'.join(['      '.join(['{}'.format(item) for item in row]) for row in self.board])
        return self.printboard
    
    def string_repr(self):
        """
        Serializes board object into string
        """
        string_repr = ""

        # iterates over every row in board
        for row in range(self.size):
            # iterates over every column in board
            for column in range(self.size):
                # string keeps extending with every spot in the grid, splitting based on location, description and item
                string_repr = string_repr + str(column) + ',' + str(row) + '.' + self.board[row][column] + '-'
        return string_repr

    def decode_str(self, string_repr):
        """
        Decodes serialized board object
        """
        self.board = [list(EMPTY * self.size) for i in range(self.size)]
        
        # set all car location values to None
        for car in self.cars_dict.values():
            car.x_location = None
            car.y_location = None

        found_cars = []
        locations = string_repr.split('-')

        for location in locations:
            filled = location.split('.')

            if len(filled) > 1 and filled[1] != EMPTY:
                coordinates = filled[0].split(',')
                x = int(coordinates[0])
                y = int(coordinates[1])
                self.board[y][x] = filled[1]

                if filled[1] not in found_cars:
                    found_cars.append(filled[1])
                    self.cars_dict[filled[1]].x_location = x
                    self.cars_dict[filled[1]].y_location = y

    # def __hash__(self):
    #     return hash(self.string_repr())
    #     # lijst maken van hashes, gebruikte boards 
    #     # bord en richting opslaan in een hash, 
    
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
        return self.board[car.y_location + car.length][car.x_location] == EMPTY



    def check_move_right(self, car):
        if car.x_location + car.length > self.size - 1:
            return False
        return self.board[car.y_location][car.x_location + car.length] == EMPTY

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


    def check_move(self, car):
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
        
        # itereer over de auto's in de cars dictionary
        for car in self.cars_dict.values():
            # vind de move options voor de huidige auto
            move_options = self.check_move(car)

            # check of deze auto kan bewegen
            if len(move_options) > 0:
                # maak een nieuwe auto dictionary aan om een move in te maken
                new_cars_dict = copy.deepcopy(self.cars_dict)
            else:
                continue
            
            # vind de huidige auto in de kopie dictionary en beweeg deze
            new_cars_dict[car.id].do_move(move_options[0])


            # voeg de lijst met bewogen auto's hier aan toe
            possible_boards.append(new_cars_dict.values())

            # als de auto twee kanten op kan maak nieuwe kopie aan
            if len(move_options) > 1:
                other_cars_dict = copy.deepcopy(self.cars_dict)
                # beweeg de auto en voeg lijst met auto's toe aan possible boards
                other_cars_dict[car.id].do_move(move_options[1])
                possible_boards.append(other_cars_dict.values())
        
        num_children = len(possible_boards)

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
        
    def is_won(self):
        return self.cars_dict['X'].x_location + 1 == self.size - 1


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
    


