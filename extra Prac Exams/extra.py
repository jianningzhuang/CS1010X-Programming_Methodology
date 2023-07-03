def most_frequent_unigram(string):
    frequency = {}
    for letter in string:
        if letter != " " and letter not in frequency:
            frequency[letter] = 0
        if letter != " ":
            frequency[letter] += 1
    highest = None
    unigram = None
    for letter in frequency:
        if highest == None or frequency[letter] > highest:
            highest = frequency[letter]
            unigram  = letter
    return (unigram, highest)

#print(most_frequent_unigram("a friend in need is a friend indeed"))

def most_frequent_bigram(string):
    frequency = {}
    for i in range(len(string) - 1):
        bigram = string[i] + string[i+1]
        if " " not in bigram and bigram not in frequency:
            frequency[bigram] = 0
        if " " not in bigram:
            frequency[bigram] += 1
    highest = None
    code = None
    for letter in frequency:
        if highest == None or frequency[letter] > highest:
            highest = frequency[letter]
            code  = letter
    return (code, highest)

#print(most_frequent_bigram("mississippi is missing"))


def exists(grid, target):
    for row in grid:
        for elem in row:
            if elem == target:
                return True
    return False

grid1 = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,1,1,1]]
grid2 = [[0,0,0,1],[0,0,0,1],[0,0,0,1],[0,0,0,1]]
grid3 = [[1,1,1,1],[0,0,0,0],[0,0,0,0],[1,1,1,1]]
grid4 = [[1,0,0,1],[1,0,0,1],[1,0,0,1],[1,0,0,1]]
grid5 = [[2,0,0,2],[0,1,1,0],[0,0,0,0],[1,1,1,1]]

grid6 = [[1,1,1,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
grid7 = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
grid8 = [[2,2,2,2],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
grid9 = [[2,0,0,0],[2,0,0,0],[2,0,0,0],[2,0,0,0]]
grid10 = [[4,4,0,0],[2,0,0,0],[0,0,0,0],[0,0,0,0]]

def transpose(grid):
    copy = []
    new_row = [0]*len(grid)
    for i in range(len(grid[0])):
        copy.append(list(new_row))

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            copy[j][i] = grid[i][j]
    return copy

    
def left(grid):
    result = []
    for row in grid:
        copy = [0]*len(row)
        avail = 0
        for elem in row:
            if elem != 0 and copy[avail] == 0:
                copy[avail] = elem
            elif elem != 0 and copy[avail] == elem:
                copy[avail] = 2*elem
                avail += 1
            elif elem != 0 and copy[avail] != elem:
                avail += 1
                copy[avail] = elem
        result.append(copy)
    return result
    
    
def play(grid, directions):
    for direction in directions:
        if direction == "L":
            grid = left(grid)
        if direction == "U":
            grid = transpose(left(transpose(grid)))
    return grid
        


print(play(grid5, ["U", "L"]))
















    
