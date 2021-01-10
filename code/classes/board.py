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
    def __init__(self, size, cars_list):
        self.board = [list(EMPTY * size) for i in range(size)]
        self.load_cars(cars_list)

    def __repr__ (self):
        return str(self.board)

    

    def load_cars(self, cars_list):
        """
            function to load a cars into the game field, fills in the car id letters into the grid
        """
        for car in cars_list:
            
            # load the board with the car description
            self.board[car.location[1]][car.location[0]] = car.description 


            if car.horizontal == True:
                self.board[car.location[1]][car.location[0]+ 1] = car.description
                if car.length > 2:
                    self.board[car.location[1]][car.location[0]+2] = car.description
            else:
                self.board[car.location[1]+1][car.location[0]] = car.description
                if car.length > 2:
                    self.board[car.location[1]+ 2][car.location[0]] = car.description

    def move(self, direction, car):
        if car.horizontal == True and direction not in HORIZONTAL_MOVES:
            return False
        elif car.horizontal == False  and direction not in VERTICAL_MOVES:
            return False
        
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
                return True
            return False
        except IndexError:
            return False
    
    def is_won(self, size, cars_list):
        for car in cars_list:
            if car.redcar == True and car.location[0] + 1 == size - 1:
                return True
        return False

    def print_board(self):
        #print('\x1b[6;31;41m' + 'X' + '\x1b[0m')
        for row in self.board:
            for item in row:
               print(f'{item} ', end="")
            print()
        
