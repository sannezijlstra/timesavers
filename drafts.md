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
