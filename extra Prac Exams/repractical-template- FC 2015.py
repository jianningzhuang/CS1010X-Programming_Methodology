#******************************************************
#*
#*  CS1010FC Re-Practical Exam
#*  AY2014/2015, Semester 2
#*  Name: <fill in your name here>
#*
#*
#*  This template is to be used if Coursemology fails.
#*  Otherwise, answers should be uploaded to Coursemology
#*  directly. 
#*
#******************************************************

# For use in testing
def compare(actual, expected):
    if actual == expected:
        return "PASS"
    else:
        return "FAIL! (expected " + str(expected) + " got " + str(actual) + ")"

###
### Question 1
###

class NumGen:
    def __init__(self):
        self.num  = 0
    
    def get(self):
        self.num += 1
        return self.num

### Your answer here.

def mass_get(gen, n):
    result = []
    for i in range(n):
        result.append(gen.get())
    return result

class FilterGen(object):

    def __init__(self, gen, filter):
        self.num = gen.num
        self.filter = filter

    def get(self):
        while not self.filter(self.num + 1):
            self.num += 1
        self.num += 1
        return self.num

def gfilter(g, f):
    return FilterGen(g, f)
    




# Tests
def test_q1a():
    print("Testing Q1A")
    a = NumGen()
    print("mass_get(a,10):",compare(mass_get(a,10),[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print("mass_get(a,10):",compare(mass_get(a,10),[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print("===========================================")

def test_q1b():
    print("Testing Q1B")
    a = NumGen()
    print("a.get():",compare(a.get(),1))
    print("a.get():",compare(a.get(),2))
    b = gfilter(a, lambda x: x%2==0)
    print("b.get():",compare(b.get(),4))
    print("b.get():",compare(b.get(),6))
    print("===========================================")

# Uncomment to test question 1
#test_q1a()
#test_q1b()

###
### Question 2
###

import csv
def read_csv(filename):
    """
    Reads a csv file and returns a list of list
    containing rows in the csv file and its entries.
    """
    with open(filename, 'r') as f:
        lines = tuple(f)[1:] # remove header
    entries = map(lambda x: x[:-1].split(','), lines) # split line 
    return list(entries)

### Your answer here.

def most_pop_categories(year, age_group, filename):
    data = read_csv(filename)
    freq = []
    for y, ag, pop, cat, p in data:
        if int(y) == year and ag == age_group:
            freq.append([cat, int(p)])
    freq.sort(key = lambda x: x[1], reverse = True)
    result = [freq[0][0]]
    i = 1
    while freq[i][1] == freq[0][1] and i < len(result):
        result.append(freq[i][0])
        i += 1
    return result
        

def increasing_trend(age_group, filename):
    data = read_csv(filename)
    bc = {}
    for y, ag, pop, cat, p in data:
        if ag == age_group:
            if cat not in bc:
                bc[cat] = []
            bc[cat].append([y, p])
    result = []
    for c in bc:
        increasing = True
        bc[c].sort(key = lambda x: x[0])
        for i in range(1, len(bc[c])):
            if bc[c][i][1] <= bc[c][i-1][1]:
                increasing = False
                break
        if increasing == True and bc[c] != []:
            result.append(c)
    return result
        
            
    



# Tests
def test_q2a():
    print("Testing Q2A")
    print("most_pop_categories(2008, '15-24 YEARS', 'shopping.csv'):", compare(most_pop_categories(2008, '15-24 YEARS', 'shopping.csv'),['CLOTHING/ FOOTWEAR/ SPORTING GOODS OR ACCESSORIES']))
    print("most_pop_categories(2009, '25-34 YEARS', 'shopping.csv'):", compare(most_pop_categories(2009, '25-34 YEARS', 'shopping.csv'),['TRAVEL PRODUCTS']))
    print("most_pop_categories(2010, '35-49 YEARS', 'shopping.csv'):", compare(most_pop_categories(2010, '35-49 YEARS', 'shopping.csv'),['TRAVEL PRODUCTS']))
    print("most_pop_categories(2011, '50-59 YEARS', 'shopping.csv'):", compare(most_pop_categories(2011, '50-59 YEARS', 'shopping.csv'),['TRAVEL PRODUCTS']))
    print("most_pop_categories(2012, '60 YEARS & ABOVE', 'shopping.csv'):", compare(most_pop_categories(2012, '60 YEARS & ABOVE', 'shopping.csv'),['TRAVEL PRODUCTS']))
    print("most_pop_categories(2008, '25-34 YEARS', 'shopping.csv'):", compare(most_pop_categories(2008, '25-34 YEARS', 'shopping.csv'),['TRAVEL PRODUCTS']))
    print("most_pop_categories(2009, '35-49 YEARS', 'shopping.csv'):", compare(most_pop_categories(2009, '35-49 YEARS', 'shopping.csv'),['TRAVEL PRODUCTS']))
    print("most_pop_categories(2010, '50-59 YEARS', 'shopping.csv'):", compare(most_pop_categories(2010, '50-59 YEARS', 'shopping.csv'),['TRAVEL PRODUCTS']))
    print("most_pop_categories(2011, '60 YEARS & ABOVE', 'shopping.csv'):", compare(most_pop_categories(2011, '60 YEARS & ABOVE', 'shopping.csv'),['TRAVEL PRODUCTS']))
    print("most_pop_categories(2012, '15-24 YEARS', 'shopping.csv'):", compare(most_pop_categories(2012, '15-24 YEARS', 'shopping.csv'),['CLOTHING/ FOOTWEAR/ SPORTING GOODS OR ACCESSORIES']))
    print("===========================================")

def test_q2b():
    print("Testing Q2B")
    print("increasing_trend('15-24 YEARS', 'shopping.csv'):", compare(increasing_trend('15-24 YEARS', 'shopping.csv'),['CLOTHING/ FOOTWEAR/ SPORTING GOODS OR ACCESSORIES']))
    print("increasing_trend('25-34 YEARS', 'shopping.csv'):", compare(increasing_trend('25-34 YEARS', 'shopping.csv'),['CLOTHING/ FOOTWEAR/ SPORTING GOODS OR ACCESSORIES']))
    print("increasing_trend('35-49 YEARS', 'shopping.csv'):", compare(increasing_trend('35-49 YEARS', 'shopping.csv'),['CLOTHING/ FOOTWEAR/ SPORTING GOODS OR ACCESSORIES']))
    print("increasing_trend('50-59 YEARS', 'shopping.csv'):", compare(increasing_trend('50-59 YEARS', 'shopping.csv'),[]))
    print("increasing_trend('60 YEARS & ABOVE', 'shopping.csv'):", compare(increasing_trend('60 YEARS & ABOVE', 'shopping.csv'),[]))
    print("===========================================")

# Uncomment to test question 2
#test_q2a()
#test_q2b()

###
### Question 3
###

### Your answer here.

class AI:
    def __init__(self, name, health):
        self.name = name
        self.full = health
        self.health = health
    
    def get_name(self):
        return self.name
    
    def get_health(self):
        return self.health
    
    def is_dead(self):
        return self.health == 0

class EvilAI(AI):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.clones = {self : True}
        self.crippled = False
    
    def clone(self):
        if self.health <= 0 or self.crippled:
            return None
        else:
            new = EvilAI(self.name, self.full)
            new.clones = self.clones
            new.clones[new] = True
            for ai in self.clones:
                ai.clones[new] = True
            return new
    
    def count_copies(self):
        count = 0
        for clone in self.clones:
            if self.clones[clone] == True:
                count += 1
        return count
    
    def is_dead(self):
        status = True
        for clone in self.clones:
            if self.clones[clone] == True:
                status = False
        return status
    
    def attack(self, target):
        if not self.health <= 0:
            target.health -= 1
        if target.health <= 0:
            target.health = 0
            if isinstance(target, EvilAI):
                target.clones[target] = False
                for clone in self.clones:
                    clone.clones[target] = False

class SuperAI(AI):
    def __init__(self, name, health):
        super().__init__(name, health)
    
    def attack(self, target):
        if not self.health <= 0:
            target.health -= 5
        if target.health <= 0:
            target.health = 0
            if isinstance(target, EvilAI):
                target.clones[target] = False
                for clone in target.clones:
                    clone.clones[target] = False
    
    def cripple(self, target):
        if not self.health <= 0:
            target.health -= 1
        if isinstance(target, EvilAI):
            target.crippled = True
        if target.health <= 0:
            target.health = 0
            if isinstance(target, EvilAI):
                target.clones[target] = False
                for clone in target.clones:
                    clone.clones[target] = False


# Tests
def test_q3():
    print("Testing Q3")
    jarvis = AI("Jarvis", 2)
    ultron = EvilAI("Ultron", 10)
    vision = SuperAI("Vision", 5)

    ultron.attack(jarvis)
    print("jarvis.get_health():", compare(jarvis.get_health(), 1))
    ultron.attack(jarvis)
    print("jarvis.is_dead():", compare(jarvis.is_dead(), True))

    u1 = ultron.clone()
    u2 = ultron.clone()
    u3 = ultron.clone()
    print("ultron.count_copies():", compare(ultron.count_copies(), 4))

    vision.attack(u1)
    vision.attack(u2)
    vision.attack(u1)
    print("u1.is_dead():", compare(u1.is_dead(), False))
    print("ultron.count_copies():", compare(ultron.count_copies(), 3))

    ultron.attack(vision)
    u1.attack(vision)
    u2.attack(vision)
    print("vision.get_health():", compare(vision.get_health(), 3))

    vision.attack(ultron)
    vision.attack(ultron)
    print("ultron.is_dead():", compare(ultron.is_dead(), False))

    vision.cripple(u2)
    u4 = u2.clone()
    vision.attack(u2)
    print("u2.get_health():", compare(u2.get_health(), 0))
    print("u3.count_copies():", compare(u3.count_copies(), 1))

# Uncomment to test question 3
test_q3()

