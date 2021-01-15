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
    def __init__(self, size, cars_list, random=False):
        # size, welke auto'tjes, list van moves, archive: DICT want key in dictionary is UNIEK, string opslaan als key van dictionary, hoe groot is bord, bord laden 


        self.board = [list(EMPTY * size) for i in range(size)]
        self.cars = cars_list
        # cars_list een dictionary waarin je kan zoeken, elke auto uniek
        self.load_cars(cars_list)
        self.size = size
        self.random = random
        self.won = False
        self.empty = [] # of variabele aan car toevoegen van is_movable, waarbij we checken na de move of er nog een vakje is

    def __repr__ (self):
        return str(self.board)

    def load_cars(self, cars_list):
        """
            function to load a cars into the game field, fills in the car id letters into the grid
        """
        
        
        for car in cars_list:
            if self.random:
                car_object = car.description
            else:
                car_object = car.car_id

            # load the board with description on initial car location
            self.board[car.location[1]][car.location[0]] = car_object

            # load the rest of the car object in horizontal or vertical direction
            if car.horizontal:
                self.board[car.location[1]][car.location[0]+ 1] = car_object
                # if car is a truck load another space in grid with object
                if car.length > 2:
                    self.board[car.location[1]][car.location[0]+2] = car_object
            else:
                self.board[car.location[1]+1][car.location[0]] = car_object
                # if car is a truck load another space in grid with object
                if car.length > 2:
                    self.board[car.location[1]+ 2][car.location[0]] = car_object

    # def load_board()
    # plaats dit object op positie 0,0 en 0,1 bijv. 


    def move(self, cars_list):
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
        # eerst alle auto's 1 plek, daarna naar links, daarna zo veel mogelijk 
        # sla alle borden op in queue 
        # je maakt alle staten van het bord aan, elk object heeft eigen locatie, maar omdat het string is zijn het geen echte objecten: representatie van bord in woorden 
        # pas bij het uitpakken van een string verander je pas echt de locaties ad hand van de string en gooi je de parent weg 
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
        return new_board


    def check_won(self, cars_list): 
        """
            Checks if the game is won by checking won flag
        """
        for car in cars_list:
            if car.redcar and car.location[0] + 1 == self.size - 1:
                self.won = True
        # if self.redcar and self.location[0] + 1 == board.size - 1:
        #     board.won = True
        
    
    def is_won (self):
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


