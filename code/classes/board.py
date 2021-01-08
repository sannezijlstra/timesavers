EMPTY = '_'
HORIZONTAL_MOVES = ['LEFT', 'RIGHT']
VERTICAL_MOVES = ['UP', 'DOWN']

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
            self.board[car.location[1]][car.location[0]] = car.car_id 
            if car.horizontal == True:
                self.board[car.location[1]][car.location[0]+ 1] = car.car_id
                if car.length > 2:
                    self.board[car.location[1]][car.location[0]+2] = car.car_id
            else:
                self.board[car.location[1]+1][car.location[0]] = car.car_id
                if car.length > 2:
                    self.board[car.location[1]+ 2][car.location[0]] = car.car_id

    def check_move(self, direction, car):
        if car.horizontal == True and direction not in HORIZONTAL_MOVES:
            return False 
        elif car.horizontal == False  and direction not in VERTICAL_MOVES:
            return False
        
        if direction == UP and self.board[car.location[1] - 1 ][car.location[0]] == EMPTY:
            return True
        elif direction == DOWN and self.board[car.location[1] + length -1][car.location[0]] == EMPTY:
            return True
        elif direction == LEFT and self.board[car.location[1]][car.location[0] - 1] == EMPTY:
            return True 
        elif direction == RIGHT and self.board[car.location[1]][car.location[0] + length - 1] == EMPTY:
            return True
            



    def do_move(self):
        pass
    
    def is_won(self, size, cars_list):
        for car in cars_list:
            if car.redcar == True and car.location[0] == size - 1:
                return True
        return False

    def print_board(self):
        for i in self.board:
            print(i)
        
