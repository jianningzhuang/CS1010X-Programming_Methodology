def make_matrix(seq):
    mat = []
    for row in seq:
        mat.append(list(row))
    return mat

#print(make_matrix(((1,2,3), (4,5,6), (7,8,9))))

def make_matrix1(seq): #no? new matrix is mutated if we change original sequence #aliasing
    
    return seq[:]

#print(make_matrix( [[ 1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def rows(m):
    return len(m)

def cols(m):
    return len(m[0])

def get(m, x, y):
    return m[x][y]

def set(m, x, y, val):
    m[x][y] = val

def transpose(m):
    new_matrix = []
    for i in range(cols(m)):
##        new_matrix.append(list(map(lambda x: x[i], m)))
        new_row = []
        for j in range(rows(m)):
            new_row.append(m[j][i])
        new_matrix.append(new_row)
##    m.clear()
##    m.extend(new_matrix)
    return new_matrix

def print_matrix(m):
    for row in m:
        print(row)



def make_matrix2(seq):
    data = []
    for i in range(len(seq)):
        for j in range(len(seq[0])):
            if seq[i][j] != 0:
                data.append([i, j, seq[i][j]])
    return [len(seq), len(seq[0]), data]

def rows2(m):
    return m[0]

def cols2(m):
    return m[1]

def get2(m, x, y):
    for row, col, element in m[2]:
        if x == row and y == col:
            return element
    return 0
##    return m[2][x*cols2(m) + y][2]

def set2(m, x, y, val):
    for i in range(len(m[2])):
        if m[2][i][0] == x and m[2][i][1] == y:
            m[2][i][2] = val
            return #else it will append every time
    m[2].append([x, y, val])
##    m[2][x*cols2(m) + y][2] = val

def transpose2(m):
    m[0], m[1] = m[1], m[0]
    for element in m[2]:
        element[0], element[1] = element[1], element[0]
##    data = []
##    for i in range(cols2(m)):
##        for j in range(rows2(m)):
##            data.append([i, j, get2(m, j, i)])
##    return [cols2(m), rows2(m), data]

def print_matrix2(m):
    result = []
    for i in range(rows2(m)):
        result.append([0]*cols2(m))
    
    for row, col, element in m[2]:
        result[row][col] = element

    print(result)

    
    for row in result:
        print(row)
        
            
m = make_matrix2( [[ 1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print_matrix2(m)
    























            
