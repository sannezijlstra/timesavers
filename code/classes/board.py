EMPTY = '_'


class Board():
    def __init__(self, size, cars_list):
        self.board = [list(EMPTY * size) for i in range(size)]
        self.load_cars(cars_list)

    def __repr__ (self):
        return str(self.board)

    def load_cars(self, cars_list):
        for car in cars_list:
            print(f'{car} with location ({car.location[0]}, {car.location[1]})')
            print(type(car.location[1]))
            temp = self.board[0]
            print(temp[0])
            # hij heeft ['______'] wij willen ['_', '_','_','_','_','_']
            self.board[car.location[1] - 1][car.location[0] - 1] = car.car_id 
            if car.horizontal == True:
                self.board[car.location[1]- 1][car.location[0]] = car.car_id
            else:
                self.board[car.location[1]][car.location[0]- 1] = car.car_id

    def check_move(self):
        pass

    def do_move(self):
        pass
    
    def print_board(self):
        for i in self.board:
            print(i)
        
