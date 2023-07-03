from math import *


###############
# Question 1a #
###############
##def smallest(*lst):
##    lst = list(lst)
##    lst.sort()
##    
##    if lst[0] == 0:
##        index = 0
##        for i in range(len(lst)):
##            if lst[i] != 0:
##                index = i
##                break
##        lst.insert(0,lst.pop(i))
##    
##    result = ""
##    for digit in map(str,lst):
##        result += digit
##    return int(result)
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

def test1a_e(): 
    print('=== Q1a_e ===')
    print(smallest(0, 0, 0, 0) == 0)
    print(smallest(0) == 0)
    print(smallest(1, 2, 3, 1) == 1123)
    print(smallest(1, 1, 1, 1) == 1111)
    print(smallest(1, 2, 0, 3) == 1023)
    print(smallest(9, 9, 9, 9) == 9999)
    print(smallest(7, 3, 5, 2, 0, 0 ) == 200357)
    print(smallest(0, 0, 0, 0, 0, 9) == 900000)
    print(smallest(0, 0, 0, 0, 1) == 10000)
    print(smallest(1, 2, 1, 2, 1, 2) == 111222)
    
#test1a()
test1a_e()

###############
# Question 1b #
###############
# General idea is to go back from back to front to find the
# first 2 digits that can be swapped. Need to take care of special
# case where second digit is zero. 

##def second_smallest(*lst):
##    lst = list(lst)
##    lst.sort()
##        
##    if lst[0] == 0:
##        index = 0
##        for i in range(len(lst)):
##            if lst[i] != 0:
##                index = i
##                break
##        lst.insert(0,lst.pop(i))
##    for i in range(len(lst)):
##        if i==len(lst)-1:
##            return None
##        elif lst[-i-1] != lst[-i-2]:
##            lst[-i-1],lst[-i-2]= lst[-i-2],lst[-i-1]
##            break
##        
##    if lst[0] == 0: # Special case where 2nd digit of smallest is a zero.
##        return None
##    result = ""
##    for digit in map(str,lst):
##        result += digit
##    return int(result)
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

def test1b():
    print('=== Q1b ===')
    print(second_smallest(9,1,3)==193)
    print(second_smallest(1,3,9,0,0)==10093)
    print(second_smallest(2,1,1,3,9,0)==101293)
    print(second_smallest(1,1,1)==None)
 
 
def test1b_e():
    print('=== Q1b_e ===')
    print(second_smallest(1, 2, 3, 4) == 1243)
    print(second_smallest(1, 0, 0, 0) == None)
    print(second_smallest(1, 0) == None)
    print(second_smallest(0, 1, 2, 3, 0, 0) == 100032)
    print(second_smallest(1, 2, 9, 0, 2, 1) == 101292)
    print(second_smallest(9) == None)
    print(second_smallest(0) == None)
    print(second_smallest(1, 0, 0, 2, 0, 0) == 100020)
    print(second_smallest(0, 0, 0, 0,) == None)
    print(second_smallest(1, 1, 1, 1) == None)
    print(second_smallest(1, 0, 1, 1, 2, 2, 2) == 1012122)

#test1b()
test1b_e()

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
##    data = read_csv(filename)[1:]
##    d = {}
##    
##    for year2,gender,course,number in data:
##        if int(year2) == year:
##            if course not in d:
##                d[course] = 0
##            if number != "na":
##                d[course] += int(number)
##
##    freq = list(d.items())
##    freq.sort(key=lambda x:x[1], reverse=True)
##    if freq:
##        return freq[0][0]
##    else:
##        return None

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

def test2a_e():
    print('=== Q2a_e ===')
    print(most_common_major("graduates-by-first-degree.csv", 2018) == None)
    print(most_common_major("graduates-by-first-degree.csv", 1999)=="Engineering Sciences")
    print(most_common_major("arts-by-first-degree.csv",1993)=='Media')
    print(most_common_major("arts-by-first-degree.csv",2001)=='Media')
    print(most_common_major("nalanda-graduates.csv",1200)=='Astrology')
    print(most_common_major("nalanda-graduates.csv",1271)=='Astrology')


#test2a()
test2a_e()

###############
# Question 2b #
###############

##def new_courses(filename,start_year,end_year):
##    data = read_csv(filename)[1:]
##
##    #Compute list of courses at the start
##    original=[]
##    for year2,gender,course,number in data:
##        if int(year2)<=start_year and number != "na" and int(number)>0 and course not in original:
##            original.append(course)
##    
##    new_courses = {}
##    for year2,gender,course,number in data:
##        if start_year<int(year2)<=end_year:
##            if course not in original and number != "na" and int(number)>0:
##                if course not in new_courses:
##                    new_courses[course] = int(year2)
##                elif new_courses[course]>int(year2):
##                    new_courses[course] = int(year2)
##    return list(new_courses.items())

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
def test2b():
    print('=== Q2b ===')
    print(new_courses("graduates-by-first-degree.csv",1993,2000)==[('Education', 1995), ('Mass Communication', 1997)]
)
    print(new_courses("graduates-by-first-degree.csv",2001,2010)==[('Applied Arts', 2003), ('Services', 2008)]
)
    print(new_courses("graduates-by-first-degree.csv",1993,2020)==[('Education', 1995), ('Mass Communication', 1997), ('Applied Arts', 2003), ('Services', 2008)])


def test2b_e():    
    print('=== Q2b_e ===')
    print(set(new_courses("graduates-by-first-degree.csv",1993, 1995))==set([('Education', 1995)]))
    print(set(new_courses("graduates-by-first-degree.csv",1993, 1998))==set([('Education', 1995), ('Mass Communication', 1997)]))
    print(set(new_courses("arts-by-first-degree.csv",2003, 2013))==set([('Fine Arts', 2010)]))
    print(set(new_courses("arts-by-first-degree.csv",1992, 2002))==set([('Media', 1993)]))
    print(set(new_courses("nalanda-graduates.csv",1158, 1199))==set([('Wall painting', 1159), ('Hunting', 1160), ('Cultivation', 1161), ('Mining', 1164), ('Carpentry', 1166), ('Commerce', 1171), ('Mathematics', 1173), ('Astrology', 1174)]))
    print(set(new_courses("nalanda-graduates.csv",1200, 1500))==set([]))

#test2b()
test2b_e()
        

###############
# Question 2c #
###############
##
##def topk_growing_major(filename,k,start_year,end_year):
##    data = read_csv(filename)[1:]
##    start = {}
##    end = {}
##    
##    for year2,gender,course,number in data:
##        if start_year==int(year2):
##            if course not in start:
##                start[course] = 0
##            if number != "na":
##                start[course] += int(number)
##        elif end_year==int(year2):
##            if course not in end:
##                end[course] = 0
##            if number != "na":
##                end[course] += int(number)
##
##    increase = []
##    for course in start.keys():
##        if course in end:
##            if start[course] != 0 and end[course] != 0:
##                increase.append((course,end[course]/start[course]))
##    increase.sort(key=lambda x: x[1],reverse=True)
##    if len(increase)>k:
##        increase = list(filter(lambda x: x[1]>=increase[k-1][1], increase))
##    return list(map(lambda x:x[0],increase))
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

def test2c():
    print('=== Q2c ===')
    print(topk_growing_major("graduates-by-first-degree.csv",3,1993,2000)==['Engineering Sciences', 'Dentistry', 'Humanities & Social Sciences']
)
    print(topk_growing_major("graduates-by-first-degree.csv",2,2000,2010)==['Health Sciences', 'Education'])
    print(topk_growing_major("graduates-by-first-degree.csv",3,2000,2014)==['Health Sciences', 'Education', 'Law'])


def test2c_e():    
    print('=== Q2c_e ===')
    lst = topk_growing_major("graduates-by-first-degree.csv",3,1773,1886)
    ans = []
    print(lst==ans)
    lst = topk_growing_major("graduates-by-first-degree.csv",5,1993,2000)
    ans = ['Engineering Sciences', 'Dentistry', 'Humanities & Social Sciences', 'Business & Administration', 'Information Technology']
    print(lst==ans)
    lst = topk_growing_major("graduates-by-first-degree.csv",10,2001,2002)
    ans = ['Information Technology', 'Medicine', 'Architecture & Building', 'Health Sciences', 'Education', 'Humanities & Social Sciences', 'Engineering Sciences', 'Mass Communication', 'Accountancy', 'Law']
    print(lst==ans)
    lst = topk_growing_major("graduates-by-first-degree.csv",3,1773,2001)
    ans = []
    print(lst==ans)
    lst = topk_growing_major("arts-by-first-degree.csv",30,1996,1999)
    ans = ['Liberal Arts', 'Graphic Design', 'Literature', 'Media', 'Performing Arts']
    print(lst==ans)
    lst = topk_growing_major("arts-by-first-degree.csv",7,2000,2001)
    ans = ['Liberal Arts', 'Graphic Design', 'Performing Arts', 'Literature', 'Media'] 
    print(lst==ans)
    lst = topk_growing_major("nalanda-graduates.csv",7,1200,1250)
    ans = ['Commerce', 'Mathematics', 'Pottery', 'Cultivation', 'Mining', 'Masonry', 'Carpentry']
    print(lst==ans)    
    lst = topk_growing_major("nalanda-graduates.csv",1,1263,1273)
    ans = ['Masonry'] 
    print(lst==ans)
    
#test2c()
test2c_e()
    
##############
# Question 3 #
##############

##class Timeline:
##
##    def __init__(self):
##        self.people = []
##
##    def born(self, name, year, lifespan):
##        p = Person(name,year,lifespan)
##        self.people.append(p)
##        return p
##
##    def get_people(self,year):
##        result = []
##        for p in self.people:
##            result.extend(p.get_people(year))
##        return result
##        
##class Person:
##
##    def __init__(self,name, born_year, lifespan):
##        self.name = name
##        # [True, start, end, identity, next segment] => Live
##        # [False, start, end, identity, next segment] => Dead
##        self.time_segments = [True,born_year,born_year+lifespan,born_year,None]
##
##    def jump(self, from_year, to_year, identity):
##        s = self.time_segments
##        while s != None:
##            if not s[0]:
##                return self.name+" dead, cannot jump!"
##            elif s[1]<from_year<s[2] and s[3]==identity: # Found jump segment
##
##                #Reset subsequent jump segment first.
##                s2 = s
##                while s2 != None:
##                    s[2] = s2[2]
##                    s2 = s2[4]
##
##                # Add new segment
##                new_segment = [True,to_year,s[2]-from_year+to_year,from_year,None]
##                s[4] = new_segment
##                s[2] = from_year
##                return True
##            s = s[4]
##        return False
##
##    def get_people(self,year): #Utility function
##        result = []
##        s = self.time_segments
##        while s != None:
##            if s[0] and s[1]<=year<s[2]: # Found jump segment
##                result.append((self.name, s[3]))
##            s = s[4] 
##        return result
##        
##    def kill(self, year, person, identity):
##        # Check that person is that year
##        s = self.time_segments
##        while s != None:
##            if not s[0]: # Dead
##                return False
##            elif s[1]<=year<s[2]: #Found him
##                s = True
##                break
##            s = s[4]
##        if s==None:
##            return False # Cannot find current person in year.
##        
##        # Check that victim is that year
##        s = person.time_segments
##        while s != None:
##            if not s[0]: # Dead
##                return False
##            elif s[1]<=year<s[2] and s[3]==identity: #Found him
##                break
##            s = s[4]
##        if s==None: # Cannot find victim in year.
##            return False 
##        elif s[0]==False: # Victim is already dead!
##            return False
##
##        #Kill victim
##        s[4] = [False,year,s[2],year,None]
##        s[2] = year
##        return True

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

    
#########################################################
# Marking scheme  
#########################################################

#  2.0 marks for Timeline::born()  
#      o 1/2 mark - check_correct_lifespan() - check that heroes born are not retrieved before they are born
#      o 1/2 mark - check_correct_lifespan() - check that heroes are retrieved after they are born
#      o 1 mark - new_timeline() - check if people are born correctly in a new timeline (check against global variables - people from old timeline shouldn't spill over)
#  2.0 marks for Timeline::get_people() 
#      o 1 mark - all_heroere_born() - Simple check to see if the heroes are retrieved correctly after the timeline initialization
#      o 1 mark - check_all_version_of_adam() - This function checks for making sure get_person can retrieve all versions of a person (in their respective years) created by multiple jumps
#  3.0 marks for People::kill() -                             
#      o 1 mark  - thanos_kills_spiderman()   - Simple check to see that if a guy dies in YEAR, he should no more appear in get_people( >YEAR )
#      o 1 mark  - ironman_kill_thanos()      - Check against valid and invalid kills. A kill is only possible if the guy who has to be killed exists in that year
#      o 1 mark  - all_thanos_have_vanished() - After the first version of a person is killed, all the version created by his jumps and death should also disappear         
#  3.0 marks for People::jump() -                             
#      o 1 mark    - jump_resets()           - Check that a jump will reset later death and jumps
#      o 1/2 mark  - ironman_thanos_jump()   - Check if forward jumps by characters reflect in the get_people function for that year and not in the gap
#      o 1/2 mark  - ironman_thanos_jump()   - Check if backward jumps by characters reflect in the get_people function for the earlier year and not in the gap
#      o 1/2 mark  - overlapped_jumps()      - Checks if multiple overlaps will retreive the right number of versions at different times
#      o 1/2 mark  - illegal_jumps()         - Checks that people cannot jump when they do not exist (not born, dead)  


t = None
ironman = None
spiderman = None
marvel = None
thanos = None

adam = None

d = None

print("===Q3_e===")

# basic initialization. this function is not tested as a test case
def eval_init():

    global t

    global ironman
    global spiderman
    global marvel
    global thanos

    t = Timeline()

    #initialize timeline with 4 heroes - Ironman, Spiderman, Capt. Marvel and Thanos
    ironman = t.born('Ironman', 1986, 80)
    spiderman = t.born('Spiderman', 1997, 80)
    marvel = t.born('Marvel', 1971, 200)
    thanos = t.born('Thanos', 0, 10000)

# make sure the born function returns an instance of a 'Person'
def type_of_born():
    global d
    d = Timeline()
    return type(d.born('Dummy', 2, 1))==Person

# Check if the basic functionalities of the get_people function works.
# Check for the correct representation of a Person's lifespan
# That is, they shou;d exist only between year of birth and year of death
def all_heroes_born():
    
    eval_init()
    results = []

    #Check if the objects were created and kept track of correctly
    results.append(set(t.get_people(2000))==set([('Ironman', 1986), ('Marvel', 1971), ('Thanos', 0), ('Spiderman', 1997)]))
    
    #both Ironman and spiderman are past their lifespans in the year 2100. Check the correct handling of 'lifespan' upon the creation of a new Person object
    results.append(set(t.get_people(2100))==set([('Marvel', 1971), ('Thanos', 0)]))

    return results

def check_correct_lifespan():

    all_heroes_born()
    results = []

    results.append(set(t.get_people(1800)) == set([('Thanos', 0)]))
    results.append(set(t.get_people(2050)) == set([('Ironman', 1986), ('Spiderman', 1997), ('Marvel', 1971), ('Thanos', 0)]))

    return results
# check for a simple kill operation. Checks for no corner cases
# Basically, just make sure if a person is correctly killed, they
# should accordingly dissapear from the result of the get_people
# query
def thanos_kills_spiderman():

    all_heroes_born()
    results = []

    #Both Thanos and Spiderman(1997) are alive in the year 2018. Thanos successfully kills Spiderman(1997)
    results.append(thanos.kill(2018, spiderman, 1997))
    #Spiderman should no longer exist in the year 2020. Check for the correct implementation of the kill and get_people methods
    results.append(set(t.get_people(2020))==set([('Ironman', 1986), ('Marvel', 1971), ('Thanos', 0)]))
    
    return results

def illegal_jumps():

    #none of the jumps in this function should happen!
    thanos_kills_spiderman()
    results = []

    #Thanos(0) shouldn't be able to jump from the year 120000
    thanos.jump(120000, 2050, 0)
    #ironman(1986) shouldn't be able to jump form the year 0
    ironman.jump(1950, 2201, 1986)
    #spiderman shouldn't be able to jump from the year 2020
    spiderman.jump(2020, 2050, 1997)
    
    #Check if the previous 2 jumps were executed correctly by getting the People that exist in the year 2055
    results.append(set(t.get_people(120000))== set([]))
    results.append(set(t.get_people(2260)) == set([('Thanos', 0)]))
    results.append(set(t.get_people(2055)) == set([('Thanos', 0), ('Marvel', 1971), ('Ironman', 1986)]))

    return results

# Next, check if the implementation of the jump funciton works
# If a person jumps, they should create a new version of themselves
# in the year they jump_to with the identity as the year they
# jumped from
def ironman_thanos_jump():

    thanos_kills_spiderman()
    results = []

    #Thanos(0) jumps to the future, creating a Thanos(2019) in the year 2050
    thanos.jump(2019, 2050, 0)
    #Ironman(1986) tries to catch up with Thanos, creating an Ironman(2018) in the year 2051
    ironman.jump(2018, 2051, 1986)
    
    #Check if the previous 2 jumps were executed correctly by getting the People that exist in the year 2055
    results.append(set(t.get_people(2055)) == set([('Marvel', 1971), ('Thanos', 2019), ('Ironman', 2018)]))

    return results

# Again, check for kill functionality. But this time, we check for
# invalid kills, like trying to kill a person when they do not exist
def ironman_kills_thanos():

    ironman_thanos_jump()
    results = []

    #Ironman tries to kill Thanos(0), but he doesn't exist in the year 2054. However, Thanos(2019) does.
    results.append(not ironman.kill(2054, thanos, 0))
    #So Ironman should be able to kill Thanos(2019) in the year 2054
    results.append(ironman.kill(2054, thanos, 2019))

    #Check if this kill was executed correctly through the get_people method
    results.append(set(t.get_people(2055))==set([('Ironman', 2018), ('Marvel', 1971)]))

    return results

# Check for jump function working. Makes sure the old version of a
# recently killed character is still functional and can jump
# This is a check against students just blindly deleting all instances
# of a character (in the future and the past) whenever a kill happens
def thanos_jumps_yet_again():

    ironman_kills_thanos()
    results = []

    #OG Thanos(0) jumps to the future AGAIN, creating a Thanos(2017) in the year 2060!
    thanos.jump(2017, 2060, 0)

    #Check if this jump was executed correctly by getting the people in the year 2060
    results.append(set(t.get_people(2060))==set([('Ironman', 2018), ('Marvel', 1971), ('Thanos', 2017)]))
    
    return results

# New hero is created just for the sake of the narrative. But this test
# case checks for valid and invalid kills. Also, the single valid kill in
# this funciton should erase all future version of a character 
def a_new_hero_is_born():

    thanos_jumps_yet_again()
    results = []

    global adam
    #A new hero Adam Warlock, is born at the beginning of time
    adam = t.born('Adam Warlock', 0, 200)
    
    #He kills Thanos(0) in the year 1. This kill effectively undos ALL kills/jumps made by the original. He shouldn't exist anywhere now.
    results.append(adam.kill(1, thanos, 0))

    #Simple check to make sure Adam can't kill someone when he doesn't exist at that time.
    results.append(not adam.kill(2051, marvel, 1971))

    #Adam jumps to the future, creating an Adam(2) in the year 2050. Another simple check for the correct execution of the jump method
    adam.jump(2, 2050, 0)
    results.append(set(t.get_people(2055)) == set([('Marvel', 1971), ('Ironman', 2018), ('Adam Warlock', 2)]))
    
    return results

# This funciton makes sure that when Thanos(0) is killed, all the jumps
# made by him and their subsequent jumped versions dissapear
def all_thanos_have_vanished():

    a_new_hero_is_born()
    results = []

    #Adam looking for all the other versions of Thanos, not knnowing they have dissapeared because he killed the first one!
    #Check for unsuccessful kill of Thanos(2019)
    results.append(not adam.kill(2051, thanos, 2019))
    
    adam.jump(2053, 2061, 2)
    #Another jump, another check. Also, Thanos(2017) shouldn't exist in the year 2065 because all his jumps were cancelled by Adam's kill
    results.append(set(t.get_people(2065))== set([('Ironman', 2018), ('Adam Warlock', 2053), ('Marvel', 1971)]))
    
    #Check for another unsuccessful attempt to kill
    results.append(not adam.kill(2062, thanos, 2017)) 
    
    return results

# 'Adam' travelled through time the most. Make sure all his versions
# exist in correct places.
def check_all_versions_of_adam():

    all_thanos_have_vanished()
    results = []

    #Check for the different versions of Adam created through his multiple jumps in various years
    results.append(set(t.get_people(2065)) == set([('Marvel', 1971), ('Ironman', 2018), ('Adam Warlock', 2053)]))
    results.append(set(t.get_people(1990)) == set([('Ironman', 1986), ('Marvel', 1971)]) )
    results.append(t.get_people(1) == [('Adam Warlock', 0)])
    results.append(t.get_people(200) == [])

    return results

antman = None

def overlapped_jumps():

    check_all_versions_of_adam()
	 
    global antman
    antman = t.born('Antman', 1980, 100)
    antman.jump(2020, 1975, 1980)
    antman.jump(1982, 1979, 2020)

    results = []

    results.append(set(t.get_people(1974))==set([('Marvel', 1971)]))
    results.append(set(t.get_people(1975))==set([('Marvel', 1971), ('Antman', 2020)]))
    results.append(set(t.get_people(1978))==set([('Marvel', 1971), ('Antman', 2020)]))
    results.append(set(t.get_people(1979))==set([('Marvel', 1971), ('Antman', 2020), ('Antman', 1982)]))
    results.append(set(t.get_people(1980))==set([('Marvel', 1971), ('Antman', 1980), ('Antman', 2020), ('Antman', 1982)]))
    results.append(set(t.get_people(2019))==set([('Marvel', 1971), ('Antman', 1980), ('Antman', 1982)]))

    #check for general overlapped jumps

    return results

n = None
strange = None
thor = None

# create a fresh timeline and check for correctness. This is basically
# to make sure students are not using global variables to track everything
# and even if they are, they flush out the old values once a new reality
# is created
def new_timeline():
    
    global n
    global thor 
    global strange

    results = []

    #create a fresh reality/timeline with 2 heroes in it - Thor and Dr. Strange
    n = Timeline() 
    strange = n.born('Dr. Strange', 1965, 120)
    thor = n.born('Thor', 512, 5000)

    #Check that these new reality does infact only hold instances of the new heroes, and doesn't carry over the heroes from the previously tested timeline
    #(check against using global variables to do everything)
    results.append(set(n.get_people(1800)) == set([('Thor', 512)]))
    results.append(set(n.get_people(1999)) == set([('Dr. Strange', 1965), ('Thor', 512)]))    

    return results

def jump_resets():
    new_timeline()
    results = []

    strange.kill(2000, thor, 512)
    results.append(set(n.get_people(2010))==set([('Dr. Strange', 1965)]))
    thor.jump(1995, 2005, 512)
    results.append(set(n.get_people(2010))==set([('Dr. Strange', 1965), ('Thor', 1995)]))

    return results

print("1", type_of_born())
print("2", all_heroes_born())
print("3", check_correct_lifespan())
print("4", thanos_kills_spiderman())

print("5", illegal_jumps())

print("6", ironman_thanos_jump())
print("7", ironman_kills_thanos())
print("8", thanos_jumps_yet_again())
print("9", a_new_hero_is_born())
print("10", all_thanos_have_vanished())
print("11", check_all_versions_of_adam())

print("12",overlapped_jumps())

print("13", new_timeline())
print("14", jump_resets())             
