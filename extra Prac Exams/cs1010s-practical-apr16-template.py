#******************************************************
#*
#*  CS1010S Practical Exam
#*  AY2015/2016, Semester 2
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
def correct_pegs(code, guess):
    count = 0
    for i in range(len(code)):
        if code[i] == guess[i]:
            count += 1
    return count

def check_guess(code, guess):
    correct = correct_pegs(code, guess)
    count = 0
    for peg in guess:
        if peg in code:
            count += 1
            index = code.index(peg)
            code = code[:index] + code[index + 1:]
    return (correct, count - correct)
            
            


### test cases
def test1a():
    print(correct_pegs("rrbk", "rkbb"))
    print(correct_pegs("ydgkyd", "yyyddd"))
    print(correct_pegs("rbygkp", "bygkpr"))

def test1b():        
    print(check_guess("wwbbb", "bbwww"))
    print(check_guess("rrbbyy", "rcbyrg"))
    print(check_guess("rbyg", "bbbb"))




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
def highest_month(fname, start, stop):
    data = read_csv(fname)[1:]
    freq = {}
    for year, month, total, malays, chinese, indians, others in data:
        if start <= int(year) < stop:
            if year not in freq:
                freq[year] = {}
            freq[year][month] = int(total)
    for y in freq:
        highest = None
        result = None
        for m in freq[y]:
            if highest == None or freq[y][m] > highest:
                highest = freq[y][m]
                result = m
        freq[y] = result
    return freq
        


def compare_growth(fname, start, stop):
    data = read_csv(fname)[1:]
    freq = {"Indians" : {}, "Malays" : {}, "Chinese" : {}, "Others" : {}}
    for year, month, total, malays, chinese, indians, others in data:
        if start <= int(year) < stop:
            if int(year) not in freq["Malays"]:
                freq["Malays"][int(year)] = 0
            if int(year) not in freq["Chinese"]:
                freq["Chinese"][int(year)] = 0
            if int(year) not in freq["Indians"]:
                freq["Indians"][int(year)] = 0
            if int(year) not in freq["Others"]:
                freq["Others"][int(year)] = 0
            freq["Malays"][int(year)] += (int(malays))
            freq["Chinese"][int(year)] += (int(chinese))
            freq["Indians"][int(year)] += (int(indians))
            freq["Others"][int(year)] += (int(others))
    for race in freq:
        result = []
        s = start + 1
        while s < stop:
            result.append(round((freq[race][s]/freq[race][s - 1])*100 - 100, 2))
            s += 1
        freq[race] = result
    return freq

### test cases
def test2a():
    print(highest_month('births.csv', 2000, 2010))
    print(highest_month('births.csv', 1965, 1975))

def test2b():
    print(compare_growth('births.csv', 1975, 1980))
    print(compare_growth('births.csv', 1996, 2005))


###
### Question 3
###

### Your answer here.
class Jedi:

    def __init__(self, name, level, *powers):
        self.name = name
        self.level = level
        self.powers = {}
        if powers != ():
            for power in powers[0]:
                self.powers[power] = 0
        self.master = None
        self.disciples = []

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_powers(self):
        result = []
        for power, value in self.powers.items():
            result.append((power, value))
        return result

    def get_master(self):
        if self.master == None:
            return None
        else:
            return self.master.name

    def set_master(self, master):
        if master.level < self.level:
            return master.name + " has a lower level than " + self.name
        elif self.master == master:
            return master.name + " is already the master of " + self.name
        else:
            self.master = master
            master.disciples.append(self)
            return master.name + " takes " + self.name + " as a disciple"

    def get_disciples(self):
        result = []
        for d in self.disciples:
            result.append(d.name)
        return result

    def train(self):
        if len(self.powers) == 0:
            return self.name + " has not learnt any powers"
        else:
            lowest = None
            weakest = None
            for power in self.powers:
                if lowest == None or self.powers[power] < lowest:
                    lowest = self.powers[power]
                    weakest = power
            if lowest == self.level:
                self.level += 1
                if self.master != None and self.level > self.master.level:
                    temp_master = self.master
                    temp_grandmaster = self.master.master
                    temp_disciples = self.disciples
                    self.disciples = [temp_master]
                    temp_master.master = self
                    self.master = temp_grandmaster
                    if temp_grandmaster != None:
                        temp_grandmaster.disciples = [self]
                    temp_master.disciples = temp_disciples
                    if temp_disciples != []:
                        for d in temp_disciples:
                            d.master = temp_master
                    
                return self.name + " levels up to level " + str(self.level)
            else:
                self.powers[weakest] += 1
                return self.name + " trains " + weakest + " to level " + str(self.powers[weakest])

    def learn(self):
        if self.master == None:
            return self.name + " does not have a master"
        else:
            for power in self.master.powers:
                if power not in self.powers:
                    self.powers[power] = 0
                    return self.name + " learns " + power + " from " + self.master.name
            return self.name + " has nothing to learn from " + self.master.name
        


### Test cases
def test3():
    dooku = Jedi("Dooku", 3, ("push", "jump"))
    quigon = Jedi("Quigon", 2, ("mind trick",))
    obiwan = Jedi("Obiwan", 1)
    anakin = Jedi("Anakin", 1)
    luke = Jedi("Luke", 1)

    print("dooku.get_name():", dooku.get_name() == "Dooku", sep='\t')
    print("dooku.get_level():", dooku.get_level() == 3, sep='\t')
    print("dooku.get_powers():", dict(dooku.get_powers()) == {'jump':0, 'push':0}, sep='\t' )
    print("dooku.train():",'', dooku.train() in ("Dooku trains jump to level 1", "Dooku trains push to level 1"), sep='\t')
    print("dooku.get_powers():", dict(dooku.get_powers()) in ({'jump':1, 'push':0}, {'jump':0, 'push':1}), sep='\t')
    print("dooku.train():",'', dooku.train() in ("Dooku trains push to level 1", "Dooku trains jump to level 1"), sep='\t')
    print("dooku.get_powers():", dict(dooku.get_powers()) == {'jump':1, 'push':1}, sep='\t')
    print("dooku.set_master(quigon):", dooku.set_master(quigon) == "Quigon has a lower level than Dooku", sep='\t')
    print("quigon.set_master(dooku):", quigon.set_master(dooku) == "Dooku takes Quigon as a disciple", sep='\t')
    print("quigon.get_master():", quigon.get_master() == "Dooku", sep='\t')
    print("quigon.train():",'', quigon.train() == "Quigon trains mind trick to level 1", sep='\t')
    print("obiwan.train():",'', obiwan.train() == "Obiwan has not learnt any powers", sep='\t')
    print("obiwan.learn():",'', obiwan.learn() == "Obiwan does not have a master", sep='\t')
    print("obiwan.set_master(quigon):", obiwan.set_master(quigon) == "Quigon takes Obiwan as a disciple", sep='\t')
    print("obiwan.learn():",'', obiwan.learn() == "Obiwan learns mind trick from Quigon", sep='\t')
    print("obiwan.get_powers():", obiwan.get_powers() == [('mind trick', 0)], sep='\t' )
    print("obiwan.train():",'', obiwan.train() == "Obiwan trains mind trick to level 1" , sep='\t')
    print("obiwan.get_level():", obiwan.get_level() == 1, sep='\t' )
    print("obiwan.train():",'', obiwan.train() == "Obiwan levels up to level 2", sep='\t' )
    print("obiwan.get_level():", obiwan.get_level() == 2, sep='\t' )
    print("obiwan.get_master():", obiwan.get_master() == "Quigon" , sep='\t')
    print("quigon.get_disciples():", quigon.get_disciples() == ['Obiwan'] , sep='\t')
    print("obiwan.learn():",'', obiwan.learn() == "Obiwan has nothing to learn from Quigon" , sep='\t')
    print("anakin.set_master(obiwan):", anakin.set_master(obiwan) == "Obiwan takes Anakin as a disciple" , sep='\t')
    print("luke.set_master(obiwan):", luke.set_master(obiwan) == "Obiwan takes Luke as a disciple" , sep='\t')
    print("obiwan.get_disciples():", sorted(obiwan.get_disciples()) == ['Anakin', 'Luke'] , sep='\t')
    print("obiwan.train():",'', obiwan.train() == "Obiwan trains mind trick to level 2" , sep='\t')
    print("obiwan.train():",'', obiwan.train() == "Obiwan levels up to level 3" , sep='\t')
    print("obiwan.get_master():", obiwan.get_master() == "Dooku" , sep='\t')
    print("quigon.get_disciples():", sorted(quigon.get_disciples()) == ['Anakin', 'Luke'] , sep='\t')
    print("obiwan.get_disciples():", obiwan.get_disciples() == ['Quigon'] , sep='\t')
    print("dooku.get_disciples():", dooku.get_disciples() == ['Obiwan'] , sep='\t')
    print("obiwan.learn():",'', obiwan.learn() in ("Obiwan learns jump from Dooku", "Obiwan learns push from Dooku") , sep='\t')
    print("obiwan.get_powers():", dict(obiwan.get_powers()) in ({'jump':0, 'mind trick':2}, {'push':0, 'mind trick':2 }) , sep='\t')
    print("obiwan.train():",'', obiwan.train() in ("Obiwan trains jump to level 1", "Obiwan trains push to level 1") , sep='\t')

def print3():
    dooku = Jedi("Dooku", 3, ("push", "jump"))
    quigon = Jedi("Quigon", 2, ("mind trick",))
    obiwan = Jedi("Obiwan", 1)
    anakin = Jedi("Anakin", 1)
    luke = Jedi("Luke", 1)
    
    print("dooku.get_name():", dooku.get_name() )
    print("dooku.get_level():", dooku.get_level() )
    print("dooku.get_powers():", dooku.get_powers() )
    print("dooku.train():", dooku.train() )
    print("dooku.get_powers():", dooku.get_powers() )
    print("dooku.train():", dooku.train() )
    print("dooku.get_powers():", dooku.get_powers() )
    print("dooku.set_master(quigon):", dooku.set_master(quigon) )
    print("quigon.set_master(dooku):", quigon.set_master(dooku) )
    print("quigon.get_master():", quigon.get_master() )
    print("quigon.train():", quigon.train() )
    print("obiwan.train():", obiwan.train() )
    print("obiwan.learn():", obiwan.learn() )
    print("obiwan.set_master(quigon):", obiwan.set_master(quigon) )
    print("obiwan.learn():", obiwan.learn() )
    print("obiwan.get_powers():", obiwan.get_powers() )
    print("obiwan.train():", obiwan.train() )
    print("obiwan.get_level():", obiwan.get_level() )
    print("obiwan.train():", obiwan.train() )
    print("obiwan.get_level():", obiwan.get_level() )
    print("obiwan.get_master():", obiwan.get_master() )
    print("quigon.get_disciples():", quigon.get_disciples() )
    print("obiwan.learn():", obiwan.learn() )
    print("anakin.set_master(obiwan):", anakin.set_master(obiwan) )
    print("luke.set_master(obiwan):", luke.set_master(obiwan) )
    print("obiwan.get_disciples():", obiwan.get_disciples() )
    print("obiwan.train():", obiwan.train() )
    print("obiwan.train():", obiwan.train() )
    print("obiwan.get_master():", obiwan.get_master() )
    print("quigon.get_disciples():", quigon.get_disciples() )
    print("obiwan.get_disciples():", obiwan.get_disciples() )
    print("dooku.get_disciples():", dooku.get_disciples() )
    print("obiwan.learn():", obiwan.learn() )
    print("obiwan.get_powers():", obiwan.get_powers() )
    print("obiwan.train():", obiwan.train() )

# Uncomment to show sample execution
# print3()

# Uncomment to test sample execution
test3()
