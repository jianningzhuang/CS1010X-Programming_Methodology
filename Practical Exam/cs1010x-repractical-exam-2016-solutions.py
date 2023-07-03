######################################
#   CS1010X AY2014/2015 Semester 2   #
#  Solutions for Re-Practical Exam   #
######################################

########################
# Q1 - Circular Primes #
########################

from math import *

#################
# Q1a - Warm Up #
#################

def rotations(n):
    result = []
    s = str(n)
    for i in range(len(str(n))):
        num = int(s[i:]+s[:i])
        if num not in result:
            result.append(num)
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

def test1a_private():
    print('Q1a private')
    status = []
    def test(x):
        if x is not True:
            status.append(test_name+" => FAILED!")
        else:
            status.append(True)

    test_name = "Two zeroes in the middle"
    test(sorted(rotations(1001))==sorted([1001, 11, 110, 1100]))

    test_name = "Three zeroes in the end"
    test(sorted(rotations(1000))==sorted([1000, 1, 10, 100]))

    test_name = "LONG number"
    test(sorted(rotations(987612345))==sorted([987612345, 876123459, 761234598, 612345987, 123459876, 234598761, 345987612, 459876123, 598761234]))

    test_name = "Only 1 digit different"
    test(sorted(rotations(333313333))==sorted([333313333, 333133333, 331333333, 313333333, 133333333, 333333331, 333333313, 333333133, 333331333]))

    test_name = "Two numbers repeated in contiguous manner"
    test(sorted(rotations(22223333))==sorted([22223333, 22233332, 22333322, 23333222, 33332222, 33322223, 33222233, 32222333]))

    test_name = "Two numbers repeated in non-contiguous manner"
    test(sorted(rotations(22332233))==sorted([22332233, 23322332, 33223322, 32233223]))

    test_name = "Palindrome input"
    test(sorted(rotations(543212345))==sorted([543212345, 432123455, 321234554, 212345543, 123455432, 234554321, 345543212, 455432123, 554321234]))

    for s in status:
        print(s)


#test1a()
#test1a_private()

###############################
# Q1b - Count Circular Primes #
###############################

def is_prime(n):
    if n==1:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def is_circular_prime(n):
    for i in rotations(n):
        if not is_prime(i):
            return False
    return True


def count_circular_primes(n):
    count = 0
    for i in range(2,n+1):
        if is_circular_prime(i):
            count += 1
    return count

def test1b():
    print('Q1b')
    print(count_circular_primes(2)==1)
    print(count_circular_primes(4)==2)
    print(count_circular_primes(13)==6)
    print(count_circular_primes(57)==9)
    print(count_circular_primes(100)==13)
    
def test1b_private():
    print('Q1b private')
    status = []
    def test(x):
        if x is not True:
            status.append(test_name+" => FAILED!")
        else:
            status.append(True)

    test_name = "Test for input 1"
    test(count_circular_primes(1)==0)

    test_name = "Test for input 200"
    test(count_circular_primes(200)==17)

    test_name = "Test for input 74"
    test(count_circular_primes(74)==11)

    for s in status:
        print(s)

#test1b()
#test1b_private()

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
def get_num_flights(src,dst,filename):
    data = import_csv(filename)
    count = 0
    for airline, source, destination, flights in data:
        if source==src and dst==destination:
            count += 1
    return count

def test2a():
    print('Q2a')
    print(get_num_flights('VIE','HAM','flight_routes.csv')==1)
    print(get_num_flights('SIN','MNL','flight_routes.csv')==3)
    print(get_num_flights('SIN','HAV','flight_routes.csv')==0)

def test2a_private():
    print('Q2a private')
    status = []
    def test(x):
        if x is not True:
            status.append(test_name+" => FAILED!")
        else:
            status.append(True)
    
    test_name = "Invalid source airport"
    test(get_num_flights('BOB','SIN','flight_routes.csv')==0)
    
    test_name = "Invalid destination airport"
    test(get_num_flights('SIN','BOB','flight_routes.csv')==0)

    test_name = "Both source and destination invalid"
    test(get_num_flights('BOB','FNJ','flight_routes.csv')==0)

    test_name = "Even # of flights"
    test(get_num_flights('MAA','SIN','flight_routes.csv')==2)

    for s in status:
        print(s)
    
#test2a()
#test2a_private()

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

def test2b_private():
    print('Q2b private')
    status = []
    def test(x):
        if x is not True:
            status.append(test_name+" => FAILED!")
        else:
            status.append(True)

    test_name="All airports tie"
    model_ans = [('DME', 1), ('MAA', 1), ('NAG', 1), ('NBC', 1), ('PNQ', 1), ('SIN', 1)]
    test(get_top_k_hubs(6,'topk_all-tie.csv') == model_ans)  # checking for alpha ordering

    test_name="k greater than number of airports"
    model_ans = [('DME', 1), ('MAA', 1), ('NAG', 1), ('NBC', 1), ('PNQ', 1), ('SIN', 1)]
    test(sorted(get_top_k_hubs(10,'topk_all-tie.csv')) == sorted(model_ans)) # we are only checking for presence & NOT alpha ordering in this test

    test_name="k greater than number of airports plus alpha ordering"
    model_ans = [('DME', 1), ('MAA', 1), ('NAG', 1), ('NBC', 1), ('PNQ', 1), ('SIN', 1)]
    test(get_top_k_hubs(10,'topk_all-tie.csv') == model_ans)

    test_name="Tie with the kth airport"
    model_ans = [('MAA', 3), ('BLR', 2), ('BOM', 2), ('NAG', 2)]
    test(sorted(get_top_k_hubs(2,'topk_tie-with-kth.csv')) == sorted(model_ans)) # again alpha ordering being not checked here

    test_name="Tie with the kth airport plus alpha ordering"
    model_ans = [('MAA', 3), ('BLR', 2), ('BOM', 2), ('NAG', 2)]
    test(get_top_k_hubs(2,'topk_tie-with-kth.csv') == model_ans)

    test_name="Large k"
    model_ans = [('SIN', 224), ('MNL', 144), ('CGN', 134), ('CTU', 122), \
                 ('KMG', 107), ('CKG', 94), ('STR', 90), ('HAM', 84), ('MEX', 82), \
                 ('DUS', 78), ('DME', 70), ('PVG', 68), ('DEL', 61), ('CEB', 59), \
                 ('TXL', 56), ('BET', 53), ('BOM', 47), ('ATL', 46), ('FAI', 46), \
                 ('OME', 45), ('CCU', 44), ('SHA', 43), ('YZF', 43), ('IST', 42), \
                 ('XIY', 42), ('OTZ', 41), ('ICN', 40), ('YVR', 39), ('LED', 36), ('ZRH', 36)]
    test(get_top_k_hubs(30,'flight_routes.csv')==model_ans) # also tests alpha ordering & tie with kth airport
    
    for s in status:
        print(s)

#test2b()
#test2b_private()
    

#######################
# Q2c - Flight Search #
#######################

##def search_routes(src,dest,filename,n):
##    data = import_csv(filename)
##    links = {}
##    for airline, source, destination, flights in data:
##        if source not in links:
##            links[source] = [destination]
##        elif destination not in links[source]:
##            links[source].append(destination)
##
##    answer = []
##    route_set = [[src]]
##    for i in range(n):
##        
##        # Generate routes
##        new_set = []
##        for route in route_set:
##            if route[-1] in links: # route[-1] should be a source for at least one destination
##                for destination in links[route[-1]]:
##                    if destination not in route: # cannot have repeats
##                        new_route = route.copy()
##                        new_route.append(destination)
##                        new_set.append(new_route)
##
##        # Deal with the routes
##        for route in new_set:
##            if route[-1]== dest and route not in answer:
##                answer.append(route) # Found one route
##            else:
##                route_set.append(route)
##                
##    return answer

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

def test2c_private():
    print('Q2c private')
    status = []
    def test(x):
        if x is not True:
            status.append(test_name+" => FAILED!")
        else:
            status.append(True)

    def check_ordering(routes):
        curr_size=0
        for route in routes:
            if len(route)>=curr_size:
                curr_size=len(route)
            else:
                return False
        return True

    test_name="No route found - Single Hop"
    test(search_routes('SIN','HAV','flight_routes.csv',1)==[])

    test_name="No route found - Multi Hop"
    test(search_routes('SIN','HAV','flight_routes.csv',3)==[])

    test_name="No outgoing flights from the source"
    test(search_routes('NDJ','SIN','flight_routes.csv',2)==[])

    test_name="No outgoing route from an airport during a search"
    model_ans=[['JED', 'DAC', 'SIN'], ['JED', 'RUH', 'SIN']]
    test(sorted(search_routes('JED','SIN','flight_routes.csv',2))==sorted(model_ans))

    test_name="Only correct routes without ordering"
    model_ans= [['DEL', 'SIN'], ['DEL', 'AMD', 'SIN'], ['DEL', 'BKK', 'SIN'], ['DEL', 'BLR', 'SIN'], \
                ['DEL', 'BOM', 'SIN'], ['DEL', 'CCU', 'SIN'], ['DEL', 'CJB', 'SIN'], ['DEL', 'COK', 'SIN'], \
                ['DEL', 'DXB', 'SIN'], ['DEL', 'HYD', 'SIN'], ['DEL', 'KTM', 'SIN'], ['DEL', 'MAA', 'SIN']]
    test(sorted(search_routes('DEL','SIN','flight_routes.csv',2))==sorted(model_ans))

    test_name="Correct routes with ordering"
    model_ans= [['DEL', 'SIN'], ['DEL', 'AMD', 'SIN'], ['DEL', 'BKK', 'SIN'], ['DEL', 'BLR', 'SIN'], \
                ['DEL', 'BOM', 'SIN'], ['DEL', 'CCU', 'SIN'], ['DEL', 'CJB', 'SIN'], ['DEL', 'COK', 'SIN'], \
                ['DEL', 'DXB', 'SIN'], ['DEL', 'HYD', 'SIN'], ['DEL', 'KTM', 'SIN'], ['DEL', 'MAA', 'SIN']]
    ans = search_routes('DEL','SIN','flight_routes.csv',2)
    ordering=check_ordering(ans)
    presence = sorted(ans)==sorted(model_ans)
    test((ordering and presence) == True)

    test_name="Correct routes with ordering 2"
    model_ans= [['BOM', 'SIN', 'LHR'], ['BOM', 'AMD', 'SIN', 'LHR'], ['BOM', 'BLR', 'SIN', 'LHR'], \
                ['BOM', 'CCU', 'SIN', 'LHR'], ['BOM', 'CJB', 'SIN', 'LHR'], ['BOM', 'COK', 'SIN', 'LHR'], \
                ['BOM', 'DEL', 'SIN', 'LHR'], ['BOM', 'DXB', 'SIN', 'LHR'], ['BOM', 'HYD', 'SIN', 'LHR'], \
                ['BOM', 'MAA', 'SIN', 'LHR'], ['BOM', 'TRV', 'SIN', 'LHR']]
    ans = search_routes('BOM','LHR','flight_routes.csv',3)
    ordering = check_ordering(ans)
    presence = (sorted(ans)==sorted(model_ans))
    test((ordering and presence) == True)

    test_name="Check for duplicate routes"
    model_ans=[['MAA', 'SIN']]
    test(search_routes('MAA','SIN','flight_routes.csv',1)==model_ans)

    test_name="Explicit loop checking" # This test doesn't check if all possible routes are returned
    routes = search_routes('BOM','SIN','flight_routes.csv',3)
    ans=True
    for route in routes:
        if len(route) != len(set(route)):
            ans=False
            break
    test(ans)

    test_name="Large hops - no route found"
    test(search_routes('MAA','SIN','searchRoutes_large-hops.csv',6)==[])

    test_name="Large hops - route found"
    model_ans = [['MAA', 'PNQ', 'DEL', 'CCU', 'NAG', 'BLR', 'BOM', 'SIN']]
    test(search_routes('MAA','SIN','searchRoutes_large-hops.csv',7)==model_ans)

    test_name="Large hops - no route found 2"
    test(search_routes('MAA','KUL','searchRoutes_large-hops.csv',10)==[])

    test_name="Large hops - route found 2"
    model_ans = [['MAA', 'PNQ', 'DEL', 'CCU', 'NAG', 'BLR', 'BOM', 'SIN', 'RUH', 'JED', 'DAC', 'KUL']]
    test(search_routes('MAA','KUL','searchRoutes_large-hops.csv',11)==model_ans)
    
    
    for s in status:
        print(s)
    

#test2c()
#test2c_private()

########################
# Q3 - Tech Tree Mania #
########################

##class TechTree:
##
##    def __init__(self,name):
##        self.name = name
##        self.nodes = []
##        self.parents = {} # Each node will map to a list of parent 
##        self.unlocked = [] # Unlocked technologies
##
##    def get_name(self):
##        return self.name
##
##    def add_tech(self,name):
##        if name not in self.nodes:
##            self.nodes.append(name)
##            self.parents[name] = []
##            return True
##        else:
##            return False
##
##    def add_dependency(self,parent,child):
##        if parent not in self.nodes or child not in self.nodes:
##            return False
##        if parent not in self.parents[child]:
##            self.parents[child].append(parent)
##            return True
##        else:
##            return False
##
##    def get_parents(self,name):
##        if name not in self.nodes:
##            return False
##        return self.parents[name].copy()
##
##    def get_ancestors(self,name):
##        if name not in self.nodes:
##            return False
##        ancestors = []
##        tocheck = self.parents[name].copy()
##        checked = []
##        while tocheck:
##            current = tocheck.pop()
##            if current in checked:  # This only happens if there's a loop.
##                continue
##            checked.append(current)
##            if self.parents[current]:
##                for tech in self.parents[current]:
##                    if tech not in tocheck:
##                        tocheck.append(tech)
##            if current not in ancestors:
##                ancestors.append(current)
##        return ancestors
##
##    def unlock(self,name):
##        if name not in self.nodes or name in self.unlocked:
##            return False
##
##        for tech in self.get_ancestors(name): # Check dependencies
##            if tech not in self.unlocked:
##                return False
##        self.unlocked.append(name)
##        return True
##
##    def is_unlocked(self,name):
##        return name in self.unlocked
##
##    def has_loop(self):
##        # Key insight is that we will detect the loop in get_ancestors
##        # so we just have a modified version of get_ancestors and
##        # loop through all the nodes.
##
##        def find_loop(name):
##            tocheck = self.parents[name].copy()
##            checked = []
##            while tocheck:
##                current = tocheck.pop()
##                if self.parents[current]:
##                    for tech in self.parents[current]:
##                        if tech==name:
##                            return True
##                        elif tech not in tocheck:
##                            tocheck.append(tech)
##            return False
##
##        for tech in self.nodes:
##            if find_loop(tech):
##                return True
##        return False

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
        if tech not in self.graph:
            return False
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


    print(sorted(tt.get_parents("mining"))==sorted(['stone working']))
    print(sorted(tt.get_ancestors("mining"))==sorted(['stone working']))
    print(sorted(tt.get_parents("construction"))==sorted(['iron working', 'craftsmanship', 'stone working']))
    print(sorted(tt.get_ancestors("construction"))==sorted(['stone working', 'craftsmanship', 'iron working', 'bronze working', 'metal working']))
    print(tt.is_unlocked("stone working")==False)
    print(tt.unlock("stone working")==True)
    print(tt.is_unlocked("stone working")==True)
    print(tt.is_unlocked("construction")==False)
    print(tt.unlock("construction")==False)
    print(tt.is_unlocked("construction")==False)
    print(tt.has_loop()==False)
    tt.add_dependency("construction","stone working")
    print(tt.has_loop()==True)

def test3_private():
    print('Q3 private')
    status = []
    def test(x):
        if x is not True:
            status.append(test_name+" => FAILED!")
        else:
            status.append(True)

    test_name="constructor and get_name()"
    evaltt = TechTree("EvalTechTree")
    test(evaltt.get_name()=="EvalTechTree")

    test_name="basic add_tech()"
    tt = TechTree("TechTree")
    test(tt.add_tech("stone working")==True)

    test_name="add_tech() when tech already present"
    tt = TechTree("TechTree")
    tt.add_tech("stone working")
    test(tt.add_tech("stone working")==False)

    test_name="basic add_dependency() and get_parents()"
    tt = TechTree("TechTree")
    tt.add_tech("stone working")
    tt.add_tech("mining")
    tt.add_dependency("stone working","mining")
    test(tt.get_parents("mining")==["stone working"])

    test_name="add_dependency() when neither parent nor child are present"
    tt = TechTree("TechTree")
    test(tt.add_dependency("stone working","mining")==False)

    test_name="add_dependency() when only parent is present"
    tt = TechTree("TechTree")
    tt.add_tech("stone working")
    test(tt.add_dependency("stone working","mining")==False)

    test_name="add_dependency() when only child is present"
    tt = TechTree("TechTree")
    tt.add_tech("mining")
    test(tt.add_dependency("stone working","mining")==False)

    test_name="get_parents() when tech not in tree"
    tt = TechTree("TechTree")
    tt.add_tech("mining")
    test(tt.get_parents("stone working")==False)

    test_name="get_parents() when tech is the root node"
    tt = TechTree("TechTree")
    tt.add_tech("mining")
    test(tt.get_parents("mining")==[])

    test_name="get_ancestors() when tech not in tree"
    tt = TechTree("TechTree")
    tt.add_tech("mining")
    test(tt.get_ancestors("stone working")==False)

    test_name="get_ancestors() when tech is the root node"
    tt = TechTree("TechTree")
    tt.add_tech("mining")
    test(tt.get_ancestors("mining")==[])

    def linear_tree():
        tt = TechTree("TechTree")                    #  one
        tt.add_tech("one")                           #   |
        tt.add_tech("two")                           #  two
        tt.add_tech("three")                         #   |
        tt.add_tech("four")                          #  three
        tt.add_tech("five")                          #   |
        tt.add_tech("six")                           #  four
        tt.add_tech("seven")                         #   |
        tt.add_dependency("one","two")               #  five
        tt.add_dependency("two","three")             #   |
        tt.add_dependency("three","four")            #  six
        tt.add_dependency("four","five")             #   |
        tt.add_dependency("five","six")              #  seven 
        tt.add_dependency("six","seven")
        return tt


    def three_lvl_tree():                            #  one   two   three   four
        tt = TechTree("TechTree")                    #   \    /       \      /
        tt.add_tech("one")                           #    five           six
        tt.add_tech("two")                           #       \          /
        tt.add_tech("three")                         #          seven
        tt.add_tech("four")
        tt.add_tech("five")
        tt.add_tech("six")
        tt.add_tech("seven")
        tt.add_dependency("one","five")
        tt.add_dependency("two","five")
        tt.add_dependency("three","six")
        tt.add_dependency("four","six")
        tt.add_dependency("five","seven")
        tt.add_dependency("six","seven")
        return tt

    def three_lvl_disjoint_tree():                   #  one   two   three   four
        tt = TechTree("TechTree")                    #   \    /       \      /
        tt.add_tech("one")                           #    five           six
        tt.add_tech("two")                           #       \          
        tt.add_tech("three")                         #          seven
        tt.add_tech("four")
        tt.add_tech("five")
        tt.add_tech("six")
        tt.add_tech("seven")
        tt.add_dependency("one","five")
        tt.add_dependency("two","five")
        tt.add_dependency("three","six")
        tt.add_dependency("four","six")
        tt.add_dependency("five","seven")
        return tt

    test_name="get_ancestors() of linear tree"
    tt=linear_tree()
    model_ans = ['six', 'five', 'four', 'three', 'two', 'one']
    test(sorted(tt.get_ancestors("seven"))==sorted(model_ans))
    
    test_name="get_ancestors() of 3-lvl tree"
    tt=three_lvl_tree()
    model_ans = ['six', 'four', 'three', 'five', 'two', 'one']
    test(sorted(tt.get_ancestors("seven"))==sorted(model_ans))

    test_name="basic unlock()"
    tt = TechTree("TechTree")
    tt.add_tech("mining")
    test(tt.unlock("mining")==True)

    test_name="unlock() when tech is already unlocked"
    tt = TechTree("TechTree")
    tt.add_tech("mining")
    tt.unlock("mining")
    test(tt.unlock("mining")==False)

    test_name="basic unlock() when pre-reqs are unlocked"
    tt = TechTree("TechTree")
    tt.add_tech("stone working")
    tt.add_tech("mining")
    tt.add_dependency("stone working","mining")
    tt.unlock("stone working")
    test(tt.unlock("mining")==True)

    test_name="basic unlock() when pre-reqs are NOT unlocked"
    tt = TechTree("TechTree")
    tt.add_tech("stone working")
    tt.add_tech("mining")
    tt.add_dependency("stone working","mining")
    test(tt.unlock("mining")==False)

    test_name="unlock() when deep pre-reqs are unlocked"
    tt = linear_tree()
    tt.unlock("one")
    tt.unlock("two")                      
    tt.unlock("three")                
    tt.unlock("four")
    tt.unlock("five")
    tt.unlock("six")
    test(tt.unlock("seven")==True)

    test_name="unlock() should fail when deep pre-reqs are NOT unlocked"
    tt = linear_tree()
    test(tt.unlock("seven")==False)

    test_name="unlock() should fail for a node in between a deep linear tree"
    tt = linear_tree()
    test(tt.unlock("three")==False)

    test_name="unlock() should fail for a node in between a deep non-linear tree"
    tt = three_lvl_tree()
    test(tt.unlock("six")==False)

    test_name="unlock() should succeed for a weird shape tree"                                              
    tt = three_lvl_tree()                                                                                   
    tt.add_tech("weird1")                                                                                                   
    tt.add_tech("weird2")                                                                                                   
    tt.add_tech("weird3")                                                                                                   
    tt.add_tech("weird4")                                                                                                                                                                                                    
    tt.add_dependency("weird2","two")                                                                                                   
    tt.add_dependency("weird1","weird2")
    tt.add_dependency("weird4","seven")
    tt.add_dependency("weird3","weird4")
    tt.unlock("weird1")
    tt.unlock("weird2")
    tt.unlock("weird3")
    tt.unlock("weird4")
    tt.unlock("one")
    tt.unlock("two")
    tt.unlock("three")
    tt.unlock("four")
    tt.unlock("five")
    tt.unlock("six")
    test(tt.unlock("seven")==True)

    test_name="unlock() should succeed for a disjoint tree"
    tt = three_lvl_disjoint_tree()
    tt.unlock("one")
    tt.unlock("two")
    tt.unlock("five")
    test(tt.unlock("seven")==True)

    test_name="unlock() should fail for a disjoint tree"
    tt = three_lvl_disjoint_tree()
    tt.unlock("one")
    tt.unlock("two")
    tt.unlock("five")
    test(tt.unlock("six")==False)

    test_name="basic is_unlocked() returns True/False"
    tt = TechTree("TechTree")
    tt.add_tech("stone working")
    tt.add_tech("mining")
    tt.unlock("stone working")
    test((tt.is_unlocked("stone working"),tt.is_unlocked("mining"))==(True,False))

    test_name="is_unlocked() changes on unlocking"
    tt = TechTree("TechTree")
    tt.add_tech("mining")
    test((tt.is_unlocked("mining"),tt.unlock("mining"),tt.is_unlocked("mining"))==(False,True,True))

    test_name="is_unlocked() remains True"
    tt = TechTree("TechTree")
    tt.add_tech("mining")
    tt.unlock("mining")
    test((tt.is_unlocked("mining"),tt.unlock("mining"),tt.is_unlocked("mining"))==(True,False,True))

    test_name="is_unlocked() remains False"
    tt = TechTree("TechTree")
    tt.add_tech("stone working")
    tt.add_tech("mining")
    tt.add_dependency("stone working","mining")
    test((tt.is_unlocked("mining"),tt.unlock("mining"),tt.is_unlocked("mining"))==(False,False,False))

    test_name="has_loop() False with linear tree"
    tt = linear_tree()
    test(tt.has_loop()==False)

    test_name="has_loop() False with 3-lvl tree"
    tt = three_lvl_tree()
    test(tt.has_loop()==False)

    test_name="has_loop() False with 3-lvl disjoint tree"
    tt = three_lvl_disjoint_tree()
    test(tt.has_loop()==False)

    test_name="has_loop() True with simple two nodes loop"
    tt = TechTree("TechTree")
    tt.add_tech("one")
    tt.add_tech("two")
    tt.add_dependency("one","two")
    tt.add_dependency("two","one")
    test(tt.has_loop()==True)

    test_name="has_loop() True with linear tree lower loop"
    tt = linear_tree()
    tt.add_dependency("two","one")
    test(tt.has_loop()==True)

    test_name="has_loop() True with linear tree upper loop"
    tt = linear_tree()
    tt.add_dependency("seven","six")
    test(tt.has_loop()==True)

    test_name="has_loop() True with linear tree BIG loop"
    tt = linear_tree()
    tt.add_dependency("seven","one")
    test(tt.has_loop()==True)

    test_name="has_loop() False with 3-lvl tree lower acylic loop 1"
    tt = three_lvl_tree()
    tt.add_dependency("four","three")
    test(tt.has_loop()==False)

    test_name="has_loop() False with 3-lvl tree lower acylic loop 2"
    tt = three_lvl_tree()
    tt.add_dependency("one","two")
    test(tt.has_loop()==False)

    test_name="has_loop() False with 3-lvl tree lower acylic loop 3"
    tt = three_lvl_tree()
    tt.add_dependency("three","two")
    test(tt.has_loop()==False)

    test_name="has_loop() False with 3-lvl tree lower acylic loop 4"
    tt = three_lvl_tree()
    tt.add_dependency("one","three")
    test(tt.has_loop()==False)

    test_name="has_loop() True with 3-lvl tree lower loop"
    tt = three_lvl_tree()
    tt.add_dependency("five","two")
    test(tt.has_loop()==True)

    test_name="has_loop() True with 3-lvl tree upper loop"
    tt = three_lvl_tree()
    tt.add_dependency("seven","six")
    test(tt.has_loop()==True)

    test_name="has_loop() True with 3-lvl tree BIG loop"
    tt = three_lvl_tree()
    tt.add_dependency("seven","two")
    test(tt.has_loop()==True)

    
    test_name="has_loop() True with 3-lvl disjoint tree 1"
    tt = three_lvl_disjoint_tree()
    tt.add_dependency("six","four")
    test(tt.has_loop()==True)

    test_name="has_loop() True with 3-lvl disjoint tree 2"
    tt = three_lvl_disjoint_tree()
    tt.add_dependency("seven","one")
    test(tt.has_loop()==True)
    
    
    for s in status:
        print(s) 

test3()
test3_private()
