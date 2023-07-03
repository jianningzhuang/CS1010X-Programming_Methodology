#
# CS1010X --- Programming Methodology
#
# Contest 10.2 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from random import *
from puzzle_AI import *
from puzzle_AI import get_average_AI_score


def heuristic(mat):
    weight = [[4**15, 4**14, 4**13, 4**12], \
              [4**8, 4**9, 4**10, 4**11], \
              [4**7, 4**6, 4**5, 4**4], \
              [4**0, 4**1, 4**2, 4**3]]

    value = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            value += mat[i][j] * weight[i][j]
    return value

def deep_copy(mat):
    if mat == []:
        return []
    elif type(mat) != list:
        return mat
    else:
        return [deep_copy(mat[0])] + deep_copy(mat[1:])

def computer_moves(mat):
    result = []

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                copy = deep_copy(mat)
                copy[i][j] = 2
                result.append(copy) 

    return result

def accumulate(fn, initial, seq):
    if not seq:
        return initial
    else:
        return fn(seq[0], 
                  accumulate(fn, initial, seq[1:]))
    
def flatten(mat):
    return [num for row in mat for num in row]

def has_zero(mat):
    return 0 in flatten(mat)

def add_two(mat):
    if not has_zero(mat):
        return mat
    a = randint(0, len(mat)-1)
    b = randint(0, len(mat)-1)
    while mat[a][b] != 0:
        a = randint(0, len(mat)-1)
        b = randint(0, len(mat)-1)
    mat[a][b] = 2
    return mat

def game_status(mat):
    for row in mat:
        for element in row:
            if element == 2048:
                return 'win'
    if has_zero(mat):
        return 'not over'
    for i in range(len(mat)): #Check horizontally
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i][j+1]:
                return 'not over'
    for i in range(len(mat)-1): #Check vertically
        for j in range(len(mat[0])):
            if mat[i][j] == mat[i+1][j]:
                return 'not over'
    return 'lose'

def transpose(mat):
    return list(map(list,zip(*mat)))

def reverse(mat):
    return list(map(lambda row: list(reversed(row)),mat))



def merge_left(matrix):
    def merge_row(row):
        merged_row, prev_tile, score_increment = [], 0, 0
        # pack element by element left-wards
        for tile in row:
            if tile == 0: continue
            if prev_tile == 0:
                prev_tile = tile
            elif prev_tile != tile:
                merged_row.append(prev_tile)
                prev_tile = tile
            else:
                merged_row.append(prev_tile*2)
                score_increment += prev_tile*2
                prev_tile = 0
        merged_row.append(prev_tile) # valid regardless whether there are merges or not
        # top up zeros
        while len(merged_row) != len(row):
            merged_row.append(0)
        return (merged_row, merged_row != row, score_increment)

    return accumulate(lambda first, rest: ([first[0]] + rest[0], 
                                            first[1] or rest[1], 
                                            first[2] + rest[2]),
                      ([], False, 0),
                      list(map(merge_row, matrix)))

def merge_right(mat):
    mat, valid, score = merge_left(reverse(mat))
    return (reverse(mat), valid, score)

def merge_up(mat):
    mat, valid, score = merge_left(transpose(mat))
    return (transpose(mat), valid, score)

def merge_down(mat):
    mat, valid, score = merge_left(reverse(transpose(mat)))
    return (transpose(reverse(mat)), valid, score)

move_funct = {'w': merge_up, 'a': merge_left, 's': merge_down, 'd': merge_right}

    
##def AI(mat):
##
##    def alphabeta(mat, depth, player, a, b):
##        if depth == 0:
##            return heuristic(mat)
##        if player == "maxi":
##            highest = -9999999999999999999
##            for move in move_funct:
##                if move_funct[move](mat)[1]:
##                    highest = max(highest, alphabeta(move_funct[move](mat)[0], depth - 1, "mini", a, b))
##                    a = max(a, highest)
##                    if a >= b:
##                        break
##            return highest
##        else:
##            lowest = 9999999999999999999
##            for move in computer_moves(mat):
##                lowest = min(lowest, alphabeta(move, depth - 1, "maxi", a, b))
##                b = min(b, lowest)
##                if a >= b:
##                    break
##            return lowest
##        
##    highest = None
##    result = None
##    for move in move_funct:
##        if move_funct[move](mat)[1]:
##            lowest = alphabeta(move_funct[move](mat)[0], 4, "mini", -99999999999999999999, 9999999999999999999999999)
##            if highest == None or lowest > highest:
##                highest = lowest
##                result = move

    
##    return result

def AI(mat):
    # replace the following line with your code
    number_of_runs = 100
    depth = 10
    left = []
    right = []
    up = []
    down = []
    moves = [merge_left, merge_right, merge_down, merge_up]
    for i in range(number_of_runs):
        temp = mat
        score = 0
        check = False
        valid = False
        while check != True:
            initial_move = moves[randint(0,3)]
            temp, check, score = initial_move(temp)
            if check:
                temp = add_two(temp)
        counter = 0
        while counter < depth:
            move = moves[randint(0,3)]
            temp, valid, additional_score = move(temp)
            if valid:
                temp = add_two(temp)
                score = score + additional_score if additional_score else score + 1
                counter = counter + 1
            if game_status(temp) != 'not over':
                break
        if score == 0:
            score = score + 1
        if initial_move == merge_left:
            left.append(score)
        elif initial_move == merge_right:
            right.append(score)
        elif initial_move == merge_up:
            up.append(score)
        elif initial_move == merge_down:
            down.append(score)
    left = [sum(left)/len(left),'a'] if left else [0, 'a']
    right = [sum(right)/len(right),'d'] if right else [0, 'd']
    up = [sum(up)/len(up),'w'] if up else [0, 'w']
    down = [sum(down)/len(down),'s'] if down else [0, 's']
    return max(left,right,up,down)[1]

##    def minimax(mat, depth, player):
##        if depth == 0:
##            return heuristic(mat)
##        if player == "maxi":
##            highest = -99999999999999
##            for move in move_funct:
##                if move_funct[move](mat)[1]:
##                    highest = max(highest, minimax(move_funct[move](mat)[0], depth - 1, "mini"))
##            return highest
##        else:
##            lowest = 9999999999999999
##            for move in computer_moves(mat):
##                lowest = min(lowest, minimax(move, depth - 1, "maxi"))
##            return lowest
##        
##    highest = None
##    result = None
##    for move in move_funct:
##        if move_funct[move](mat)[1]:
##            lowest = minimax(move_funct[move](mat)[0], 4, "mini")
##            if highest == None or lowest > highest:
##                highest = lowest
##                result = move
##
##    
##    return result

##    highest = None
##    result = None
##    for move in move_funct:
##        if move_funct[move](mat)[1]:
##            one_move = move_funct[move](mat)[0]
##            lowest = mini(computer_moves(one_move))
##            if highest == None or lowest > highest:
##                highest = lowest
##                result = move
##                
##    return result



    
##    highest = None
##    result = None
##    for move1 in move_funct:
##        if move_funct[move1](mat)[1]:
##            one_move = move_funct[move1](mat)[0]
##            for move2 in move_funct:
##                if move_funct[move2](one_move)[1]:
##                    if highest == None or heuristic(move_funct[move2](one_move)[0]) > highest:
##                        highest = heuristic(move_funct[move2](one_move)[0])
##                        print(highest)
##                        result = move1
##    return result



    
##    def minimax(mat, depth):
##        if depth == 0:
##            return [heuristic(mat), None]
##        highest = None
##        result = None
##        for move in move_funct:
##            if move_funct[move](mat)[1]:
##                if highest == None or minimax(move_funct[move](mat)[0], depth - 1)[0] > highest:
##                    highest = minimax(move_funct[move](mat)[0], depth - 1)[0]
##                    result = move
##        return [highest, result]
##    return minimax(mat, 2)[1]
            

a = [[4,4,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

#print(computer_moves(a))

    


    
    
#    return ('w', 'a', 's', 'd')[randint(0,3)]


# UNCOMMENT THE FOLLOWING LINES AND RUN TO WATCH YOUR SOLVER AT WORK
game_logic['AI'] = AI
gamegrid = GameGrid(game_logic)

# UNCOMMENT THE FOLLOWING LINE AND RUN TO GRADE YOUR SOLVER
# Note: Your solver is expected to produce only valid moves.
get_average_AI_score(AI, True)
