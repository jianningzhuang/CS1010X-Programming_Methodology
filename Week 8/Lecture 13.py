###Question 1

def normalize(lst):
    s = sum(lst)
    return list(map(lambda v: v / s, lst))

#print(normalize([1, 2, -7, 4])) #ZeroDivisionError

def safe_normalize(lst):
    try:
        normalize(lst)
    except ZeroDivisionError:
        return lst
    return normalize(lst)

#print(safe_normalize([1, 2, 2, 3]))


###Question 2
def safe_calculate(num):
    try:
        calculate(num)
    except ZeroDivisionError:
        return 0
    except TypeError:
        return None
    return calculate(num)

###Question 3

def is_leap_year(year):
    # DONE: do not need to modify
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 400 == 0:
        return True
    return False

def is_valid(d, m, y):
    # DONE: do not need to modify    
    # d, m, y represents day, month, and year in integer.
    if y < 1970 or y > 9999:
        return False
    if m < 0 or m > 12:
        return False
    if d < 0 or d > 31:
        return False

    if m == 4 or m == 6 or m == 9 or m == 11:
        if d > 30:
            return False

    if is_leap_year(y):
        if m == 2 and d > 29:
            return False
    else:
        if m == 2 and d > 28:
            return False
        
    return True

def get_day_month_year(date):
    # TODO: split the date and return a tuple of integer (day, month, year)
    d, m, y = date.split("/")
    return (int(d), int(m), int(y))

def less_than_equal(start_day, start_mon, start_year, \
                    end_day, end_mon, end_year):    
    # TODO: return true if start date is before or same as end date
    if start_year < end_year:
        return True
    if start_year == end_year:
        if start_mon < end_mon:
            return True
        elif start_mon == end_mon:
            if start_day <= end_day:
                return True
            else:
                return False
        else:
            return False
    return False

def next_date(d, m, y):
    # TODO: get the next date from the current date (d, m, y)
    # return a tuple of integer (day, month, year).
    if is_valid(d+1, m, y):
        d, m, y = d+1, m, y
    elif is_valid(1, m+1, y):
        d, m, y = 1, m+1, y
    else:
        d, m, y = 1, 1, y+1
    return (d, m, y)

def count_days(start_date, end_date):
    # date is represented as a string in format dd/mm/yyyy
    start_day, start_mon, start_year = get_day_month_year(start_date)
    end_day, end_mon, end_year = get_day_month_year(end_date)

    # TODO: check for data validity here #
    # if start date is not valid...
    # if end date is not valid...
    # if start date > end date...
    
    if not is_valid(start_day, start_mon, start_year):
        raise Exception("Not a valid date: " + start_date)
    if not is_valid(end_day, end_mon, end_year):
        raise Exception("Not a valid date: " + end_date)
    if not less_than_equal(start_day, start_mon, start_year, end_day, end_mon, end_year):
        raise Exception("Start date must be less than or equal end date.")
                        
    # lazy - let the computer count from start date to end date
    count = 0
    while less_than_equal(start_day, start_mon, start_year, end_day, end_mon, end_year):
        count = count + 1
        start_day, start_mon, start_year = next_date(start_day, start_mon, start_year)

    # exclude end date
    return count - 1

#print(count_days('1/1/1970', '31/12/1969'))


###Question 4

def pascal(row, col):
    if col == 1 or col == row:
        return 1
    else:
        return pascal(row - 1, col) + pascal(row - 1, col - 1)

def faster_pascal(row, col):
    level = [1]*(col+1)
    table = []
    for i in range(row+1):
        table.append(level.copy())
    for j in range(1, col+1):
        table[0][j] = 0
    for i in range(1, row+1):
        for j in range(1, col+1):
            table[i][j] = table[i-1][j-1] + table[i-1][j]
    return table[row-1][col-1]

memo = {}
def dp_pascal(row, col):
    if (row, col) in memo:
        return memo[(row, col)]
    elif col == 1 or col == row:
        return 1
    else:
        result = dp_pascal(row-1, col) + dp_pascal(row-1, col-1)
        memo[(row, col)] = result
    return memo[(row, col)]

#print(dp_pascal(500, 3))


###Question 5

table = {}  # table to memoize computed values

def num_of_paths(n, m):
    if (n, m) in table:
        return table[(n, m)]
    elif n == 1 or m == 1:
        return 1
    else:
        result = num_of_paths(n, m-1) + num_of_paths(n-1, m)
        table[(n, m)] = result
    return table[(n, m)]

#print(num_of_paths(3, 3))

###Question 7

def num_of_paths(maze):
    table = {}
    def dp_paths(n, m):
        if (n, m) in table:
            return table[(n, m)]
        elif n == 1 and m == 1:
            return 1
        elif maze[n-1][m-1] == 0:
            return 0
        elif m == 1:
            result = dp_paths(n-1, m)
            table[(n, m)] = result
        elif n == 1:
            result = dp_paths(n, m-1)
            table[(n, m)] = result
        else:
            result = dp_paths(n, m-1) + dp_paths(n-1, m)
            table[(n, m)] = result
        return table[(n, m)]
    return dp_paths(len(maze), len(maze[0]))


maze1 = ((1, 1, 1, 1, 1, 1, 1, 1, 0, 1),
         (1, 0, 0, 1, 1, 1, 0, 0, 1, 1),
         (0, 1, 1, 1, 0, 0, 1, 1, 1, 0),
         (1, 1, 0, 1, 1, 1, 1, 0, 1, 1),
         (0, 1, 0, 1, 0, 0, 1, 0, 1, 0),
         (1, 0, 1, 1, 1, 1, 0, 1, 1, 1),
         (1, 1, 0, 1, 0, 1, 0, 0, 1, 1),
         (0, 1, 1, 1, 1, 1, 1, 1, 1, 0),
         (1, 0, 1, 0, 0, 1, 1, 0, 1, 1),
         (1, 0, 1, 1, 1, 0, 1, 0, 1, 0),
         (1, 1, 0, 1, 0, 1, 0, 1, 1, 1))


maze2 = ((1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1),
         (1, 1, 1, 1, 1, 1, 1, 1, 1))

maze3 = ((1, 0, 1, 1),
         (1, 0, 1, 1),
         (1, 0, 1, 1),
         (1, 0, 1, 1),
         (1, 0, 1, 0),
         (1, 0, 0, 1))

print(num_of_paths(maze3))






























