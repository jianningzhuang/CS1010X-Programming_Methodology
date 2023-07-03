###CG1101 Basic Sequence

###Question 1: Easy Sudoku

SIZE = 9

board = ((5, 3, 4, 6, 7, 8, 9, 1, 2),
(6, 0, 2, 1, 9, 0, 3, 4, 0),
(1, 9, 8, 3, 4, 2, 0, 6, 7),
(8, 5, 9, 7, 6, 1, 4, 2, 3),
(4, 2, 0, 8, 5, 3, 7, 9, 1),
(7, 1, 3, 9, 2, 4, 8, 5, 6),
(9, 6, 1, 0, 3, 7, 2, 8, 4),
(2, 8, 7, 4, 1, 9, 6, 0, 5),
(3, 4, 5, 2, 8, 6, 1, 7, 9))

def easy_sudoku(x, y, n):
    for entry in board[x-1]:
        if entry == n:
            return "Violation"
    for i in range(len(board)):
        if board[i][y-1] == n:
            return "Violation"
    return "No violation"

##print(easy_sudoku(2,2,7))
##print(easy_sudoku(2, 9, 2))

###Question 2: Car

def car(odometer, distances):
    count = 0
    total_distance = 0.0
    max_difference = 0.0
    for distance in distances:
        total_distance += distance
        count += 1
    for i in range(len(distances) - 1):
        difference = abs(distances[i] - distances[i+1])
        if difference > max_difference:
            max_difference = difference
    final_odometer_value = round((odometer + total_distance)%1000, 1)
    total_number_of_trips = count
    if count == 0:
        avg_dist_per_trip = 0.0
    else:
        avg_dist_per_trip = round(total_distance/count, 1)
    max_diff_between_two_consecutive_trips = round(max_difference, 1)
    return (final_odometer_value, total_number_of_trips, avg_dist_per_trip, max_diff_between_two_consecutive_trips)

#print(car(980.5, (23.8, 19, 8.2)))

###Question 3: Ordered Matrix

def check_matrix(matrix):
    one_row = ()
    for row in matrix:
        one_row += row
        
    for i in range(len(one_row)-1):
        if (one_row[i] - one_row[i+1]) > 0:
            return False
    return True

#print(check_matrix(((-1, 2, 4), (3, 5, 6))))

###CG1101 Basic Tuple

###Question 1

def get_hundredth(a, b, c):
    def helper(x):
        if type(x) != int or x <= 0:
            return None
        elif x <  100:
            return 0
        else:
            return (x%1000)//100
    return (helper(a), helper(b), helper(c))

#print(get_hundredth(1234, "Hello", 80633))

###Question 2 Standard Deviation

def deviation(real_numbers):
    total = 0
    for number in real_numbers:
        total += number
    x_bar = total/len(real_numbers)
    sum_of_squares = 0
    for i in range(len(real_numbers)):
        sum_of_squares += (real_numbers[i] - x_bar)**2
    return round((sum_of_squares/len(real_numbers))**(1/2), 2)

#print(deviation((-5, )))

###Question 3 E;evator

ELEVATOR_SPEED = 2

def operate_elevator(t1, t2):
    current_floor_1, current_floor_2 = 1, 1
    time_taken_1, time_taken_2 = 0, 0
    if t1[0] == 1:
        time_taken_1 += (abs(t1[1] - current_floor_1) + abs(t1[2] -t1[1]))*ELEVATOR_SPEED
        current_floor_1 = t1[2]
    else:
        time_taken_2 += (abs(t1[1] - current_floor_2) + abs(t1[2] -t1[1]))*ELEVATOR_SPEED
        current_floor_2 = t1[2]
    if t2[0] == 1:
        time_taken_1 += (abs(t2[1] - current_floor_1) + abs(t2[2] -t2[1]))*ELEVATOR_SPEED
        current_floor_1 = t2[2]
    else:
        time_taken_2 += (abs(t2[1] - current_floor_2) + abs(t2[2] -t2[1]))*ELEVATOR_SPEED
        current_floor_2 = t2[2]
    return ((1, time_taken_1, current_floor_1), (2, time_taken_2, current_floor_2))

#print(operate_elevator((1, 9, 7), (1, 3, 10)))

###Question 4 Pascal Triangle

def pascal(n):
    if n == 1:
        return (1, )
    elif n == 2:
        return ((1, ), (1, 1))
    else:
        previous_row = pascal(n-1)[-1]
        current_row = ()
        for i in range(len(previous_row)-1):
            current_row += ((previous_row[i] + previous_row[i+1]), )
        return pascal(n-1) + ((1, ) + current_row + (1, ), )

#print(pascal(5))

###Mini Sudoku

SIZE = 4
board1 = [[1, 0, 3, 0], [3, 0, 0, 2], [4, 3, 2, 1], [0, 0, 0, 3]]
board2 = [[0, 1, 3, 2], [2, 0, 1, 0], [1, 0, 0, 3], [3, 4, 2, 1]]
board3 = [[0, 0, 0, 0], [0, 1, 2, 4], [0, 3, 4, 1], [0, 4, 0, 2]]

def fill_row(board):
    filled = False
    for row in board:
        if row.count(0) == 1:
            row[row.index(0)] = SIZE*(SIZE+1)//2 - sum(row)
            filled = True
    return filled
    

def fill_col(board):
    filled = False
    for i in range(SIZE):
        new_column = []
        for row in board:
            new_column.append(row[i])
        if new_column.count(0) == 1:
            board[new_column.index(0)][i] = SIZE*(SIZE+1)//2 - sum(new_column)
            filled = True
    return filled



def fill_section(board):
    filled = False
    for k in range(SIZE):
        new_section = []
        for i in range(int(k//(SIZE**(1/2)))*2, int(SIZE**(1/2)) + int(k//(SIZE**(1/2)))*2):
            for j in range(int(k%(SIZE**(1/2)))*2, int(SIZE**(1/2)) + int(k%(SIZE**(1/2)))*2):
                new_section.append(board[i][j])
        if new_section.count(0) == 1:
            board[new_section.index(0)//int(SIZE**(1/2)) + int(k//(SIZE**(1/2)))*2][new_section.index(0)%int(SIZE**(1/2)) + int(k%(SIZE**(1/2)))*2] = SIZE*(SIZE+1)//2 - sum(new_section)
            filled = True
    
    return filled

def fill_board(board):
    fillable = True  # indicate if a board is still fillable
    while fillable:
        fill_row(board)
        fill_col(board)
        fill_section(board)
        fillable = fill_row(board) or fill_col(board) or fill_section(board)
        
        
    # if still fillable, you shall continue filling it
    # if no longer fillable, shall return the board
    # write your code here
    return board

##fill_row(board3)
##fill_col(board3)
##fill_section(board3)
##print(board3)
print(fill_board(board3))

###Polygons

def make_vertex(x, y):
    return (x, y)       # x, y coordinates

def get_x(vertex):
    return vertex[0]

def get_y(vertex):
    return vertex[1]

def rep_vtx(vertex):
    return "(" + str(get_x(vertex)) + ", " + str(get_y(vertex)) + ")"

vertices1 = [make_vertex(x, y) for x, y in [(0, 10), (5, 20), (10, 10), (8, 0), (2, 0)]]
vertices2 = [make_vertex(x, y) for x, y in [(0, 0), (-6, -2), (4, -2), (0, 5)]]
vertices3 = [make_vertex(x, y) for x, y in [(52, 53), (39, 55), (18, 8)]]


def make_polygon(vertices):
    return [vertices, len(vertices)]

def get_vertices(polygon):
    return polygon[0]

def count_vertices(polygon):
    return polygon[1]


polygon1 = make_polygon(vertices1)
polygon2 = make_polygon(vertices2)
polygon3 = make_polygon(vertices3)

# check if all vertices are in the polygon
def polygon_contains(polygon, vertices):
    for vtx_rep in list(map(rep_vtx, get_vertices(polygon1))):
        if vtx_rep not in list(map(rep_vtx, vertices1)):
            return False

    return True

def calculate_area(polygon):
    # MODIFY AS NECESSARY
    minX, minY = None, None # left-bottom point of bounding box
    maxX, maxY = None, None # right-top   point of bounding box
    
    ## YOUR SOLUTION HERE #
    for i in range(count_vertices(polygon)):
        if maxX == None or get_x(get_vertices(polygon)[i]) > maxX:
            maxX = get_x(get_vertices(polygon)[i])
        if maxY == None or get_y(get_vertices(polygon)[i]) > maxY:
            maxY = get_y(get_vertices(polygon)[i])
        if minX == None or get_x(get_vertices(polygon)[i]) < minX:
            minX = get_x(get_vertices(polygon)[i])
        if minY == None or get_y(get_vertices(polygon)[i]) < minY:
            minY = get_y(get_vertices(polygon)[i])
    print(maxX, minX, maxY, minY)
    return (maxX - minX)*(maxY - minY)

#print(calculate_area(polygon1))

def determinant(pt1, pt2, pt3):
    return get_x(pt1)*(get_y(pt2)*1 - get_y(pt3)*1) - get_y(pt1)*(get_x(pt2)*1 - get_x(pt3)*1) + 1*(get_x(pt2)*get_y(pt3) - get_x(pt3)*get_y(pt2))

def is_convex(polygon):
    convex = True
    for i in range(count_vertices(polygon)):
        if determinant(get_vertices(polygon)[0], get_vertices(polygon)[1], get_vertices(polygon)[2]) < 0:
            if determinant(get_vertices(polygon)[i], get_vertices(polygon)[(i+1)%count_vertices(polygon)], get_vertices(polygon)[(i+2)%count_vertices(polygon)]) > 0:
                convex = False
        else:
            if determinant(get_vertices(polygon)[i], get_vertices(polygon)[(i+1)%count_vertices(polygon)], get_vertices(polygon)[(i+2)%count_vertices(polygon)]) < 0:
                convex = False
        print(determinant(get_vertices(polygon)[i], get_vertices(polygon)[(i+1)%count_vertices(polygon)], get_vertices(polygon)[(i+2)%count_vertices(polygon)]))
            
    return convex

#print(is_convex(polygon1))


###Working with sequences

###Question 1

def rabbit(rocks):
    jumps, position = 0, 0
    while position < rocks[-1]:
        new_position = position
        for rock in rocks:
            if position < rock <= position + 50 and rock > new_position:
                new_position = rock
        if position == new_position:
            return -1
        position = new_position
        jumps += 1
    return jumps

#print(rabbit((50, 51, 101, 102, 152, 153, 203, 204, 254, 255, 305, 306, 356, 357, 407)))

###Question 2 Cache

def cache(slots):
    memory = []
    time = 0
    for item in slots:
        if item in memory:
            memory.remove(item)
            memory.append(item)
            time += 20
        else:
            time += 100
            memory.append(item)
            memory = memory[-8:]

        print(memory)
    
    return time

#print(cache((3, 51, 24, 12, 3, 7, 51, 8, 90, 10, 5, 24)))

### Merge

def merge(tup1, tup2):
    i, j = 0, 0
    merged_list = ()
    while i < len(tup1) and j < len(tup2):
        if tup1[i] < tup2[j]:
            merged_list += (tup1[i], )
            i += 1
        else:
            merged_list += (tup2[j], )
            j += 1
    if i == len(tup1):
        for leftover in tup2[j:]:
            merged_list += (leftover, )
    else:
        for leftover in tup1[i:]:
            merged_list += (leftover, )
    return merged_list

#print(merge((-3, 8, 65, 100, 207), (-10, 20, 30, 40, 65, 80, 90)))

###Question 4

def reverse_tuple(tup):
    result = ()
    for i in range(len(tup)):
        result += (tup[-i-1], )
    return result

def reverse_tuple_recursive(tup):
    if len(tup) == 1:
        return tup
    else:
        return (tup[-1], ) + reverse_tuple_recursive(tup[:-1])

def reverse_tuple_recursive1(tup):
    if len(tup) == 1:
        return tup
    else:
        return reverse_tuple_recursive(tup[1:]) + (tup[0], )

#print(reverse_tuple_recursive1((1, 2, 3, 4, 5, 6, 7, 8, 9)))

###Question 5
def repeat(string):
    frequencies = {}
    result = 0
    for letter in string:
        if letter not in frequencies:
            frequencies[letter] = 1
        else:
            frequencies[letter] += 1
    for frequency in frequencies.values():
        if frequency > 1:
            result += 1
    return result

def repeat1(string):
    frequency = []
    visited = []
    result = 0
    for letter in string:
        if letter in frequency and letter not in visited:
            visited.append(letter)
        else:
            frequency.append(letter)
    return len(visited)

#print(repeat1('the QUICK bRoWn FoX'))

###Question 6

def repeat3(string):
    result = 0
    counter = 0
    current_letter = string[0]
    for i in range(1, len(string)):
        if string[i] == current_letter and i!=len(string)-1:
            counter += 1
            continue
            
        else:
            current_letter = string[i]
            if counter >= 1:
                result += 1
                counter = 0
    return result

print(repeat3('hssisss'))


































