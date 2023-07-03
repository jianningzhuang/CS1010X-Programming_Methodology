##############
# Question 1 #
##############

def floyd_row(n):
    result = ()
    start = ((n-1)*n//2) + 1
    for i in range(start, start + n):
        result += (i, )
    return result


def floyd_sum(n):
    return (floyd_row(n)[-1])*(floyd_row(n)[-1] + 1)//2


# Tests
def test_q1a():
    print(floyd_row(1))
    print(floyd_row(2))
    print(floyd_row(5))


def test_q1b():
    print(floyd_sum(1))
    print(floyd_sum(2))
    print(floyd_sum(5))


# Uncomment to test
#test_q1a()
#test_q1b()



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


### Your answer here.
# Q2A
def regional_sales(filename, platform, year):
    data = read_csv(filename)[1:]
    result = {"NA" : 0, "EU" : 0, "JP" : 0, "Other" : 0, "Total" : 0}
    for name, platform_, year_, genre, published, na, eu, jp, other, total in data:
        if platform_ == platform and year_ != "N/A":
            if int(year_) == year:
                if na != "N/A":
                    result["NA"] += float(na)
                if na != "N/A":
                    result["EU"] += float(eu)
                if na != "N/A":
                    result["JP"] += float(jp)
                if na != "N/A":
                    result["Other"] += float(other)
                if na != "N/A":
                    result["Total"] += float(total)
    sales = ()
    sales += (round(result["NA"], 2),)
    sales += (round(result["EU"], 2),)
    sales += (round(result["JP"], 2),)
    sales += (round(result["Other"], 2),)
    sales += (round(result["Total"], 2),)
    return sales

# Q2B      
def trending_genre(filename, platform):
    data = read_csv(filename)[1:]
    result = {}
    for name, platform_, year, genre, published, na, eu, jp, other, total in data:
        if platform_ == platform and year != "N/A" and genre != "N/A":
            if int(year) not in result:
                result[int(year)] = {}
                result[int(year)][genre] = float(total)
            else:
                if genre not in result[int(year)]:
                    result[int(year)][genre] = float(total)
                else:
                    result[int(year)][genre] += float(total)
    final = {}
    for year_ in result:
        if year_ - 1 in result:
            highest = None
            best = None
            for genre in result[year_]:
                if genre in result[year_-1]:
                    increase = round(((result[year_][genre] - result[year_-1][genre])/result[year_-1][genre])*100, 2)
                    if highest == None or increase >= highest:
                        if increase == highest:
                            if genre < best:
                                highest = increase
                                best = genre
                        else:
                            highest = increase
                            best = genre
            final[year_] = best
    return final
                    
                        
            
            
    



# Tests
def test_q2a():
    print(regional_sales("vgsales.csv", "X360", 2016))
    print(regional_sales("vgsales.csv", "3DS", 2012))


def test_q2b():
    print(trending_genre("vgsales.csv", "PS3") == \
        {2013: 'Misc', 2014: 'Misc', 2015: 'Simulation', 2016: 'Role-Playing'})
    print(trending_genre("vgsales.csv", "PC") == \
        {2013: 'Misc', 2014: 'Simulation', 2015: 'Strategy', 2016: 'Adventure'})


#test_q2a()
#test_q2b()

    

##############
# Question 3 #
##############

class Stone:

    def __init__(self, name, *powers):
        self.name = name
        self.powers = list(powers)
        self.status = "okay"
        self.artefact = None

    def imbue(self, power):
        if self.status == "destroyed":
            return self.name + " already destroyed"
        if power in self.powers:
            return self.name + " already imbued with the power " + power
        else:
            self.powers.append(power)
            return self.name + " is now imbued with the power " + power
        
    def disarm(self, power):
        if self.status == "destroyed":
            return self.name + " already destroyed"
        if power not in self.powers:
            return self.name + " is not imbued with the power " + power
        else:
            self.powers.remove(power)
            return self.name + " is no longer imbued with the power " + power

    def destroy(self):
        if self.status == "destroyed":
            return self.name + " already destroyed"
        else:
            self.status = "destroyed"
            if self.artefact != None:
                self.artefact.remove_stone(self)
            return self.name + " is now destroyed"

    def list_powers(self):
        if self.status == "destroyed":
            return ()
        return tuple(self.powers)
        
        
class Artefact:

    def __init__(self, name, *stones):
        self.name = name
        self.stones = list(stones)
        for stone in self.stones:
            stone.artefact = self
        self.set = []

    def add_stone(self, stone):
        if stone.status == "destroyed":
            return stone.name + " is already destroyed"
        if stone in self.stones:
            return self.name + " already has " + stone.name
        if stone.artefact != None and stone.artefact != self:
            return stone.name + " is already part of " + stone.artefact.name
        else:
            self.stones.append(stone)
            stone.artefact = self
            return stone.name + " is added to " + self.name

    def remove_stone(self, stone):
        if stone not in self.stones:
            return self.name + " does not contain " + stone.name
        else:
            self.stones.remove(stone)
            stone.artefact = None
            return stone.name + " is removed from " + self.name

    def combine(self, other):
        if self == other:
            return "Cannot combine " + self.name + " with itself"
        if other in self.set:
            return self.name + " is already combined with " + other.name
        else:
            copy_self = self.set.copy()
            copy_other = other.set.copy()
            self.set.append(other)
            self.set.extend(copy_other)
            self.stones.extend(other.stones)
            for elem in self.set:
                elem.set.append(other)
                elem.set.extend(copy_other)
                elem.stones.extend(other.stones)
            other.set.append(self)
            other.set.extend(copy_self)
            other.stones.extend(self.stones)
            for ele in other.set:
                ele.set.append(self)
                ele.set.extend(copy_self)
                ele.stones.extend(self.stones)
            return self.name + " combines with " + other.name

    def invoke(self):
        result  = ()
        for stone in self.stones:
            for power in stone.list_powers():
                if power not in result:
                    result += (power, )
        return result
                

# Test cases

def test_q3():
    power_stone   = Stone("Power Stone", "Attack", "Defense")
    mind_stone    = Stone("Mind Stone", "Brainwash")
    time_stone    = Stone("Time Stone")
    reality_stone = Stone("Reality Stone", "Illusion")

    vision          = Artefact("Vision", mind_stone)
    gauntlet        = Artefact("Gauntlet", power_stone)
    eye_of_agamotto = Artefact("Eye of Agamoto")

    mind_stone_remade = Stone("Mind Stone", "Brainwash", "Illusion")

    _=power_stone.imbue("Attack"); print(_ == "Power Stone already imbued with the power Attack", "\tpower_stone.imbue('Attack'):\t", _)
    _=power_stone.imbue("Strength"); print(_ == "Power Stone is now imbued with the power Strength", "\tpower_stone.imbue('Strength'):\t", _)
    _=power_stone.list_powers(); print(tuple(sorted(_)) == ('Attack', 'Defense', 'Strength'), "\tpower_stone.list_powers():\t", _)
    _=time_stone.imbue("Repeat"); print(_ == "Time Stone is now imbued with the power Repeat", "\ttime_stone.imbue('Repeat'):\t", _)
    _=time_stone.imbue("Undo"); print(_ == "Time Stone is now imbued with the power Undo", "\ttime_stone.imbue('Undo'):\t", _)
    _=vision.add_stone(mind_stone); print(_ == "Vision already has Mind Stone", "\tvision.add_stone(mind_stone):\t", _)
    _=vision.remove_stone(power_stone); print(_ == "Vision does not contain Power Stone", "\tvision.remove_stone(power_stone):\t", _)
    _=vision.remove_stone(mind_stone); print(_ == "Mind Stone is removed from Vision", "\tvision.remove_stone(mind_stone):\t", _)
    _=vision.add_stone(mind_stone); print(_ == "Mind Stone is added to Vision", "\tvision.add_stone(mind_stone):\t", _)
    _=vision.invoke(); print(tuple(sorted(_)) == ('Brainwash',), "\tvision.invoke():\t", _)
    _=vision.add_stone(power_stone); print(_ == "Power Stone is already part of Gauntlet", "\tvision.add_stone(power_stone):\t", _)
    _=mind_stone.disarm("AI"); print(_ == "Mind Stone is not imbued with the power AI", "\tmind_stone.disarm('AI'):\t", _)
    _=mind_stone.destroy(); print(_ == "Mind Stone is now destroyed", "\tmind_stone.destroy():\t", _)
    _=mind_stone.disarm("Brainwash"); print(_ == "Mind Stone already destroyed", "\tmind_stone.disarm('Brainwash'):\t", _)
    _=vision.remove_stone(mind_stone); print(_ == "Vision does not contain Mind Stone", "\tvision.remove_stone(mind_stone):\t", _)
    _=eye_of_agamotto.add_stone(time_stone); print(_ == "Time Stone is added to Eye of Agamoto", "\teye_of_agamotto.add_stone(time_stone):\t", _)
    _=vision.combine(eye_of_agamotto); print(_ == "Vision combines with Eye of Agamoto", "\tvision.combine(eye_of_agamotto):\t", _)
    _=eye_of_agamotto.combine(vision); print(_ == "Eye of Agamoto is already combined with Vision", "\teye_of_agamotto.combine(vision):\t", _)
    _=gauntlet.add_stone(mind_stone); print(_ == "Mind Stone is already destroyed", "\tgauntlet.add_stone(mind_stone):\t", _)
    _=gauntlet.add_stone(mind_stone_remade); print(_ == "Mind Stone is added to Gauntlet", "\tgauntlet.add_stone(mind_stone_remade):\t", _)
    _=gauntlet.invoke(); print(tuple(sorted(_)) == ('Attack', 'Brainwash', 'Defense', 'Illusion', 'Strength'), "\tgauntlet.invoke():\t", _)
    _=gauntlet.add_stone(reality_stone); print(_ == "Reality Stone is added to Gauntlet", "\tgauntlet.add_stone(reality_stone):\t", _)
    _=gauntlet.invoke(); print(tuple(sorted(_)) == ('Attack', 'Brainwash', 'Defense', 'Illusion', 'Strength'), "\tgauntlet.invoke():\t", _)
    _=gauntlet.combine(eye_of_agamotto); print(_ == "Gauntlet combines with Eye of Agamoto", "\tgauntlet.combine(eye_of_agamotto):\t", _)
    _=gauntlet.combine(vision); print(_ == "Gauntlet is already combined with Vision", "\tgauntlet.combine(vision):\t", _)
    _=gauntlet.invoke(); print(tuple(sorted(_)) == ('Attack', 'Brainwash', 'Defense', 'Illusion', 'Repeat', 'Strength', 'Undo'), "\tgauntlet.invoke():\t", _)



# Uncomment to test question 3
test_q3()    
