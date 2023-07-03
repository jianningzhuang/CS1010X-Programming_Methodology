#******************************************************
#*
#*  CS1010S Practical Exam
#*  AY2014/2015, Semester 1
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

def count_digits(n):
    result = {}
    for digit in str(n):
        if int(digit) not in result:
            result[int(digit)] = 0
        result[int(digit)] += 1
    return result

def most_common_digit(n):
    freq = count_digits(n)
    most = None
    for digit in freq:
        if most == None or freq[digit] > most:
            most = freq[digit]
    result = []
    for d in freq:
        if freq[d] == most:
            result.append(d)
    result.sort()
    return result

### Your answer here.

# Tests

def test_q1a():
    print("Testing Q1A")
    print(count_digits(1212121) == {1:4, 2:3})
    print(count_digits(1212333) == {1:2, 2:2, 3:3 })
    print(count_digits(12345) == {1:1, 2:1, 3:1, 4:1, 5:1 })
    print("===========================================")

def test_q1b():
    # Keep in mind that your answer might be slightly different
    # because of the ordering, but might still be correct.
    print("Testing Q1B")
    print(most_common_digit(1212121) == [1])
    print(most_common_digit(12345) == [1, 2, 3, 4, 5])
    print(most_common_digit(12586269025) == [2])
    print(most_common_digit(1548008755920) == [0, 5])
    print(most_common_digit(190392490709135) == [9])
    print("===========================================")

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

    with open(csvfilename) as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            rows.append(row)
    return rows

### Your answer here.

def count_high_psi(filename, n):
    data = read_csv(filename)[1:]
    result = {}
    for year, month, day, time, north, south, east, west, central in data:
        if (year, month, day) not in result:
            result[(year, month, day)] = {}
        if time not in result[(year, month, day)]:
            result[(year, month, day)][time] = 0
        total = int(north) + int(south) + int(east) + int(west) + int(central)
        result[(year, month, day)][time] += total/5
    count = 0
    for d in result:
        t = 0
        for h in result[d]:
            t += result[d][h]
        ave = t/len(result[d])
        if ave > n:
            count += 1
    return count
            

def avg_psi(filename):
    data = read_csv(filename)[1:]
    result = {"North" : {}, "South" : {}, "East" : {}, "West" : {}, "Central" : {}}
    for year, month, day, time, north, south, east, west, central in data:
        for a in result:
            if (year, month, day) not in result[a]:
                result[a][(year, month, day)] = []
        result["North"][(year, month, day)].append(int(north))
        result["South"][(year, month, day)].append(int(south))
        result["East"][(year, month, day)].append(int(east))
        result["West"][(year, month, day)].append(int(west))
        result["Central"][(year, month, day)].append(int(central))
    for a in result:
        t = 0
        for d in result[a]:
            result[a][d] = sum(result[a][d])/len(result[a][d])
            t += result[a][d]
        result[a] = round(t/len(result[a]), 3)
    return result

# Tests

def test_q2():
    print(count_high_psi('psi-2013.csv', 50)==19)
    print(count_high_psi('psi-2013.csv', 100)==6)
    print(avg_psi('psi-2013.csv')=={'North': 31.954, 'South': 28.892, 'East': 27.418, 'West': 31.230, 'Central': 27.747})

# Uncomment to test question 2
#test_q2()

###
### Question 3
###

class PowerSuit:

    def __init__(self, name, mounting_points):
        self.name = name
        self.mounts = {}
        for point in mounting_points:
            self.mounts[point] = None

    def mount(self, equipment, *mounting_points):
        for point in mounting_points:
            if point not in self.mounts:
                return "No such mount point"
        if not isinstance(equipment, Equipment):
            return "Not mountable"
        if equipment.suit != None:
            return "Already mounted on " + equipment.suit.name
        for point in mounting_points:
            if self.mounts[point] != None:
                return "Mounting point occupied"
        if len(mounting_points) != equipment.space:
            return "Wrong number of mount points"
        else:
            equipment.suit = self
            for point in mounting_points:
                self.mounts[point] = equipment
            return equipment.name + " mounted on " + self.name

    def remove(self, socket):
        if socket not in self.mounts:
            return "No such mount point"
        if self.mounts[socket] == None:
            return "Nothing to remove"
        else:
            e = self.mounts[socket]
            e.suit = None
            self.mounts[socket] = None
            return e.name + " removed"

    def activate(self, socket):
        if socket not in self.mounts:
            return "No such mount point"
        if self.mounts[socket] == None:
            return "Nothing to activate"
        else:
            e = self.mounts[socket]
            return e.name + " activated!"

    def sockets(self):
        result = {}
        for p in self.mounts:
            if self.mounts[p] == None:
                result[p] = "Empty"
            else:
                result[p] = self.mounts[p].name
        return result
                
                
        

class Equipment:

    def __init__(self, name, space = 1):
        self.name = name
        self.space = space
        self.suit = None



def test_q3():
    # Ironman Mark II Armour
    mark2 = PowerSuit("Mark 2", ["Left Arm", "Right Arm", "Boots"])
    repulsor = Equipment("Repulsor Beam")
    
    print("mark2.mount(Equipment(\"Flight Jet\",\"Boots\")):"+mark2.mount(Equipment("Flight Jet"),"Boots"))
    print("mark2.mount(repulsor, \"Shoulder\"):"+mark2.mount(repulsor,"Shoulder"))
    print("mark2.mount(repulsor, \"Left Arm\"):"+mark2.mount(repulsor, "Left Arm"))
    print("mark2.mount(repulsor, \"Right Arm\"):"+mark2.mount(repulsor,"Right Arm"))
    print("mark2.mount(Equipment(\"Repulsor Beam\"), \"Right Arm\"):"+mark2.mount(Equipment("Repulsor Beam"),"Right Arm"))
    print("mark2.sockets():"+str(mark2.sockets()))
    print("mark2.activate(\"Left Arm\"):"+mark2.activate("Left Arm"))
    print("mark2.remove(\"Left Arm\"):"+mark2.remove("Left Arm"))
    print("mark2.activate(\"Left Arm\"):"+mark2.activate("Left Arm"))
    print("mark2.remove(\"Left Arm\"):"+mark2.remove("Left Arm"))
    print("mark2.mount(repulsor, \"Left Arm\"):"+mark2.mount(repulsor, "Left Arm"))
    
    # Ironman Armour Model 11
    mark11 = PowerSuit("Model 11", ["Left Shoulder", "Right Shoulder", "Left Arm", "Right Arm", "Boots"])
    print("mark11.mount(Equipment(\"Flight Jet\"),\"Boots\"):"+mark11.mount(Equipment("Flight Jet"),"Boots"))
    print("mark11.mount(repulsor,\"Left Shoulder\"):"+mark11.mount(repulsor,"Left Shoulder"))
    print("mark11.mount(Equipment(\"Chain Gun\"),\"Left Shoulder\"):"+mark11.mount(Equipment("Chain Gun"),"Left Shoulder"))
    print("mark11.sockets():"+str(mark11.sockets()))
    flamethrower = Equipment("Flamethrower")
    print("mark11.mount(flamethrower,\"Right Arm\"):"+mark11.mount(flamethrower, "Right Arm"))
    print("mark11.mount(Equipment(\"Repulsor Beam\", \"Left Arm\")):"+mark11.mount(Equipment("Repulsor Beam"),"Left Arm"))
    print("mark11.sockets():"+str(mark11.sockets()))
    print("mark11.mount(flamethrower,\"Right Arm\"):"+mark11.mount(flamethrower,"Right Arm"))
    print("mark11.activate(\"Boots\"):"+mark11.activate("Boots"))
    print("mark11.activate(\"Right Shoulder\"):"+mark11.activate("Right Shoulder"))
    launcher = Equipment("Rocket Lancher",2)
    print("mark11.mount(launcher, \"Right Shoulder\"):"+mark11.mount(launcher, "Right Shoulder"))
    print("mark11.activate(\"Right Shoulder\"):"+mark11.activate("Right Shoulder"))
    print("mark11.remove(\"Left Shoulder\"):"+mark11.remove("Left Shoulder"))
    print("mark11.mount(launcher, \"Left Shoulder\", \"Right Shoulder\"):"+mark11.mount(launcher, "Left Shoulder", "Right Shoulder"))
    print("mark11.activate(\"Right Shoulder\"):"+mark11.activate("Right Shoulder"))
    print("mark11.sockets():"+str(mark11.sockets()))

# Uncomment to test question 3
#test_q3()

###
### Question 4
###

def binary_rep(n, digits):
    result = ""
    while n > 0:
        result = str(n%2) + result
        n = n//2
    for i in range(digits - len(result)):
        result = "0" + result
    return result


def gen_powerset(lst):
    powerset = []
    for i in range(2**len(lst)):
        binary = binary_rep(i, len(lst))
        subset = []
        for j in range(len(lst)):
            if binary[j] == "1":
                subset.append(lst[j])
        powerset.append(subset)
    return powerset

def staircases(n):
    powerset = gen_powerset(list(range(1, n)))
    result = []
    for elem in powerset:
        if len(elem) > 1 and sum(elem) == n:
            result.append(tuple(elem))
    return result
            


def test_q4a():
    print("staircases(2) : "+str(staircases(2)))
    print("staircases(3) : "+str(staircases(3)))
    print("staircases(4) : "+str(staircases(4)))
    print("staircases(5) : "+str(staircases(5)))
    print("staircases(6) : "+str(staircases(6)))
    print("staircases(7) : "+str(staircases(7)))
    print("staircases(8) : "+str(staircases(8)))

def test_q4b():
    print("pyramids(2) : "+str(pyramids(2)))
    print("pyramids(3) : "+str(pyramids(3)))
    print("pyramids(4) : "+str(pyramids(4)))
    print("pyramids(5) : "+str(pyramids(5)))
    print("pyramids(6) : "+str(pyramids(6)))
    print("pyramids(7) : "+str(pyramids(7)))
    print("pyramids(8) : "+str(pyramids(8)))

# Uncomment to test question 4
test_q4a()
# test_q4b()
