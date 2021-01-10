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
            if car.horizontal == True:
                self.board[car.location[1]][car.location[0]+ 1] = car.description
                # if car is a truck load another space in grid with object
                if car.length > 2:
                    self.board[car.location[1]][car.location[0]+2] = car.description
            else:
                self.board[car.location[1]+1][car.location[0]] = car.description
                # if car is a truck load another space in grid with object
                if car.length > 2:
                    self.board[car.location[1]+ 2][car.location[0]] = car.description

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
        
