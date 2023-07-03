import csv
from math import sqrt

##############
# Question 1 #
##############


##################################
# Q1a - Is right angle triangle? #
##################################



def pythagoras(a,b,c):
    side1 = (a[0] - b[0])**2 + (a[1] - b[1])**2
    side2 = (a[0] - c[0])**2 + (a[1] - c[1])**2
    side3 = (c[0] - b[0])**2 + (c[1] - b[1])**2
    return (side1 + side2) == side3 or (side1 + side3) == side2 or (side3 + side2) == side1
    

    
def test1a():
    print('=== Q1a ===')
    print(pythagoras((0,0),(1,2),(1,1))==False)
    print(pythagoras((0,0),(1,0),(0,1))==True)
    print(pythagoras((0,0),(2,0),(0,2))==True)
   
test1a()

#########################
# Q1b - Count triangles #
#########################

def count_triangles(lst):
    count = 0
    for i in range(len(lst) - 2):
        for j in range(i + 1, len(lst) - 1):
            for k in range(j + 1, len(lst)):
                if pythagoras(lst[i], lst[j], lst[k]):
                    count += 1
    return count
                
    
def test1b():
    print('=== Q1b ===')
    print(count_triangles(((0,0),(1,0),(0,1)))==1)
    print(count_triangles(((0,0),(1,1),(2,1)))==0)
    print(count_triangles(((0,0),(1,0),(0,1),(-1,-2)))==2)  # [[(0, 0), (1, 0), (0, 1)], [(1, 0), (0, 1), (-1, -2)]]
    print(count_triangles(((0,0),(1,0),(0,1),(1,1)))==4)

test1b()
 
###########################
# Q2 - Finding Happiness  #
###########################
# These functions are provided for you
# Do not make any changes to them
def approx(a,b):
    return (a-b)*(a-b)<0.0000001

def read_csv(filename):  # provided
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)
 
#######
# Q2A #
#######

stats = ['GDP', 'Social', 'HLE', 'Freedom', 'Generosity']

def parse_data(filename):
    data = read_csv(filename)[1:]
    result = {}
    for country, year, gdp, social, hle, freedom, generosity in data:
        if int(year) not in result:
            result[int(year)] = {}
        if country not in result[int(year)]:
            result[int(year)][country] = {}
        if gdp != "":
            result[int(year)][country]["GDP"] = float(gdp)
        if social != "":
            result[int(year)][country]["Social"] = float(social)
        if hle != "":
            result[int(year)][country]["HLE"] = float(hle)
        if freedom != "":
            result[int(year)][country]["Freedom"] = float(freedom)
        if generosity != "":
            result[int(year)][country]["Generosity"] = float(generosity)
    return result
        
        
    


def test2a():
    print('=== Q2a ===')
    report = parse_data("happiness.csv")
    print(approx(report[2017]['India']['Social'], 0.6067674756) == True)
    print(approx(report[2013]['Singapore']['GDP'], 11.2714776993) == True)
    print(approx(report[2014]['Brazil']['Generosity'], -0.1286974549) == True)
    print(approx(report[2008]['Austria']['Freedom'], 0.8790692687) == True)
    print(approx(report[2011]['Chile']['HLE'], 68.6461639404) == True)
    try:
        report[2007]['Canada']['Social']
    except KeyError as e:
        print(e) # 'Social'

test2a()

#######
# Q2B #
#######
def get_all_countries(data_map):
    countries = []
    for v in data_map.values():
        for k in v.keys():
            if k not in countries:
                countries.append(k)
    return countries

def get_countries(filename,*conditions):
    data = parse_data(filename)
    result = []
    if not conditions:
        return get_all_countries(data)
    else:   
        for country in get_all_countries(data):
            flag = False
            for condition in conditions:
                flag = False
                for year in data:
                    try:
                        if condition(year, data[year][country]):
                            flag = True
                            break
                    except KeyError:
                        continue
                if flag == True:
                    continue
                else:
                    break
            if flag == True:
                result.append(country)
    print(result)
    return result
                
                    

            
        
        

## Tests ##
def test2b():
    print('=== Q2b ===')
    print(get_countries("happiness.csv", lambda y, c: y >= 2012 and c['GDP'] > 11, lambda y, c: y == 2011 and c['Social'] > 0.9)==['Ireland', 'Singapore', 'Luxembourg']) 
    print(get_countries("happiness.csv", lambda y, c: y == 2012 and c['GDP'] > 11, lambda y, c: y == 2011 and c['Social'] > 0.9)==['Luxembourg']) 
    print(get_countries("happiness.csv", lambda y, c: y > 2020 and c['GDP'] > 0)==[]) 

test2b()

#######
# Q2C #
#######
def predict(filename, country, metric, year):
    data = parse_data(filename)
    data_tuples = []
    for y in data:
        if country in data[y]:
            if metric in data[y][country]:
                data_tuples.append((y, data[y][country][metric]))
    if data_tuples == []:
        return None
    sum_y = 0
    sum_x = 0
    sum_xy = 0
    sum_x2 = 0
    sum_y2 = 0
    for pair in data_tuples:
        sum_y += pair[1]
        sum_x += pair[0]
        sum_xy += pair[0]*pair[1]
        sum_x2 += pair[0]**2
        sum_y2 += pair[1]**2

    a = (sum_y * sum_x2 - sum_x * sum_xy)/(len(data_tuples)*sum_x2 - (sum_x)**2)
    b = (len(data_tuples)*sum_xy - sum_x * sum_y)/(len(data_tuples)*sum_x2 - (sum_x)**2)
    print(a + b*year)
    return a + b*year

        
 
## Tests ##
def test2c():
    print('=== Q2c ===')
    print(approx(predict("happiness.csv", "Japan", "GDP", 2050), 10.786426327185783) == True) 
    print(approx(predict("happiness.csv", "Italy", "Social", 2030), 0.9245298996310285) == True)
    print(approx(predict("happiness.csv", "Nigeria", "Generosity", 2019), 0.018709013077190306) == True) 
     
test2c()

#########################
# Q3 - Trump-Kim Summit #
#########################

class TripPlanner:

    def __init__(self, filename):
        # add your code here
        self.graph = {}
        self.places = {}

        # Do not modify this line.
        self.read(filename)       
    
    def read(self, filename):   # Provided Helper - do not modify
        data = read_csv(filename)
        for line in data:
            if line[0] == "JOIN":
                to_add = list(filter(lambda x: x !="", line[1:]))
                self.add_junction(*to_add)
            elif line[0] == "BUILDING":
                self.add_place(line[1],line[2])
            else:
                print("Error:", line)

    def add_junction(self, *roads):
        for road1 in roads:
            for road2 in roads:
                if road1 == road2:
                    continue
                else:
                    if road1 not in self.graph:
                        self.graph[road1] = {}
                        self.graph[road1]["connected"] = [road2]
                        self.graph[road1]["status"] = "unblocked"
                    else:
                        if road2 not in self.graph[road1]["connected"]:
                            self.graph[road1]["connected"].append(road2)

    def add_place(self, place, road):
        if place not in self.places:
            self.places[place] = [road]
        else:
            if road not in self.places[place]:
                self.places[place].append(road)

    def is_connected(self, road1, road2):
        if road1 not in self.graph or road2 not in self.graph:
            return "No such road"
        else:
            if road2 in self.graph[road1]["connected"]:
                return True
            else:
                return False
            
    def get_road(self, place):
        if place not in self.places:
            return "No such place"
        else:
            return self.places[place][0]

    def block_road(self, road):
        if road not in self.graph:
            return "No such road"
        else:
            if self.graph[road]["status"] == "blocked":
                return False
            else:
                self.graph[road]["status"] = "blocked"
                return True

    def unblock_road(self, road):
        if road not in self.graph:
            return "No such road"
        else:
            if self.graph[road]["status"] == "unblocked":
                return False
            else:
                self.graph[road]["status"] = "unblocked"
                return True

    def is_blocked(self, road):
        if road in self.graph:
            if self.graph[road]["status"] == "blocked":
                return True
            else:
                return False
    def can_reach(self, place1, place2):
        if place1 not in self.places or place2 not in self.places:
            return "No such place"
        else:
            start = self.get_road(place1)
            end = self.get_road(place2)
            if self.graph[start]["status"] == "blocked":
                return False
            initial = [start]
            pathq = [initial]
            while len(pathq) != 0:
                tmp = pathq.pop(0)
                last_node = tmp[-1]
                if last_node == end:
                    return True
                for next in self.graph[last_node]["connected"]:
                    if next not in tmp and self.graph[next]["status"] != "blocked":
                        new_path = tmp + [next]
                        pathq.append(new_path)
            return False
            
        

    
    
        
## Tests ##
def test3():
    print('=== Q3 ===')
    t = TripPlanner("orchard.csv")
    print(t.can_reach('Gleneagles Hospital', 'St Regis')==True)
    print(t.can_reach('Four Seasons', 'St Regis')==True)
    print(t.can_reach('M&S', 'St Regis')==True)
    print(t.can_reach('Marriot', 'St Regis')==True)
    print(t.can_reach('Shangri La', 'St Regis')==True)
    print(t.is_connected('Tanglin Road', 'Orchard Road A')==True)
    print(t.is_connected('Tanglin Road', 'Paterson Road')==False)
    print(t.get_road('Shangri La')=="Orange Grove Road")
    print(t.places)
    print(t.block_road('Cuscaden Road')==True)
    print(t.block_road('Cuscaden Road')==False)
    print(t.can_reach('Gleneagles Hospital', 'St Regis')==False)
    print(t.can_reach('Four Seasons', 'St Regis')==False)
    print(t.can_reach('M&S', 'St Regis')==False)
    print(t.can_reach('Marriot', 'St Regis')==False)
    print(t.can_reach('Shangri La', 'St Regis')==False)

    print(t.unblock_road('Cuscaden Road')==True)
    print(t.unblock_road('Cuscaden Road')==False)
    print(t.can_reach('Shangri La', 'St Regis')==True)
    print(t.block_road('Orange Grove Road')==True)
    print("check")
    print(t.can_reach('Shangri La', 'St Regis')==False)
    print(t.can_reach('Gleneagles Hospital','Marriot')==True)

test3()
