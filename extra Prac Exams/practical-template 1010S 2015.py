#******************************************************
#*
#*  CS1010S Practical Exam
#*  AY2015/2016, Semester 1
#*  Name: <fill in your name here>
#*
#*
#*  This template is to be used if Coursemology fails.
#*  Otherwise, answers should be uploaded to IVLE
#*  directly. 
#*
#******************************************************

###
### Question 1
###

### Your answer here.

def count_char(letter, sentence):
    count = 0
    all_lower = sentence.lower()
    for l in all_lower:
        if l == letter:
            count += 1
    return count

def char_count(freq, sentence):
    result = {}
    all_lower = sentence.lower()
    for letter in all_lower:
        if letter != " " and letter not in result:
            result[letter] = 0
        if letter != " ":
            result[letter] += 1
    ans = []
    for l in result:
        if result[l] == freq:
            ans.append(l)
    return ans
    
    
    

# Tests
sentence = 'The quick brown fox jumps over the lazy dog.'

def test_q1a():
    print(count_char('e', sentence ))
    print(count_char('t', sentence ))
    print(count_char('7', sentence ))

def test_q1b():
    print(char_count(5, sentence))
    print(char_count(4, sentence))
    print(char_count(2, sentence))

# Uncomment to test question 1
#test_q1a()
#test_q1b()


###
### Question 2
###

import csv
def read_csv(csvfilename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    rows = []

    with open(csvfilename, encoding = 'utf-8') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

### Your answer here.

def get_route_info(source_city, source_country, dest_city, dest_country, filename):
    data = read_csv(filename)[1:]
    result = {}
    for airline, s_airport, s_city, s_country, d_airport, d_city, d_country, manufacturer, model in data:
        if s_city == source_city and s_country == source_country and d_city == dest_city and d_country == dest_country:
            if airline not in result:
                result[airline] = []
            result[airline].append(model)
    return result

def get_airline_equipment_info(airline, filename):
    data = read_csv(filename)[1:]
    result = {}
    routes = []
    for airline_, s_airport, s_city, s_country, d_airport, d_city, d_country, manufacturer, model in data:
        if airline_ == airline:
            if (s_airport, s_city, s_country, d_city, d_airport, d_country) not in routes:
                routes.append((s_airport, s_city, s_country, d_city, d_airport, d_country))
            if model not in result:
                result[model] = 0
            result[model] += 1
    for m in result:
        result[m] = (result[m]/len(routes)*100)
    return result
            


# Tests
def test_q2a():
    print("Singapore -> Dubai")
    print(get_route_info("Singapore", "Singapore", "Dubai", "United Arab Emirates",\
            "airline_routes.csv"))

    print("Singapore -> Melbourne")
    print(get_route_info("Singapore", "Singapore", "Melbourne", "Australia",\
            "airline_routes.csv"))

def test_q2b():
    print("AirAsia Airlines")
    print(get_airline_equipment_info("AirAsia", "airline_routes.csv"))

    print("SilkAir")
    print(get_airline_equipment_info("SilkAir", "airline_routes.csv"))

# Uncomment to test question 2
#test_q2a()
#test_q2b()


###
### Question 3
###

### Your answer here.

class Thing:

    def __init__(self, name, mass):
        self.name = name
        self.mass = mass
        self.time = 0
        self.revert = {}

    def get_name(self):
        return self.name

    def get_mass(self):
        return self.mass

    def wait_for(self, time):
        self.time += time
        if len(self.revert) == 0:
            return "Nothing happens after " + str(time) + " mins"
        else:
            for unshrink in self.revert:
                if self.time >= unshrink:
                    temp = self.mass
                    self.mass = self.mass*(self.revert[unshrink].mass)
                    self.revert[unshrink].shrunk.remove(self)
                    del self.revert[unshrink]
                    if isinstance(self, ShrinkRay):
                        for s in self.shrunk:
                            s.mass = s.mass*(temp/self.mass)
                    return self.name + " has unshrunk to " + str(self.mass) + " kg"
            return "Nothing happens after " + str(time) + " mins"


class ShrinkRay(Thing):

    def __init__(self, mass, time, charge):
        super().__init__("Shrink Ray", mass)
        self.effect = time
        self.max = charge
        self.shrunk = []

    def shrink(self, thing):
        if self == thing:
            return "Shrink Ray cannot shrink itself"
        elif len(self.shrunk) == self.max:
            return "Maximum number of objects shrunk"
        else:
            temp = thing.mass
            thing.mass = temp/self.mass
            if isinstance(thing, ShrinkRay):
                thing.mass = max(1, thing.mass)
                for s in thing.shrunk:
                    s.mass = s.mass*(temp/thing.mass)
            self.shrunk.append(thing)
            undo = thing.time + self.effect
            thing.revert[undo] = self
            return thing.name + " has shrunk to " + str(thing.mass) + " kg"

    def things_shrunk(self):
        result = ()
        for item in self.shrunk:
            result += (item.name,)
        return result
        

# Tests

# Uncomment the following to create the objects before testing
sr1 = ShrinkRay(4, 5, 2)
sr2 = ShrinkRay(2, 2, 3)
sr3 = ShrinkRay(5, 2, 1)
kevin = Thing("Kevin", 25)
bob = Thing("Bob", 20)
moon = Thing("Moon", 7 * 10**22)

def test_q3a():
    cases = \
    ((kevin.get_name(), 'Kevin'),
    (kevin.get_mass(),  25),
    (sr1.shrink(kevin), 'Kevin has shrunk to 6.25 kg'),
    (kevin.wait_for(3), 'Nothing happens after 3 mins'),
    (sr1.shrink(bob),   'Bob has shrunk to 5.0 kg'),
    (sr1.shrink(moon),  'Maximum number of objects shrunk'),
    (set(sr1.things_shrunk()), set(('Kevin', 'Bob'))),
    (kevin.wait_for(3), 'Kevin has unshrunk to 25 kg'),
    (sr1.shrink(moon),  'Moon has shrunk to 1.75e+22 kg'),
    (set(sr1.things_shrunk()), set(('Bob', 'Moon'))),
    (bob.get_mass(),    5.0),
    (bob.wait_for(5),  'Bob has unshrunk to 20 kg'))
    print(tuple(map(lambda x:x[0] == x[1], cases)))
    return cases

def test_q3b():
    cases = \
    ((sr1.shrink(kevin), 'Kevin has shrunk to 6.25 kg'),
    (sr2.shrink(sr1),    'Shrink Ray has shrunk to 2.0 kg'),
    (kevin.get_mass(),    12.5), # Kevin's mass changed to 25/2 = 12.5 because sr1 is now 2 kg
    (sr1.shrink(sr1),    'Shrink Ray cannot shrink itself'),
    (sr3.shrink(sr1),    'Shrink Ray has shrunk to 1 kg'), # minimum mass is 1 kg
    (kevin.get_mass(),    25), # Kevin is now back to 25 kg since sr1 is now 1 kg
    (sr1.wait_for(5),    'Shrink Ray has unshrunk to 4 kg'), # sr2 and sr3 effect wears off
    (kevin.get_mass(),    6.25),# Kevin is now shrunk to 25/4 since sr1 is now 4 kg
    (kevin.wait_for(5),  'Kevin has unshrunk to 25 kg'))
    print(tuple(map(lambda x:x[0] == x[1], cases)))
    return cases
    
def test_q3c():
    cases = \
    ((sr1.shrink(kevin),   'Kevin has shrunk to 6.25 kg'), # sr1 has a time of 5
    (kevin.wait_for(4),    'Nothing happens after 4 mins'),
    (sr2.shrink(kevin),    'Kevin has shrunk to 3.125 kg'), # sr2 has a time of 2
    (kevin.wait_for(1),    'Kevin has unshrunk to 12.5 kg'), # sr1 effect wears off
    (kevin.wait_for(1),    'Kevin has unshrunk to 25 kg')) # sr2 effect wears off     
    print(tuple(map(lambda x:x[0] == x[1], cases)))
    return cases

# Uncomment to test question 3
test_q3a()
test_q3b()
test_q3c()


###
### Question 4
###

### Your answer here.

def rob(street):
    memo = {}
    def DP(n, start):
        route = street[start:] + street[:start]
        if (n, start) in memo:
            return memo[(n, start)]
        else:
            if n >= len(route) - 1:
                return 0
            else:
                max = 0
                for i in range(n + 2, len(route) + 1):
                    temp = (route[n] + DP(i, start))
                    if temp > max:
                        max = temp
                memo[(n, start)] = max
                return max
    value = None
    for j in range(len(street)):
        temp = DP(0, j)
        if value == None or temp > value:
            value = temp
        
    
    return value
        
        

def test_q4():    
    print(rob([1, 2, 1]))
        
    print(rob([0, 1, 0, 1, 0, 0, 1, 0, 1, 0]))

    print(rob(list(range(10))))
    
    street3 = [183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211] 
    print(rob(street3))

    print(rob(list(range(100))))

# Uncomment to test question 4
#test_q4()
