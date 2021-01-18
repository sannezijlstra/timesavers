
def reverse_move(direction):
    if direction == 'UP':
        return 'DOWN'
    elif direction == 'DOWN':
        return 'UP'
    elif direction == 'RIGHT':
        return 'LEFT'
    else:
        return 'RIGHT'