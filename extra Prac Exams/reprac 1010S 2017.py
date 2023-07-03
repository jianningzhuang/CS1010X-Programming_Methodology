#******************************************************
#*
#*  CS1010S Re-Practical Exam
#*  AY2016/2017, Semester 2
#*  Name: <fill in your name here>
#*
#*  This template is to be used if Coursemology fails.
#*  Otherwise, answers should be uploaded to Coursemology
#*  directly. 
#*
#******************************************************

#------------#
# Question 1 #
#------------#

def check_digit(digits, table):
    sum_dig = 0
    for digit in digits:
        sum_dig += int(digit)
    return table[sum_dig%len(table)]


nus_matric = {
    0: 'Y',
    1: 'X',
    2: 'W',
    3: 'U',
    4: 'R',
    5: 'N',
    6: 'M',
    7: 'L',
    8: 'J',
    9: 'H',
    10: 'E',
    11: 'A',
    12: 'B'
}
# Uncomment to test
#print(check_digit("0113093", nus_matric))
#print(check_digit("0129969", nus_matric))


def weighted_check_digit(digits, table, weights):
    sum_weighted = 0
    for i in range(len(digits)):
        sum_weighted += int(digits[i])*int(weights[i])
    return table[sum_weighted%len(table)]


sg_nric = dict(enumerate("JZIHGFEDCBA"))
sg_weights = "2765432"

# Uncomment to test
#print(weighted_check_digit("9702743", sg_nric, sg_weights))
#print(weighted_check_digit("9875133", sg_nric, sg_weights))


#------------#
# Question 2 #
#------------#

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


def oversub_avg(fname, year):
    data = read_csv(fname)[1:]
    result = {}
    for y, month, bidding, veh_class, quota, success, received, premium in data:
        if y == year:
            if veh_class not in result:
                result[veh_class] = []
            result[veh_class].append(float(received)/float(success))
    for vc in result:
        result[vc] = round(sum(result[vc])/len(result[vc]), 3)
    return result
        


# Uncomment to test
#print(oversub_avg("coe.csv", "2013"))
#print(oversub_avg("coe.csv", "2015"))


def most_oversub(fname, year):
    data = read_csv(fname)[1:]
    result = {}
    bids = {}
    for y, month, bidding, veh_class, quota, success, received, premium in data:
        if y == year:
            if veh_class not in result:
                result[veh_class] = 0
            if (month, bidding) not in bids:
                bids[(month, bidding)] = {}
            bids[(month, bidding)][veh_class] = float(received)/float(success)
    for bid in bids:
        veh = None
        highest = None
        for v_class in bids[bid]:
            if highest == None or bids[bid][v_class] > highest:
                highest = bids[bid][v_class]
                veh = v_class
        result[veh] += 1
    return result

# Uncomment to test
#print(most_oversub("coe.csv", "2013"))     
#print(most_oversub("coe.csv", "2015")) 



#------------#
# Question 3 #
#------------#

class Monster:

    def __init__(self, name, scariness):
        self.name = name
        self.scariness = scariness
        self.energy = 0
        self.location = "Scream Floor"

    def get_name(self):
        return self.name

    def get_energy(self):
        return self.energy

    def get_location(self):
        if self.location == "Scream Floor":
            return self.name + " is on the Scream Floor"
        else:
            return self.name + " is in " + self.location.name
        
    def enter(self, door):
        if self.location == door:
            return self.name + " has already entered " + door.name
        elif self.location == "Scream Floor":
            self.location = door
            door.monsters.append(self)
            if self not in door.visited:
                door.visited[self] = 1
            return self.name + " enters " + door.name
        else:
            return self.name + " is currently in " + self.location.name

    def scare(self):
        if self.location == "Scream Floor":
            return self.name + " has not entered any door"
        else:
            eff = 0
            for monster in self.location.monsters:
                eff += monster.scariness/self.location.visited[monster]
                self.location.visited[monster] += 1
            energy = eff - self.location.bravery
            self.location.bravery += len(self.location.monsters)
            if energy <= 0:
                m = self.location.get_monsters()
                n = self.location
                for monster in self.location.monsters:
                    monster.location = "Scream Floor"
                n.monsters = []
                return m + " failed to obtain energy from " + n.name
            else:
                m = self.location.get_monsters()
                n = self.location
                k = len(self.location.monsters)
                for monster in self.location.monsters:
                    monster.energy += energy/k
                    monster.location = "Scream Floor"
                n.monsters = []
                return m + " got " + str(energy) + " energy from " + n.name
            
        
        


class Door:

    def __init__(self, name, bravery):
        self.name = name
        self.bravery = bravery
        self.visited = {}
        self.monsters = []

    def get_bravery(self):
        return self.bravery

    def get_monsters(self):
        monsters = list(map(lambda x: x.name, self.monsters))
        monsters.sort()
        result = ", ".join(monsters)
        return result



## helper function. Do NOT modify. No need to paste on Coursemology
def leaderboard(*monsters):
    return "\n".join("{}: {}".format(m.get_name(),
                                     round(m.get_energy(), 2)) for m in
                     sorted(monsters, key=lambda x:float(x.get_energy()), reverse=True))

# Sample run test case
def test_q3():
    sully = Monster("Sully", 12)
    mike = Monster("Mike", 1)
    randall = Monster("Randall", 8)

    mary = Door("Mary's Room", 1)
    ted = Door("Ted's Room", 1)
    boo = Door("Boo's Room", 21)
        
    _=leaderboard(sully, mike, randall); print(_ == """Sully: 0
Mike: 0
Randall: 0""", '\tleaderboard(sully, mike, randall):\t', _)
    _=sully.get_energy(); print(_ == 0, '\tsully.get_energy():\t', _)
    _=sully.get_location(); print(_ == "Sully is on the Scream Floor", '\tsully.get_location():\t', _)
    _=sully.enter(mary); print(_ == "Sully enters Mary's Room", '\tsully.enter(mary):\t', _)
    _=sully.get_location(); print(_ == "Sully is in Mary's Room", '\tsully.get_location():\t', _)
    _=mary.get_monsters(); print(_ == "Sully", '\tmary.get_monsters():\t', _)
    _=sully.scare(); print(_ == "Sully got 11.0 energy from Mary's Room", '\tsully.scare():\t', _)
    _=leaderboard(sully, mike, randall); print(_ == """Sully: 11.0
Mike: 0
Randall: 0""", '\tleaderboard(sully, mike, randall):\t', _)
    _=mary.get_bravery(); print(_ == 2, '\tmary.get_bravery():\t', _)
    _=sully.get_location(); print(_ == "Sully is on the Scream Floor", '\tsully.get_location():\t', _)
    _=randall.scare(); print(_ == "Randall has not entered any door", '\trandall.scare():\t', _)
    _=randall.enter(mary); print(_ == "Randall enters Mary's Room", '\trandall.enter(mary):\t', _)
    _=randall.scare(); print(_ == "Randall got 6.0 energy from Mary's Room", '\trandall.scare():\t', _)
    _=sully.enter(mary); print(_ == "Sully enters Mary's Room", '\tsully.enter(mary):\t', _)
    _=sully.enter(ted); print(_ == "Sully is currently in Mary's Room", '\tsully.enter(ted):\t', _)
    _=mary.get_bravery(); print(_ == 3, '\tmary.get_bravery():\t', _)
    _=sully.scare(); print(_ == "Sully got 3.0 energy from Mary's Room", '\tsully.scare():\t', _)
    _=mary.get_bravery(); print(_ == 4, '\tmary.get_bravery():\t', _)
    _=sully.enter(mary); print(_ == "Sully enters Mary's Room", '\tsully.enter(mary):\t', _)
    _=sully.scare(); print(_ == "Sully failed to obtain energy from Mary's Room", '\tsully.scare():\t', _)
    _=randall.enter(mary); print(_ == "Randall enters Mary's Room", '\trandall.enter(mary):\t', _)
    _=randall.scare(); print(_ == "Randall failed to obtain energy from Mary's Room", '\trandall.scare():\t', _)
    _=mary.get_bravery(); print(_ == 6, '\tmary.get_bravery():\t', _)
    _=randall.get_location(); print(_ == "Randall is on the Scream Floor", '\trandall.get_location():\t', _)
    _=sully.enter(ted); print(_ == "Sully enters Ted's Room", '\tsully.enter(ted):\t', _)
    _=mike.enter(ted); print(_ == "Mike enters Ted's Room", '\tmike.enter(ted):\t', _)
    _=leaderboard(sully, mike, randall); print(_ == """Sully: 14.0
Randall: 6.0
Mike: 0""", '\tleaderboard(sully, mike, randall):\t', _)
    _=ted.get_monsters(); print(_ == "Mike, Sully", '\tted.get_monsters():\t', _)
    _=ted.get_bravery(); print(_ == 1, '\tted.get_bravery():\t', _)
    _=mike.scare(); print(_ == "Mike, Sully got 12.0 energy from Ted's Room", '\tmike.scare():\t', _)
    _=leaderboard(sully, mike, randall); print(_ == """Sully: 20.0
Mike: 6.0
Randall: 6.0""", '\tleaderboard(sully, mike, randall):\t', _)
    _=ted.get_bravery(); print(_ == 3, '\tted.get_bravery():\t', _)
    _=sully.enter(ted); print(_ == "Sully enters Ted's Room", '\tsully.enter(ted):\t', _)
    _=mike.enter(ted); print(_ == "Mike enters Ted's Room", '\tmike.enter(ted):\t', _)
    _=randall.enter(ted); print(_ == "Randall enters Ted's Room", '\trandall.enter(ted):\t', _)
    _=randall.scare(); print(_ == "Mike, Randall, Sully got 11.5 energy from Ted's Room", '\trandall.scare():\t', _)
    _=ted.get_bravery(); print(_ == 6, '\tted.get_bravery():\t', _)
    _=sully.enter(boo); print(_ == "Sully enters Boo's Room", '\tsully.enter(boo):\t', _)
    _=mike.enter(boo); print(_ == "Mike enters Boo's Room", '\tmike.enter(boo):\t', _)
    _=randall.enter(boo); print(_ == "Randall enters Boo's Room", '\trandall.enter(boo):\t', _)
    _=sully.scare(); print(_ == "Mike, Randall, Sully failed to obtain energy from Boo's Room", '\tsully.scare():\t', _)
    _=mike.get_energy(); print(_ == 9.833333333333334, '\tmike.get_energy():\t', _)
    _=leaderboard(sully, mike, randall); print(_ == """Sully: 23.83
Mike: 9.83
Randall: 9.83""", '\tleaderboard(sully, mike, randall):\t', _)

# Uncomment to test
test_q3()
