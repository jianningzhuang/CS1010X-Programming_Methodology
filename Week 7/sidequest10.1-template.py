#
# CS1010X --- Programming Methodology
#
# Sidequest 10.1 Template
#
# Note that written answers are commented out to allow us to run your #
# code easily while grading your problem set.

from random import *
from puzzle import GameGrid

###########
# Helpers #
###########

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0],
                  accumulate(fn, initial, seq[1:]))

def flatten(mat):
    return [num for row in mat for num in row]



###########
# Task 1  #
###########

def new_game_matrix(n):
    result = []
    for i in range(n):
        result.append([0]*n)
    return result

def has_zero(mat):
    return 0 in flatten(mat)
    
##    for row in mat:
##        for elem in row:
##            if elem == 0:
##                return True
##    return False

def add_two(mat):
    if not has_zero(mat):
        return mat
    else:    
        row = randint(0, len(mat) - 1)
        column = randint(0, len(mat) - 1)
        while mat[row][column] != 0:
            row = randint(0, len(mat) - 1)
            column = randint(0, len(mat) - 1)
        mat[row][column] = 2
        return mat





###########
# Task 2  #
###########

def adjacent(n, mat):
    a = len(mat)
    if n == 0:
        return [n+1, n+a]
    elif n == a-1:
        return [n-1, n+a]
    elif n == a*(a-1):
        return [n-a, n+1]
    elif n == a**2 - 1:
        return [n-1, n-a]
    elif n%a == 0:
        return [n-a, n+1, n+a]
    elif n%a == a-1:
        return [n-a, n-1, n+a]
    elif n < a:
        return [n-1, n+1, n+a]
    elif n > a*(a-1):
        return [n-1, n+1, n-a]
    else:
        return [n-1, n+1, n-a, n+a]
    
def same_adjacent(mat):
    for i in range(len(flatten(mat))):
        for j in adjacent(i, mat):
            if flatten(mat)[i] == flatten(mat)[j]:
                return True
    return False
        

def game_status(mat):
    if 2048 in flatten(mat):
        return "win"
    elif not has_zero(mat) and not same_adjacent(mat):
        return "lose"
    else:
        return "not over"



###########
# Task 3a #
###########

def transpose(mat):
    result = []
    for i in range(len(mat[0])):
        result.append([0]*len(mat))
    for row in range(len(mat)):
        for column in range(len(mat[0])):
            result[column][row] = mat[row][column]
    return result

#print(transpose([[1, 2, 3], [4, 5, 6]]))



###########
# Task 3b #
###########

def reverse(mat):
    result = []
    for row in mat:
        new_row = []
        for i in range(len(row)):
            new_row.append(row[len(row) - 1 - i])
        result.append(new_row)
    return result

#print(reverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))



############
# Task 3ci #
############

def merge_left1(mat):
    "Your answer here"
    new_mat = []
    for i in range(len(mat)):
        new_mat.append([0] * len(mat[0]))

    #Compressing the cell first
    for i in range(len(mat)):
        pos = 0
        for j in range(len(mat[0])):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                pos += 1

    #merging
    score_increment = 0
    for i in range(len(new_mat)):
        for j in range(len(new_mat[0]) - 1):
            if (new_mat[i][j] == new_mat[i][j+1]) and (new_mat[i][j] != 0):
                new_mat[i][j] = new_mat[i][j] * 2
                score_increment += new_mat[i][j]
                new_mat[i][j+1] = 0
                
            elif new_mat[i][j-1] == 0:
                if (j-1) > 0:
                    new_mat[i][j-1] = new_mat[i][j]
                    new_mat[i][j] = 0

                

    if mat == new_mat:
        is_valid = False
    else:
        is_valid = True

    
    
    return (new_mat,is_valid,score_increment)

def merge_left(mat):
    new_matrix, is_valid, score_increment = [], False, 0
    for row in mat:
        new_row = [0]*len(row)
        current_tile, next_tile, next_available = None, None, 0
        for i in range(len(row)):
            if row[i] != 0 and current_tile == None:
                current_tile = row[i]
                new_row[next_available] = current_tile
            elif row[i] != 0:
                next_tile = row[i]
                if next_tile == current_tile:
                    new_row[next_available] = current_tile*2
                    score_increment += current_tile*2
                    next_available += 1
                    current_tile = None
                else:
                    next_available += 1
                    new_row[next_available] = next_tile
                    current_tile = next_tile
        new_matrix.append(new_row)
        is_valid = new_matrix != mat
    return (new_matrix, is_valid, score_increment)

print(merge_left([[2, 2, 2, 2], [4, 0, 0, 0], [4, 8, 0, 4], [0, 0, 0, 2]]))
            

                
                



#############
# Task 3cii #
#############

def merge_right(mat):
    return (reverse(merge_left(reverse(mat))[0]),merge_left(reverse(mat))[1],merge_left(reverse(mat))[2])

#print(merge_right([[2, 2, 0, 2], [2, 0, 2, 4], [4, 8, 0, 4], [0, 0, 0, 2]]))

def merge_up(mat):
    return (transpose(merge_left(transpose(mat))[0]), merge_left(transpose(mat))[1], merge_left(transpose(mat))[2])

#print(merge_up([[2, 2, 0, 2], [2, 0, 2, 4], [4, 8, 0, 4], [0, 0, 0, 2]]))

def merge_down(mat):
    return (transpose(reverse(merge_left(reverse(transpose(mat)))[0])), merge_left(reverse(transpose(mat)))[1], merge_left(reverse(transpose(mat)))[2])
#print(merge_down([[2, 2, 0, 2], [2, 0, 2, 4], [4, 8, 0, 4], [0, 0, 0, 2]]))

###########
# Task 3d #
###########

def text_play():
    def print_game(mat, score):
        for row in mat:
            print(''.join(map(lambda x: str(x).rjust(5), row)))
        print('score: ' + str(score))
    GRID_SIZE = 4
    score = 0
    #mat = add_two(add_two([[1024, 1024, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
    mat = add_two(add_two(new_game_matrix(GRID_SIZE)))
    print_game(mat, score)
    while True:
        move = input('Enter W, A, S, D or Q: ')
        move = move.lower()
        if move not in ('w', 'a', 's', 'd', 'q'):
            print('Invalid input!')
            continue
        if move == 'q':
            print('Quitting game.')
            return
        move_funct = {'w': merge_up,
                      'a': merge_left,
                      's': merge_down,
                      'd': merge_right}[move]
        mat, valid, score_increment = move_funct(mat)
        if not valid:
            print('Move invalid!')
            continue
        score += score_increment
        mat = add_two(mat)
        print_game(mat, score)
        status = game_status(mat)
        if status == "win":
            print("Congratulations! You've won!")
            return
        elif status == "lose":
            print("Game over. Try again!")
            return

# UNCOMMENT THE FOLLOWING LINE TO TEST YOUR GAME
#text_play()


# How would you test that the winning condition works?
# Your answer: by playing until you reach 2048!
#              Enter W, A, S, D or Q: a   #PROOF!
#               2048    2    0    0
#                  2    2    0    0
#                  0    0    0    0
#                  0    0    0    0
#               score: 2048 #highscore sia
#               Congratulations! You've won!



#              kidding ain't nobody got time for that
#              we can modify the initial matrix in text_play to have [1024, 1024, 0, 0] for its first row and try if the input 'a' wins the game


##########
# Task 4 #
##########

def make_state(matrix, total_score):
    return (matrix, total_score)

def get_matrix(state):
    return state[0]

def get_score(state):
    return state[1]

def make_new_game(n):
    return make_state(add_two(add_two((new_game_matrix(n)))), 0)

def helper(direction, state):
    if direction(get_matrix(state))[1]:
        return (make_state(add_two(direction(get_matrix(state))[0]), get_score(state) + direction(get_matrix(state))[2]), direction(get_matrix(state))[1])
    else:
        return (state, direction(get_matrix(state))[1])

def left(state):
    return helper(merge_left, state)
            
def right(state):
    return helper(merge_right, state)

def up(state):
    return helper(merge_up, state)

def down(state):
    return helper(merge_down, state)

##game_state = make_new_game(4)
##print(merge_left(get_matrix(game_state))[1])
##print(left(game_state))
##print(game_state)

# Do not edit this #
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': lambda state: (state, False)
}

# UNCOMMENT THE FOLLOWING LINE TO START THE GAME (WITHOUT UNDO)
#gamegrid = GameGrid(game_logic)




#################
# Optional Task #
#################

###########
# Task 5i #
###########

def make_new_record(mat, increment):
    return (mat, increment)

def get_record_matrix(record):
    return record[0]

def get_record_increment(record):
    return record[1]

############
# Task 5ii #
############

def make_new_records():
    return []

def push_record(new_record, stack_of_records):
    stack_of_records.append(new_record)
    return stack_of_records[-3:]

def is_empty(stack_of_records):
    return stack_of_records == []

def pop_record(stack_of_records):
    if is_empty(stack_of_records):
        return (None, None, stack_of_records)
    else:
        return (get_record_matrix(stack_of_records[-1]), get_record_increment(stack_of_records[-1]), stack_of_records[:-1])

#############
# Task 5iii #
#############

# COPY AND UPDATE YOUR FUNCTIONS HERE
def make_state(matrix, total_score, records):
    return (matrix, total_score, records)

def get_matrix(state):
    return state[0]

def get_score(state):
    return state[1]

def get_records(state):
    return state[2]

def make_new_game(n):
    return make_state(add_two(add_two((new_game_matrix(n)))), 0, make_new_records())


def helper(direction, state):
    if direction(get_matrix(state))[1]:
        return (make_state(add_two(direction(get_matrix(state))[0]),
                           get_score(state) + direction(get_matrix(state))[2],
                           push_record(make_new_record(get_matrix(state), direction(get_matrix(state))[2]), get_records(state))),
                direction(get_matrix(state))[1])
    else:
        return (state, direction(get_matrix(state))[1])

def left(state):
    return helper(merge_left, state)


def right(state):
    return helper(merge_right, state)

def up(state):
    return helper(merge_up, state)

def down(state):
    return helper(merge_down, state)

# NEW FUNCTIONS TO DEFINE
##def get_records(state):
##    "Your answer here"

def undo(state):
    if not is_empty(get_records(state)):
        return (make_state(get_matrix(pop_record(get_records(state))),
                           get_score(state) - get_score(pop_record(get_records(state))),
                           get_records(pop_record(get_records(state)))), True)
    else:
        return (state, False)


# UNCOMMENT THE FOLLOWING LINES TO START THE GAME (WITH UNDO)
game_logic = {
    'make_new_game': make_new_game,
    'game_status': game_status,
    'get_score': get_score,
    'get_matrix': get_matrix,
    'up': up,
    'down': down,
    'left': left,
    'right': right,
    'undo': undo
}
#gamegrid = GameGrid(game_logic)
