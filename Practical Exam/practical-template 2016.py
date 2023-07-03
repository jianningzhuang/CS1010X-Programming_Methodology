import csv

##############
# Question 1 #
##############

#################
# Q1a - Warm Up #
#################

def contains(a, b):
    return str(b) in str(a)

def test1a():
    print('Q1a')
    print(contains(123, 123) == True)
    print(contains(1234, 123) == True)
    print(contains(4123, 123) == True)
    print(contains(123555, 123) == True)
    print(contains(123555, 23) == True)
    print(contains(1243555, 123) == False)

test1a()



########################
# Q1b - Longest Streak #
########################

def count_longest_streak(a):
    str_a = str(a)
    longest = None
    current = str_a[0]
    streak = 1
    for i in range(1, len(str_a)):
        if str_a[i] == current:
            streak += 1
        else:
            if longest == None or streak > longest:
                longest = streak
            current = str_a[i]
            streak = 1
    if longest == None or streak > longest:
        longest = streak
    return longest
        
        

def test1b():
    print('Q1b')
    print(count_longest_streak(123456789) == 1)
    print(count_longest_streak(111123456789) == 4)
    print(count_longest_streak(123444456789) == 4)
    print(count_longest_streak(11112211111) == 5)

test1b()



##############################
# Q2 - Stock Market Analysis #
##############################
# These functions are provided for you
# Do not make any changes to them

def import_csv(filename):
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)


#######################
# Q2a - Minimum Price #
#######################

def min_stock(datafile, start, end):
    data = import_csv(datafile)
    lowest = None
    for date, time, open, high, low, close, volume in data:
        if start <= int(date) <= end:
            if lowest == None or float(low) < lowest:
                lowest = float(low)
    return lowest
            

EPS = 1e-10 # For approximation of floating point answers
def close(a, b):
    return b-EPS <= a <= b+EPS

def test2a():
    print('Q2a')
    print(close(min_stock("table_tap.csv", 19980218, 19980309), 11.6277))
    print(close(min_stock("table_tap.csv", 19980102, 20130809), 11.0139))
    print(close(min_stock("table_apa.csv", 19980102, 20130809), 6.91758))

test2a()


##################
# Q2b - Volatity #
##################

def average_daily_variation(datafile, start, end):
    data = import_csv(datafile)
    fluc = []
    for date, time, open, high, low, close, volume in data:
        if start <= int(date) <= end:
            difference = float(high) - float(low)
            fluc.append(difference)
    if fluc == []:
        return None
    else:
        return sum(fluc)/len(fluc)

        

def test2b():
    print('Q2b')
    print(close(average_daily_variation("table_tap.csv", 19980218, 19980309), 0.47104285714285715))
    print(close(average_daily_variation("table_tap.csv", 19980102, 20130809), 0.668375878757002))
    print(close(average_daily_variation("table_apa.csv", 19980102, 20130809), 1.6702794752929195))

test2b()


#######################
# Q2c - Optimal Trade #
#######################

def trade_stock(datafile, start, end):
    data = import_csv(datafile)
    highest = {}
    lowest = {}
    for date, time, open, high, low, close, volume in data:
        if start <= int(date) <= end:
            highest[int(date)] = float(high)
            lowest[int(date)] = float(low)
    difference = None
    for d_h, v_h in highest.items():
        for d_l, v_l in lowest.items():
            if d_h >= d_l:
                if difference == None or (v_h - v_l) > difference:
                    difference = (v_h - v_l)
    return difference

        

def test2c():
    print('Q2c')
    print(close(trade_stock("table_tap.csv", 19980218, 19980309), 1.3630999999999993))
    print(close(trade_stock("table_tap.csv", 19980102, 20130809), 42.7361))
    print(close(trade_stock("table_apa.csv", 19980102, 20130809), 136.89742))

    # Test null set
    print(trade_stock("table_apa.csv", 20180101, 20181230)==None)

#test2c()


#####################
# Q3 - Going Places #
#####################

class Map():
    def __init__(self):
        self.nodes = []
        self.edges = {}

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes.append(name)
            self.edges[name] = {}

    def add_link(self, loc1, loc2, distance):
        if loc1 not in self.edges or loc2 not in self.edges:
            return False
        else:
            self.edges[loc1][loc2] = distance
            self.edges[loc2][loc1] = distance
    def get_distance(self, loc1, loc2):
        if loc1 not in self.edges or loc2 not in self.edges:
            return False
        else:
            return self.edges[loc1][loc2]
    
    def get_paths(self, loc1, loc2):
        result = []
        def DFS(start, end, path):
            path = path + [start]
            if start ==  end:
                result.append(path)
                return 
            for node in self.edges[start]:
                if node not in path:
                    DFS(node, end, path)
            return
        DFS(loc1, loc2, [])
        print(result)
        return result

    def shortest_path(self, loc1, loc2):
        def DFS(start, end, path, shortest, cur_dist, min_dist):
            path = path + [start]
            if start == end:
                return (path, cur_dist)
            for node in self.edges[start]:
                if node not in path:
                    if shortest == None or (cur_dist + self.get_distance(start, node)) < min_dist:
                        new_path, dist = DFS(node, end, path, shortest, (cur_dist + self.get_distance(start, node)), min_dist)
                        if new_path != None:
                            print(min_dist)
                            shortest = new_path
                            min_dist = dist
            return (shortest, min_dist)
        a, b = DFS(loc1, loc2, [], None, 0, 0)
        print(b)
        return b
                        


        
                    
                            
class Map:

    def __init__(self):
        self.nodes = []
        self.graph = {}

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes.append(name)
            self.graph[name] = {}

    def add_link(self, node1, node2, distance):
        if node1 not in self.graph or node2 not in self.graph:
            return False
        else:
            self.graph[node1][node2] = distance
            self.graph[node2][node1] = distance
            return True

    def get_distance(self, node1, node2):
        if self.graph[node1] == {} or self.graph[node2] == {}:
            return False
        else:
            return self.graph[node1][node2]

    def get_paths(self, start, end):
        if start not in self.graph or end not in self.graph:
            return []
        result = []
        initial = [start]
        pathq = [initial]
        while len(pathq) != 0:
            tmp = pathq.pop(0)
            last_node = tmp[-1]
            if last_node == end:
                result.append(tmp)
            for next in self.graph[last_node]:
                if next not in tmp:
                    new_path = tmp + [next]
                    pathq.append(new_path)
        return result

    def length(self, path):
        distance = 0
        for i in range(1, len(path)):
            distance += self.get_distance(path[i], path[i - 1])
        return distance

    def shortest_path(self, start, end):
        paths = self.get_paths(start, end)
        if paths == []:
            return False
        shortest = None
        for path in paths:
            if shortest == None or self.length(path) < shortest:
                shortest = self.length(path)
        return shortest
            
        

    
                    
                    
        
            
        


def test3():
    m = Map()
    m.add_node("Singapore")
    m.add_node("Seoul")
    m.add_node("San Francisco")
    m.add_node("Tokyo")
    m.add_link("Tokyo","Seoul",1152)
    m.add_link("Singapore","Seoul",4669)
    m.add_link("Singapore","Tokyo",5312)
    m.add_link("Tokyo","San Francisco",5136)

    def sortall(lst):
        return sorted(list(map(sortall, lst))) if type(lst) is list else lst

    print("Q3")
    print(sortall(m.get_paths("Singapore","Seoul")) ==\
            sortall([['Singapore', 'Seoul'], ['Singapore', 'Tokyo', 'Seoul']]))

    print(sortall(m.get_paths("San Francisco","Seoul")) ==\
            sortall([['San Francisco', 'Tokyo', 'Seoul'],\
            ['San Francisco', 'Tokyo', 'Singapore', 'Seoul']]))

    print(sortall(m.get_paths("Seoul","San Francisco")) ==\
            sortall([['Seoul', 'Tokyo', 'San Francisco'],\
            ['Seoul', 'Singapore', 'Tokyo', 'San Francisco']]))

    print(m.shortest_path("Singapore","Seoul") == 4669)
    print(m.shortest_path("San Francisco","Seoul") == 6288)
    print(m.shortest_path("Seoul","San Francisco") == 6288)

test3()
