#******************************************************
#*
#*  CS1010S Make Up Practical Exam
#*  AY2014/2015, Semester 2
#*  Name: <fill in your name here>
#*
#*
#*  This template is to be used if Coursemology fails.
#*  Otherwise, answers should be uploaded to Coursemology
#*  directly. 
#*
#******************************************************

###
### Question 1
###

### Your answer here.

def are_anagrams(w1, w2):
    if len(w1) != len(w2):
        return False
    else:
        lst1 = []
        lst2 = []
        for i in range(len(w1)):
            lst1.append(w1[i])
            lst2.append(w2[i])
        lst1.sort()
        lst2.sort()
        return lst1 == lst2

def has_anagrams(lst):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if are_anagrams(lst[i], lst[j]):
                return True
    return False

def find_anagrams(lst):
    anagrams = {}
    for elem in lst:
        found = False
        for a in anagrams:
            if are_anagrams(a, elem):
                anagrams[a].append(elem)
                found = True
        if found == False:
            anagrams[elem] = []
    result = []
    for a in anagrams:
        if len(anagrams[a]) >= 1:
            result.append([a] + anagrams[a])
    return result
            
        


# Tests
def test_q1a():
    print(are_anagrams('dictionary', 'indicatory'))
    print(are_anagrams('listen', 'silent'))
    print(are_anagrams('test', 'exam'))
    print(are_anagrams('melon', 'watermelon'))

def test_q1b():
    print(has_anagrams(['apple', 'banana', 'pear', 'reap']))
    print(has_anagrams(['apple', 'banana', 'pear', 'papaya']))

def test_q1c():
    print(find_anagrams(['actress', 'grudge', 'recasts', 'rugged',
                         'casters', 'apple', 'pear', 'reap']))
    print(find_anagrams(['these', 'aren\'t', 'the', 'anagrams',
                         'you\'re', 'looking', 'for']))

    
# Uncomment to test question 1
#test_q1a()
#test_q1b()
#test_q1c()


###
### Question 2
###

### Your answer here.

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

def find_increase(filename, town):
    data = read_csv(filename)[1:]
    prices = {"3room": [], "4room": [], "5room": [], "exec": []}
    for year, quarter, t, three, four, five, exe in data:
        if t == town:
            if three.isdigit():
                prices["3room"].append((int(year), int(three)))
            if four.isdigit():
                prices["4room"].append((int(year), int(four)))
            if five.isdigit():
                prices["5room"].append((int(year), int(five)))
            if exe.isdigit():
                prices["exec"].append((int(year), int(exe)))
    for r in prices:
        prices[r].sort(key = lambda x: x[0])
        difference = None
        for i in range(len(prices[r]) - 1):
            for j in range(i + 1, len(prices[r])):
                if difference == None or (prices[r][j][1] - prices[r][i][1]) > difference:
                    difference = (prices[r][j][1] - prices[r][i][1])
        prices[r] = difference
    return prices
            
            
def cheapest_town(filename, y):
    data = read_csv(filename)[1:]
    prices = {"3room": {}, "4room": {}, "5room": {}, "exec": {}}
    for year, quarter, t, three, four, five, exe in data:
        if int(year) == y:
            if three.isdigit():
                if t not in prices["3room"]:
                    prices["3room"][t] = []
                prices["3room"][t].append(int(three))
            if four.isdigit():
                if t not in prices["4room"]:
                    prices["4room"][t] = []
                prices["4room"][t].append(int(four))
            if five.isdigit():
                if t not in prices["5room"]:
                    prices["5room"][t] = []
                prices["5room"][t].append(int(five))
            if exe.isdigit():
                if t not in prices["exec"]:
                    prices["exec"][t] = []
                prices["exec"][t].append(int(exe))
    for r in prices:
        lowest = None
        cheapest = None
        for town in prices[r]:
            if cheapest == None or (sum(prices[r][town])/len(prices[r][town])) < cheapest:
                cheapest = (sum(prices[r][town])/len(prices[r][town]))
                lowest = town
        prices[r] = (lowest, cheapest)
    return prices
            
            
    
        
    


# Tests
def test_q2a():
    print(find_increase('hdb-resale-prices.csv', 'Ang Mo Kio'))
    print(find_increase('hdb-resale-prices.csv', 'Jurong East'))

def test_q2b():
    print(cheapest_town('hdb-resale-prices.csv', 2011))
    print(cheapest_town('hdb-resale-prices.csv', 2013))


# Uncomment to test question 2
#test_q2a()
#test_q2b()

###
### Question 3
###

### Your answer here.

class Trainer:

    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        self.dragons = {}
        self.trained = []
        self.mounted = None

    def train(self, dragon):
        if dragon not in self.dragons:
            self.dragons[dragon] = 0
        if dragon in self.trained:
            return dragon.name + " has already been trained"
        if (self.skill + self.dragons[dragon]) >= dragon.level:
            self.trained.append(dragon)
            dragon.trainers.append(self)
            return self.name + " successfully trained " + dragon.name
        else:
            self.dragons[dragon] += 1
            return self.name + " failed to train " + dragon.name

    def trained_dragons(self):
        result = ()
        for dragon in self.trained:
            result += (dragon.name, )
        return result

    def mount(self, dragon):
        if self.mounted != None:
            return self.name + " is currently mounted on " + self.mounted.name
        if dragon.trainer != None:
            return dragon.trainer.name + " is currently mounted on " + dragon.name
        if dragon not in self.trained:
            return self.name + " has not yet trained " + dragon.name
        else:
            self.mounted = dragon
            dragon.trainer = self
            return self.name + " mounts " + dragon.name

    def dismount(self):
        if self.mounted == None:
            return self.name + " is not mounted"
        else:
            dragon = self.mounted
            dragon.trainer = None
            self.mounted = None
            return self.name + " dismounts from " + dragon.name
        

class Dragon:

    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.trainer = None
        self.trainers = []

    def get_trainers(self):
        result = ()
        for t in self.trainers:
            result += (t.name ,)
        return result
            

    def fly(self):
        if self.trainer == None:
            return self.name + " does not have a rider"
        else:
            return self.name + " flies around with " + self.trainer.name


# Tests
def test_q3():
        toothless = Dragon("Toothless", 7)
        meatlug = Dragon("Meatlug", 1)
        stormfly = Dragon("Stormfly", 5)
        
        hiccup = Trainer("Hiccup", 4)
        astrid = Trainer("Astrid", 5)
        
        print(astrid.train(stormfly) == 'Astrid successfully trained Stormfly')
        print(astrid.mount(stormfly) == 'Astrid mounts Stormfly')
        print(stormfly.fly() == 'Stormfly flies around with Astrid')

        print(meatlug.fly() == 'Meatlug does not have a rider')
        print(hiccup.mount(meatlug) == 'Hiccup has not yet trained Meatlug')
        print(hiccup.train(meatlug) == 'Hiccup successfully trained Meatlug')
        print(hiccup.train(meatlug) == 'Meatlug has already been trained')
        print(hiccup.mount(meatlug) == 'Hiccup mounts Meatlug')
        print(meatlug.fly() == 'Meatlug flies around with Hiccup')
                      
        print(hiccup.mount(stormfly) == 'Hiccup is currently mounted on Meatlug')
        print(hiccup.dismount() == 'Hiccup dismounts from Meatlug')
        print(hiccup.mount(stormfly) == 'Astrid is currently mounted on Stormfly')
        print(astrid.dismount() == 'Astrid dismounts from Stormfly')
        print(hiccup.mount(stormfly) == 'Hiccup has not yet trained Stormfly')

        print(astrid.trained_dragons() == ('Stormfly',))
        print(hiccup.trained_dragons() == ('Meatlug',))
        print(stormfly.get_trainers() == ('Astrid',))
        print(hiccup.train(stormfly) == 'Hiccup failed to train Stormfly')
        print(hiccup.train(stormfly) == 'Hiccup successfully trained Stormfly')
        print(sorted(stormfly.get_trainers()) == sorted(('Astrid', 'Hiccup')))

        print(hiccup.train(toothless) == 'Hiccup failed to train Toothless')
        print(hiccup.train(toothless) == 'Hiccup failed to train Toothless')
        print(hiccup.train(toothless) == 'Hiccup failed to train Toothless')
        print(hiccup.train(toothless) == 'Hiccup successfully trained Toothless')
        print(hiccup.mount(toothless) == 'Hiccup mounts Toothless')
        print(toothless.fly() == 'Toothless flies around with Hiccup')
        print(sorted(hiccup.trained_dragons()) == sorted(('Meatlug', 'Stormfly', 'Toothless')))

# Uncomment to test question 3
#test_q3()

###
### Question 4
###

### Your answer here.

def bomb_blast(n, m, bombs, walls, start):
    matrix = []
    for i in range(n):
        matrix.append([1]*m)
    for i in range(n):
        for j in range(m):
            if (i, j) in bombs:
                matrix[i][j] = [0, "B"]
            elif (i, j) in walls:
                matrix[i][j] = [0, "W"]
            else:
                matrix[i][j] = [1, "G"]
    def is_wall(row,col):
        if row >= 0 and row < n and \
           col >= 0 and col < m and \
           matrix[row][col][1] == 'W':
            return True
        return False

    def is_bomb(row,col):
        if row >= 0 and row < n and \
           col >= 0 and col < m and \
           matrix[row][col][1] == 'B':
            return True
        return False

    def is_normal_cell(row,col):
        if row >= 0 and row < n and \
           col >= 0 and col < m and \
           matrix[row][col][1] == 'G':
            return True
        return False

    def spread(row, col, direction):
        if direction == "B":
            spread(row-1, col, "U")
            spread(row+1, col, "D")
            spread(row, col+1, "R")
            spread(row, col-1, "L")
        else:
            if is_normal_cell(row, col):
                matrix[row][col][0] = 0
                if direction == 'U':
                    spread(row-1,col,direction)
                elif direction == 'D':
                    spread(row+1,col,direction)
                elif direction == 'L':
                    spread(row,col-1,direction)
                elif direction == 'R':
                    spread(row,col+1,direction)
            elif is_bomb(row, col):
                matrix[row][col][1] = "E"
                spread(row, col, "B")
    row, col = bombs[start][0], bombs[start][1]
    matrix[row][col][1] = "E"
    spread(row, col, "B")
    total = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j][1] == "G":
                total += matrix[i][j][0]
    print(total)
    return total
                
    


# Tests
def test_q4():
    print(bomb_blast(6, 5,
                     ((1, 1), (3, 1), (3, 3), (5, 4)),
                     ((3, 0), (4, 2), (1, 3)),
                     0) == 12)          
    print(bomb_blast(6, 7,
                     ((1, 1), (4, 1), (1, 5), (4, 5)),
                     ((2, 5),),
                     1) == 12)

# Uncomment to test question 4
test_q4()
