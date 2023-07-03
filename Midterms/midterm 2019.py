def make_board(n):
    empty_board = ()
    for i in range(n):
        empty_row = (0, )*n
        empty_board += (empty_row, )
    return empty_board

def add_queen(b, r, c):
    if b[r][c] == 1:
        return False
    else:
        new_row = b[r][:c] + (1, ) + b[r][c+1:]
        return b[:r] + (new_row, ) + b[r+1:]

b1 = make_board(4)
b2 = add_queen(b1, 0, 1)
b3 = add_queen(b2, 1, 3)
b4 = add_queen(b3, 2, 2)
b5 = add_queen(b4, 3, 0)
b6 = add_queen(b3, 2, 0)
b7 = add_queen(b6, 3, 2)


def num_queens(b):
    count = 0
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 1:
                count += 1
    return count

def size(b):
    return len(b)

def one_per_column(b):
    for row in b:
        sum = 0
        for i in row:
            sum += i
        if sum != 1:
            return False
    return True

def one_per_row(b):
    for i in range(size(b)):
        sum = 0
        for row in b:
            sum += row[i]
        if sum != 1:
            return False
    return True

def simple_solved(b):
    return one_per_column(b) and one_per_row(b)
        

def one_per_diagonal(b):
    for i in range(size(b)):
        sum = 0
        x = i
        for j in range(size(b)):
            sum += b[x][j]
            x = (x+1)%size(b)
        if sum != 1:
            return False
    return True
            

def is_solved(b):
    return simple_solved(b) and one_per_diagonal(b)


def g(n):
    a, b, c = 1, 2, 3
    next_value = 0
    for i in range(n-2):
        next_value = c + 2*b - 2*a
        a, b, c = b, c, next_value
    return next_value

def fib(n):
    a, b = 0, 1
    for i in range(n-1):
        result = a + b
        a, b = b, result
    return result

def create_schedule(rooms):
    schedule = ()
    for room in rooms:
        schedule += ((room, )+ ((0, )*24), )
    return schedule

def is_schedule(obj):
    if type(object) == tuple and object != ():
        return True

def get_venues(schedule):
    rooms = ()
    for room_schedule in schedule:
        rooms += (room_schedule[0], )
    return rooms

def reserve(schedule, room, start, end):
    new_schedule = ()
    for room_schedule in schedule:
        if room_schedule[0] == room:
            for i in range(start, end+1):
                if room_schedule[i] == 1:
                    return False
            new_room_schedule = (room_schedule[:start]) + (1, )*(end-start+1) + (room_schedule[end + 1:])
            new_schedule += (new_room_schedule, )
        else:
            new_schedule += (room_schedule, )
    return new_schedule

def is_reserved(schedule, room, slot):
    for room_schedule in schedule:
        if room_schedule[0] == room:
            if room_schedule[slot] == 1:
                return True
            else:
                return False
def remove_reservation(schedule, room, slot):
    if is_reserved(schedule, room, slot):
        new_schedule = ()
        for room_schedule in schedule:
            if room_schedule[0] == room:
                new_room_schedule = (room_schedule[:slot]) + (0, ) + (room_schedule[slot+1:])
                new_schedule += (new_room_schedule, )
            else:
                new_schedule += (room_schedule, )
    return new_schedule


s1 = create_schedule(("LT15", "LT2", "LT19"))
s2 = reserve(s1, "LT15", 3, 5)
s3 = remove_reservation(s2, "LT15", 4)


def twice(f):
    return lambda x: f(f(x))

def thrice(f):
    return lambda x: f(f(f(x)))

def double(x):
    return 2*x

def repeated(f, n):
    if n == 1:
        return lambda x: f(x)
    else:
        return lambda x: repeated(f, n-1)(f(x))

##print(twice(double)(3))
##print(repeated(double, 2)(3))


    









    

































        
