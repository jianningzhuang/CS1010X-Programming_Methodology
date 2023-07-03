######################################
#   CS1010X AY2015/2016 Semester 2   #
#   Template for Re-Practical Exam   #
######################################

########################
# Q1 - Circular Primes #
########################

from math import *

#################
# Q1a - Warm Up #
#################

def rotations(n):
    string_n = str(n)
    result = [n]
    for i in range(len(string_n)-1):
        string_n = string_n[-1] + string_n[:-1]
        if int(string_n) not in result:
            result.append(int(string_n))
    return result
        
    

def test1a():
    print('Q1a')
    print(sorted(rotations(1))==sorted([1]))
    print(sorted(rotations(11))==sorted([11]))
    print(sorted(rotations(101))==sorted([101, 11, 110]))
    print(sorted(rotations(123))==sorted([123, 231, 312]))
    print(sorted(rotations(221))==sorted([221, 212, 122]))
    print(sorted(rotations(1231))==sorted([1231, 2311, 3112, 1123]))
    print(sorted(rotations(1212))==sorted([1212, 2121]))

test1a()


###############################
# Q1b - Count Circular Primes #
###############################

def is_prime(n): # Bonus! :-) 
    if n==1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def count_circular_primes(n):
    count = 0
    for i in range(2, n + 1):
        flag = True
        for rotation in rotations(i):
            if not is_prime(rotation):
                flag = False
                break
        if flag == True:
            count += 1
    return count
        

def test1b():
    print('Q1b')
    print(count_circular_primes(2)==1)
    print(count_circular_primes(4)==2)
    print(count_circular_primes(13)==6)
    print(count_circular_primes(57)==9)
    print(count_circular_primes(100)==13)

test1b()

##############################
# Q2 - Tyrion's Flight Mania #
##############################
# DATA Reference : quantquote.com
import csv

def import_csv(filename):
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)

#########################
# Q2a - Get Num Flights #
#########################
def get_num_flights(src, dst, filename):
    data = import_csv(filename)
    count = 0
    for airline, source, destination, aircraft in data:
        if source == src and destination == dst:
            count += 1
    return count
        

def test2a():
    print('Q2a')
    print(get_num_flights('VIE','HAM','flight_routes.csv')==1)
    print(get_num_flights('SIN','MNL','flight_routes.csv')==3)
    print(get_num_flights('SIN','HAV','flight_routes.csv')==0)

test2a()

#####################
# Q2b  - Top K Hubs #
#####################

def get_top_k_hubs(k, filename):
    data = import_csv(filename)
    freq = {}
    for airline, source, destination, aircraft in data:
        if source not in freq:
            freq[source] = 0
        freq[source] += 1
        if destination not in freq:
            freq[destination] = 0
        freq[destination] += 1

    sorting = []

    for key, value in freq.items():
        sorting.append((key, value))

    sorting.sort(key = lambda x: x[0])
    sorting.sort(key = lambda x: x[1], reverse = True)

    result = sorting[:k]
    i = 0
    while (k + i) < len(sorting) and sorting[k+i][1] == sorting[k-1][1]:
        result.append(sorting[k+i])
        i += 1

    return result

        
    
    

def test2b():
    print('Q2b')
    print(get_top_k_hubs(1,'flight_routes.csv')==[('SIN', 224)])
    print(get_top_k_hubs(2,'flight_routes.csv')==[('SIN', 224), ('MNL', 144)])
    print(get_top_k_hubs(3,'flight_routes.csv')==[('SIN', 224), ('MNL', 144), ('CGN', 134)])
    print(get_top_k_hubs(4,'flight_routes.csv')==[('SIN', 224), ('MNL', 144), ('CGN', 134), ('CTU', 122)])

test2b()

#######################
# Q2c - Flight Search #
#######################

def search_routes(src, dest, filename, n):
    data = import_csv(filename)
    graph = {}
    for airline, source, destination, aircraft in data:
        if source not in graph:
            graph[source] = []
        if destination not in graph:
            graph[destination] = []
        if destination not in graph[source]:
            graph[source].append(destination)

    if src not in graph:
        return []

    result = []
    initial = [src]
    pathq = [initial]
    while len(pathq) != 0:
        tmp = pathq.pop(0)
        last_node = tmp[-1]
        if last_node == dest:
            result.append(tmp)
        for next in graph[last_node]:
            if next not in tmp and len(tmp) <= n:
                new_path = tmp + [next]
                pathq.append(new_path)
    return result

    
    

def test2c():
    print('Q2c')

    def order_not_increasing(lst): # returns True if routes are NOT arranged in increasing order
        curr_size = 0
        for i in lst:
            if curr_size <= len(i):
                curr_size = len(i)
            else:
                return True
        return False

    ans1 = search_routes('LED','NBC','flight_routes.csv',1)
    model_ans1 = [['LED','NBC']]
    ans2 = search_routes('LED','NBC','flight_routes.csv',2)
    model_ans2 = [['LED', 'NBC'], ['LED', 'DME', 'NBC']]
    ans3 = search_routes('LED','NBC','flight_routes.csv',3)
    model_ans3 = [['LED', 'NBC'], ['LED', 'DME', 'NBC'], ['LED', 'KZN', 'DME', 'NBC'], ['LED', 'KZN', 'SVX', 'NBC'], ['LED', 'UUA', 'DME', 'NBC'], ['LED', 'ASF', 'DME', 'NBC'], ['LED', 'SCW', 'SVX', 'NBC'], ['LED', 'OVB', 'SVX', 'NBC'], ['LED', 'DYU', 'DME', 'NBC'], ['LED', 'DYU', 'SVX', 'NBC'], ['LED', 'LBD', 'DME', 'NBC'], ['LED', 'CSY', 'DME', 'NBC'], ['LED', 'MCX', 'DME', 'NBC'], ['LED', 'SKX', 'DME', 'NBC'], ['LED', 'VOZ', 'DME', 'NBC']]

    if order_not_increasing(ans1):
        print(False)
    else:
        print(sorted(ans1)==sorted(model_ans1))
    if order_not_increasing(ans2):
        print(False)
    else:
        print(sorted(ans2)==sorted(model_ans2))
    if order_not_increasing(ans3):
        print(False)
    else:
        print(sorted(ans3)==sorted(model_ans3))

test2c()


########################
# Q3 - Tech Tree Mania #
########################

class TechTree:

    def __init__(self, name):
        self.name = name
        self.graph = {}

    def get_name(self):
        return self.name

    def add_tech(self, tech):
        if tech in self.graph:
            return False
        else:
            self.graph[tech] = {}
            self.graph[tech]["parents"] = []
            self.graph[tech]["children"] = []
            self.graph[tech]["status"] = "locked"
            return True


    def add_dependency(self, parent, child):
        if parent not in self.graph or child not in self.graph:
            return False
        else:
            if child not in self.graph[parent]["children"]:
                self.graph[parent]["children"].append(child)
            if parent not in self.graph[child]["parents"]:
                self.graph[child]["parents"].append(parent)
            return True

    def get_parents(self, tech):
        if tech not in self.graph:
            return False
        return self.graph[tech]["parents"]

    def get_ancestors(self, tech):
        if tech not in self.graph:
            return False
        result = []
        initial = [tech]
        pathq = [initial]
        while len(pathq) != 0:
            tmp = pathq.pop(0)
            last_node = tmp[-1]
            for parent in self.graph[last_node]["parents"]:
                if parent not in result:
                    result.append(parent)
            for parent in self.graph[last_node]["parents"]:
                if parent not in tmp:
                    new_path = tmp + [parent]
                    pathq.append(new_path)
        return result

    def unlock(self, tech):
        if self.graph[tech]["status"] == "unlocked":
            return False
        for ancestor in self.get_ancestors(tech):
            if self.graph[tech]["status"] == "locked":
                return False
        self.graph[tech]["status"] = "unlocked"
        return True

    def is_unlocked(self, tech):
        return self.graph[tech]["status"] == "unlocked"

    def tech_loop(self, tech):
        initial = [tech]
        pathq = [initial]
        while len(pathq) != 0:
            tmp = pathq.pop(0)
            last_node = tmp[-1]
            for parent in self.graph[last_node]["parents"]:
                if parent in tmp:
                    return True
                else:
                    new_path = tmp + [parent]
                    pathq.append(new_path)
        return False



            
    def has_loop(self):
        for tech in self.graph:
            if self.tech_loop(tech):
                return True
        return False
        
                
        

def test3():
    print("Q3")
    tt = TechTree("civilization")
    tt.add_tech("metal working")
    tt.add_tech("stone working")
    tt.add_tech("bronze working")
    tt.add_tech("iron working")
    tt.add_tech("construction")
    tt.add_tech("mining")
    tt.add_tech("craftsmanship")
    tt.add_dependency("metal working","bronze working")
    tt.add_dependency("bronze working","iron working")
    tt.add_dependency("iron working","construction")
    tt.add_dependency("stone working","mining")
    tt.add_dependency("stone working","craftsmanship")
    tt.add_dependency("craftsmanship","construction")
    tt.add_dependency("stone working","construction")

    print(tt.graph)

    print(sorted(tt.get_parents("mining"))==sorted(['stone working']))
    print(sorted(tt.get_ancestors("mining"))==sorted(['stone working']))
    print(sorted(tt.get_parents("construction"))==sorted(['iron working', 'craftsmanship', 'stone working']))
    print(sorted(tt.get_ancestors("construction"))==sorted(['stone working', 'craftsmanship', 'iron working', 'bronze working', 'metal working']))
    print(tt.is_unlocked("stone working")==False)
    print(tt.unlock("stone working")==True)
    print(tt.is_unlocked("stone working")==True)
    print(tt.graph)
    print(tt.is_unlocked("construction")==False)
    print(tt.unlock("construction")==False)
    print(tt.is_unlocked("construction")==False)
    print(tt.has_loop()==False)
    tt.add_dependency("construction","stone working")
    print(tt.has_loop()==True)

test3()
