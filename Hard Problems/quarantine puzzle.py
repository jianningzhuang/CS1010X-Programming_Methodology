
hospital = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

def position(n, hospital):
    for i in range(len(hospital)):
        for j in range(len(hospital[0])):
            if hospital[i][j] == n:
                return [i, j]

def move(pos, hospital):
    result = []
    moveset = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for m in moveset:
        new_x = pos[0] + m[0]
        new_y = pos[1] + m[1]
        if 0 <= new_x < len(hospital) and 0 <= new_y < len(hospital[0]):
            result.append([new_x, new_y])
    return result
        

def traverse(hospital, start, end):
    result = []
    initial = [start]
    pathq = [initial]
    revisit = False
    while len(pathq) != 0:
        tmp = pathq.pop(0)
        last_node = tmp[-1]
        if last_node == end:
            result.append(tmp)
        for next in move(position(last_node,  hospital), hospital):
            if hospital[next[0]][next[1]] == start and revisit == False:
                revisit = True
                new_path = tmp + [hospital[next[0]][next[1]]]
                pathq.append(new_path)
            elif hospital[next[0]][next[1]] not in tmp:
                new_path = tmp + [hospital[next[0]][next[1]]]
                pathq.append(new_path)
    return result

def puzzle(hospital, start, end):
    result = []
    all_paths = traverse(hospital, start, end)
    for path in all_paths:
        if len(path) == 17:
            result.append(path)
    return result

print(puzzle(hospital, 13, 4))
    
