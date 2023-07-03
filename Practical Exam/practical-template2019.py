from math import *


###############
# Question 1a #
###############
def smallest(*digits):
    lst = list(digits)
    lst.sort()
    if lst[0] == 0:
        for i in range(1, len(lst)):
            if lst[i] != 0:
                lst[0], lst[i] = lst[i], lst[0]
                break
    result = ""
    for d in lst:
        result += str(d)
    return int(result)



def test1a():
    print('=== Q1a ===')
    print(smallest(9,1,3)==139)
    print(smallest(1,3,9,0,0)==10039)
    print(smallest(2,1,1,3,9,0)==101239)
 
#test1a() 

###############
# Question 1b #
###############
def second_smallest(*digits):
    lst = list(digits)
    lst.sort()
    if lst[0] == 0:
        for i in range(1, len(lst)):
            if lst[i] != 0:
                lst[0], lst[i] = lst[i], lst[0]
                break
    for j in range(len(lst) - 1, 0, -1):
        if lst[j - 1] < lst[j]:
            lst[j-1], lst[j] = lst[j], lst[j - 1]
            break
    if lst[0] == 0:
        return None
    result = ""
    for d in lst:
        result += str(d)
    if int(result) == smallest(*digits):
        return None
    else:
        return int(result)
    
    

    
            
                
print("Test")
print(second_smallest(1, 0, 1, 1, 2, 2, 2))
                            
print(second_smallest(1, 0, 1, 1, 2, 2, 2) == 1012122)
def test1b():
    print('=== Q1b ===')
    print(second_smallest(9,1,3)==193)
    print(second_smallest(1,3,9,0,0)==10093)
    print(second_smallest(2,1,1,3,9,0)==101293)
    print(second_smallest(1,1,1)==None)
     
#test1b() 

##############
# Question 2 #
##############

import csv
def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

###############
# Question 2a #
###############

def most_common_major(filename, year):
    
    data = read_csv(filename)[1:]
    frequency = {}
    for y, gender, course, num in data:
        if int(y) == year and num != "na":
            if course not in frequency:
                frequency[course] = 0
            frequency[course] += int(num)
    max_val = None
    result = None
    for c in frequency:
        if max_val == None or frequency[c] > max_val:
            max_val = frequency[c]
            result = c
    return result

        
        
        
        

def test2a():
    print('=== Q2a ===')
    print(most_common_major("graduates-by-first-degree.csv", 1993)=="Engineering Sciences")
    print(most_common_major("graduates-by-first-degree.csv", 2000)=="Engineering Sciences")
    print(most_common_major("graduates-by-first-degree.csv", 2010)=="Engineering Sciences")

#test2a()

###############
# Question 2b #
###############

def new_courses(filename,start_year,end_year):
    data = read_csv(filename)[1:]
    before = []
    result = {}
    for y, gender, course, num in data:
        if int(y) <= start_year and num != "na" and int(num) > 0 and course not in before:
            before.append(course)
    for y, gender, course, num in data:
        if start_year < int(y) <= end_year and num != "na" and int(num) > 0 and course not in before:
            if course not in result:
                result[course] = int(y)
            if int(y) < result[course]:
                result[course] = int(y)
    return list(result.items())
    
    
    
##    data = read_csv(filename)
##    result = []
##    before = []
##    for major in data[1:]:
##        if int(major[0]) <= start_year and major[2] not in before and major[3] != "na" and int(major[3]) > 0:
##            before.append(major[2])
##        if start_year < int(major[0]) <= end_year and major[2] not in before and major[3] != "na" and int(major[3]) > 0:
##            before.append(major[2])
##            result.append((major[2], int(major[0])))
##    return result
            
            
        

def test2b():
    print('=== Q2b ===')
    print(new_courses("graduates-by-first-degree.csv",1993,2000)==[('Education', 1995), ('Mass Communication', 1997)]
)
    print(new_courses("graduates-by-first-degree.csv",2001,2010)==[('Applied Arts', 2003), ('Services', 2008)]
)
    print(new_courses("graduates-by-first-degree.csv",1993,2020)==[('Education', 1995), ('Mass Communication', 1997), ('Applied Arts', 2003), ('Services', 2008)])

#test2b()

###############
# Question 2c #
###############

def topk_growing_major(filename,k,start_year,end_year):
    data = read_csv(filename)[1:]
    start_data = {}
    end_data = {}
    growth = {}
    for y, gender, course, num in data:
        if int(y) == start_year and num != "na" and int(num) > 0:
            if course not in start_data:
                start_data[course] = 0
            start_data[course] += int(num)
        if int(y) == end_year and num != "na" and int(num) > 0:
            if course not in end_data:
                end_data[course] = 0
            end_data[course] += int(num)
    to_sort = []
    for c in end_data:
        if c in start_data:
            growth[c] = end_data[c]/start_data[c]
            to_sort.append([c, growth[c]])
    to_sort.sort(key = lambda x: x[1], reverse = True)
    result = list(map(lambda x: x[0], to_sort[:k]))
    i = 0
    while (k + i) < len(to_sort) and to_sort[k + i][1] == to_sort[k - 1][1]:
        result.append(to_sort[k + i][0])
        i += 1
    return result
    
        
    
##    data = read_csv(filename)
##    growth = {}
##    start_data = {}
##    end_data = {}
##    for major in data[1:]:
##        if int(major[0]) == start_year and major[3] != "na" and int(major[3]) > 0:
##            if major[2] not in start_data:
##                start_data[major[2]] = int(major[3])
##            else:
##                start_data[major[2]] += int(major[3])
##    for end in data[1:]:
##        if int(end[0]) == end_year and end[3] != "na" and int(end[3]) > 0 and end[2] in start_data:
##            if end[2] not in end_data:
##                end_data[end[2]] = int(end[3])
##            else:
##                end_data[end[2]] += int(end[3])
##    for course in end_data:
##        growth[course] = end_data[course]/start_data[course]
##    increase = list(growth.items())
##    increase.sort(key = lambda x: x[1], reverse = True)
##    top_k = list(map(lambda x: x[0], increase[:k]))
##    print(top_k)
##    return top_k
    

def test2c():
    print('=== Q2c ===')
    print(topk_growing_major("graduates-by-first-degree.csv",3,1993,2000)==['Engineering Sciences', 'Dentistry', 'Humanities & Social Sciences']
)
    print(topk_growing_major("graduates-by-first-degree.csv",2,2000,2010)==['Health Sciences', 'Education'])
    print(topk_growing_major("graduates-by-first-degree.csv",3,2000,2014)==['Health Sciences', 'Education', 'Law'])

#test2c()
    
##############
# Question 3 #
##############

class Timeline:

    def __init__(self):
        self.people = []

    def born(self, name, year, lifespan):
        p = Person(name, year, lifespan)
        p.timeline = self
        self.people.append(p)
        return p

    def get_people(self, year):
        result = []
        for p in self.people:
            if p.around(year):
                result.append((p.name, p.identity))
        print(result)
        return result

class Person:

    def __init__(self, name, year, lifespan):
        self.name = name
        self.born = year
        self.lifespan = lifespan
        self.identity = year
        self.start = year
        self.end = year + lifespan
        self.timeline = None

    def around(self, year):
        if self.start <= year < self.end:
            return True
        return False

    def jump(self, from_year, to_year, identity):
        for p in self.timeline.people:
            if p.name == self.name and p.identity == identity and p.around(from_year):
                p.end = from_year
                new = Person(p.name, p.born, p.lifespan)
                new.identity = from_year
                new.start = to_year
                new.timeline = p.timeline
                p.timeline.people.append(new)


    def kill(self, year, person, identity):
        if not self.around(year):
            return False
        for p in self.timeline.people:
            if p.name == person.name and p.identity == identity:
                if p.around(year):
                    p.end = year
                    return True
        return False
        
        
        
        
        

        

def test3():
    print('=== Q3 ===')
    t = Timeline()
    thor = t.born("Thor",518,5000)
    thanos = t.born("Thanos",1950,1000000)

    print(t.get_people(2017)==[('Thor', 518), ('Thanos', 1950)])
    print(thor.kill(2018,thanos,1950)) # whoops. Violence. :'(
    print(not thor.kill(2018,thanos,1950)) # Can't kill him twice!
    print(t.get_people(2018)==[('Thor', 518)]) # Thanos dead.
    
    thor.jump(2023,2013,518)
    thor.jump(2014,2024,2023)

    print(set(t.get_people(2013))==set([('Thor', 2023), ('Thor', 518), ('Thanos', 1950)]))
    print(set(t.get_people(2014))==set([('Thor', 518), ('Thanos', 1950)]))

    print(t.get_people(2022)==[('Thor', 518)])
    print(t.get_people(2023)==[])
    print(t.get_people(2024)==[('Thor', 2014)])

    thanos.jump(2014,2024,1950)
    print(set(t.get_people(2024))==set([('Thor', 2014), ('Thanos', 2014)]))

    # New Thor and old Thanos jumped so only old Thor left
    print(t.get_people(2014)==[('Thor', 518)]) 
    print(t.get_people(2017)==[('Thor', 518)])

    #Thanos is no longer around to die. 
    print(not thor.kill(2018,thanos,1950))


test3()


             
