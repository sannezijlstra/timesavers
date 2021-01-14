def reverse_move(direction):
    if direction == 'UP':
        return 'DOWN'
    elif direction == 'DOWN':
        return 'UP'
    elif direction == 'RIGHT':
        return 'LEFT'
    else:
        return 'RIGHT'


def find_cars_that_can(self, cars_list, count):
    cars_that_can = {}
    
    for car in cars_list:
        result = car.can_move(new_board, size)
        if result:
            cars_that_can[car] = result

    

    return cars_that_can