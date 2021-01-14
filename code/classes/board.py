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
    def __init__(self, size, cars_list, won=False):
        self.board = [list(EMPTY * size) for i in range(size)]
        self.load_cars(cars_list)
        self.size = size
        self.won = won
        self.empty = [] # of variabele aan car toevoegen van is_movable, waarbij we checken na de move of er nog een vakje is

    def __repr__ (self):
        return str(self.board)

    def load_cars(self, cars_list):
        """
            function to load a cars into the game field, fills in the car id letters into the grid
        """
        for car in cars_list:
            # load the board with description on initial car location
            self.board[car.location[1]][car.location[0]] = car.description

            # load the rest of the car object in horizontal or vertical direction
            if car.horizontal:
                self.board[car.location[1]][car.location[0]+ 1] = car.description
                # if car is a truck load another space in grid with object
                if car.length > 2:
                    self.board[car.location[1]][car.location[0]+2] = car.description
            else:
                self.board[car.location[1]+1][car.location[0]] = car.description
                # if car is a truck load another space in grid with object
                if car.length > 2:
                    self.board[car.location[1]+ 2][car.location[0]] = car.description


    def is_won(self):
        """
            Checks if the game is won by checking won flag
        """
        return self.won

    def print_board(self):
        """
            iterate over the board rows and items to print the board
        """
        for row in self.board:
            for item in row:
               print(f'{item} ', end="")
            print()
    

     

