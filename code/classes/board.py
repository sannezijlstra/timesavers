EMPTY = '_'
HORIZONTAL_MOVES = ['LEFT', 'RIGHT']
VERTICAL_MOVES = ['UP', 'DOWN']

CRED = '\033[91m'
CEND = '\033[0m'

class Board():
    """
        class for supporting the game of rush hour
        needs a size and list of cars to generate a new game
    """
    def __init__(self, size, cars_list, random=False):
        self.board = [list(EMPTY * size) for i in range(size)]
        self.cars = cars_list
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

    
    def move(self, cars_list):
        # kopie van het huidige bord maken en met move 1 aanpassing maken
        # move moet een nieuwe instantie aanmaken in plaats van zichzelf aanpassen
        # kijken naar het bord ipv naar de auto's
        # steeds opnieuw een bord aanmaken 
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

    def print_board(self):
        """
            iterate over the board rows and items to print the board
        """
        for row in self.board:
            for item in row:
               print(f'{item} ', end="")
            print()


