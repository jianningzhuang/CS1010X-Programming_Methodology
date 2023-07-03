from calendar import isleap
#******************************************************
#*
#*  CS1010S Re-Practical Exam
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
def num_swaps(candies):
    max = None
    seen = []
    for candy in candies:
        if candy not in seen:
            seen.append(candy)
            if max == None or candies.count(candy) > max:
                max = candies.count(candy)
    return len(candies) - max

def num_trades(candies, rules):
    count = 0
    for candy in candies:
        cycle = 0
        while candy != "b":
            if cycle > len(rules) - 1:
                return float("inf")
            candy = rules[candy]
            count += 1
            cycle += 1
    return count
            


### test cases
def test1a():
    print(num_swaps("rbygo"))
    print(num_swaps("rrbbbg"))
    print(num_swaps("rrrbbbggy"))

def test1b():        
    print(num_trades('rrbbgg', {'r':'b', 'b':'y', 'y':'g', 'g':'o', 'o':'r'}))
    print(num_trades('rbbryy', {'r':'b', 'b':'r', 'y':'r'}))
    print(num_trades('rygop',
                     {'r':'b', 'b':'b', 'y':'b', 'g':'b', 'o':'b', 'p':'b'}))


def test_bonus():
    print(num_trades('rrbbgg', {'r':'b', 'b':'r', 'y':'g', 'g':'y'}))
    print(num_trades('rbbb', {'r':'y', 'b':'r', 'y':'g', 'g':'g'}))



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
def highest_rainfall(fname, start, stop):
    data = read_csv(fname)[1:]
    result = {}
    for year, month, total, max_day, num_day, mean_hour in data:
        if start <= int(year) < stop:
            if year not in result:
                result[year] = {}
            if month not in result[year]:
                result[year][month] = float(max_day)
    for y in result:
        highest = None
        month = None
        for m in result[y]:
            if highest == None or result[y][m] > highest:
                highest = result[y][m]
                month = m
        result[y] = (month, highest)
    return result
            
    


def rainy(fname, start, stop):
    data = read_csv(fname)[1:]
    result = {}
    for year, month, total, max_day, num_day, mean_hour in data:
        if start <= int(year) < stop:
            if int(year) not in result:
                result[int(year)] = 0
            result[int(year)] += int(num_day)
    for y in result:
        if isleap(y):
            result[y] = round(result[y]/3.66, 2)
        else:
            result[y] = round(result[y]/3.65, 2)
    return result
            

### test cases
def test2a():
    print(highest_rainfall('rainfall.csv', 2001, 2011))
    print(highest_rainfall('rainfall.csv', 1980, 1986))

def test2b():
    print(rainy('rainfall.csv', 1975, 1981))
    print(rainy('rainfall.csv', 2010, 2016))




###
### Question 3
###

### Your answer here.
class Sith:

    def __init__(self, name, *powers):
        self.name = "Darth " + name
        self.powers = {}
        for power in powers:
            self.powers[power] = 0
        self.master = None
        self.apprentice = None
        self.alive = True

    def get_name(self):
        return self.name

    def get_powers(self):
        result = ()
        for power, value in self.powers.items():
            result += ((power, value), )
        return result

    def get_master(self):
        if self.master == None:
            return None
        else:
            return self.master.name

    def get_apprentice(self):
        if self.apprentice == None:
            return None
        else:
            return self.apprentice.name

    def take_apprentice(self, apprentice):
        if apprentice.alive != True:
            return apprentice.name + " is already dead"
        elif self.apprentice != None or self.master != None:
            return self.name + " cannot take " + apprentice.name + " as an apprentice"
        else:
            self.apprentice = apprentice
            apprentice.master = self
            return self.name + " takes " + apprentice.name + " as an apprentice"

    def impart(self):
        if self.alive != True:
            return self.name + " is already dead"
        elif self.apprentice == None:
            return self.name + " does not have an apprentice"
        else:
            for power in self.powers:
                if power not in self.apprentice.powers:
                    self.apprentice.powers[power] = 0
                    return self.name + " imparts " + power + " to " + self.apprentice.name
            return self.name + " has nothing to impart to " + self.apprentice.name

    def train(self, power):
        if self.alive != True:
            return self.name + " is already dead"
        elif power not in self.powers:
            return self.name + " has does not know " + power
        else:
            self.powers[power] += 1
            return self.name + " trains " + power + " to level " + str(self.powers[power])

    def fight(self, opponent):
        if self.alive != True:
            return self.name + " is already dead"
        elif opponent.alive != True:
            return opponent.name + " is already dead"
        else:
            self_p = 0
            op_p = 0
            for power in self.powers:
                if power not in opponent.powers:
                    self_p += 1
                else:
                    if self.powers[power] > opponent.powers[power]:
                        self_p += 1
            for power in opponent.powers:
                if power not in self.powers:
                    op_p += 1
                else:
                    if self.powers[power] < opponent.powers[power]:
                        op_p += 1
            if self_p == op_p:
                return self.name + " and " + opponent.name + " are equally matched"
            elif self_p > op_p:
                opponent.alive = False
                if opponent.master != None:
                    opponent.master.apprentice = None
                elif opponent.apprentice != None:
                    opponent.apprentice.master = None
                opponent.master = None
                opponent.apprentice = None
                return self.name + " kills " + opponent.name + " in battle"
            else:
                self.alive = False
                if self.master != None:
                    self.master.apprentice = None
                elif self.apprentice != None:
                    self.apprentice.master = None
                self.master = None
                self.apprentice = None
                return opponent.name + " kills " + self.name + " in battle"
                
                    
            
            
            
        


### Test cases
def test3():
    plagueis = Sith("Plagueis", "lightning", "choke") 
    sidious = Sith("Sidious", "shadow")
    maul = Sith("Maul")
    tyranus = Sith("Tyranus")
    vader = Sith("Vader", "hate")

    print("plagueis.get_name():", plagueis.get_name() == 'Darth Plagueis' , sep="\t")
    print("plagueis.get_powers():", dict(plagueis.get_powers()) == {'choke':0, 'lightning':0} , sep="\t")
    print("plagueis.train('choke'):", plagueis.train("choke") == 'Darth Plagueis trains choke to level 1' , sep="\t")
    print("plagueis.train('lightning'):", plagueis.train("lightning") == 'Darth Plagueis trains lightning to level 1' , sep="\t")
    print("plagueis.take_apprentice(sidious):", plagueis.take_apprentice(sidious) == 'Darth Plagueis takes Darth Sidious as an apprentice' , sep="\t")
    print("plagueis.get_apprentice():", plagueis.get_apprentice() == 'Darth Sidious' , sep="\t")
    print("sidious.get_master():", sidious.get_master() == 'Darth Plagueis' , sep="\t")
    print("plagueis.impart():", plagueis.impart() in ['Darth Plagueis imparts choke to Darth Sidious', 'Darth Plagueis imparts lightning to Darth Sidious'] , sep="\t")
    print("sidious.train('lightning'):", sidious.train("lightning") in ['Darth Sidious has does not know lightning', 'Darth Sidious trains lightning to level 1'] , sep="\t")
    print("sidious.train('choke'):", sidious.train("choke") in ['Darth Sidious has does not know choke' ,'Darth Sidious trains choke to level 1'], sep="\t")
    print("sidious.get_powers():", dict(sidious.get_powers()) in [{'choke':1, 'shadow':0}, {'lightning':1, 'shadow':0}], sep="\t")
    print("sidious.take_apprentice(maul):", sidious.take_apprentice(maul) == 'Darth Sidious cannot take Darth Maul as an apprentice' , sep="\t")
    print("sidious.fight(plagueis):", sidious.fight(plagueis) == 'Darth Sidious and Darth Plagueis are equally matched' , sep="\t")
    print("plagueis.impart():", plagueis.impart() in ['Darth Plagueis imparts lightning to Darth Sidious', 'Darth Plagueis imparts choke to Darth Sidious'] , sep="\t")
    print("plagueis.impart():", plagueis.impart() == 'Darth Plagueis has nothing to impart to Darth Sidious' , sep="\t")
    print("sidious.get_powers():", dict(sidious.get_powers()) in [{'choke':1, 'shadow':0, 'lightning':0}, {'choke':0, 'shadow':0, 'lightning':1}], sep="\t")
    print("sidious.fight(plagueis):", sidious.fight(plagueis) == 'Darth Sidious and Darth Plagueis are equally matched' , sep="\t")
    print("sidious.train('shadow'):", sidious.train("shadow") == 'Darth Sidious trains shadow to level 1' , sep="\t")
    print("sidious.fight(plagueis):", sidious.fight(plagueis) == 'Darth Sidious and Darth Plagueis are equally matched' , sep="\t")
    print("sidious.train('lightning'):", sidious.train("lightning") in ['Darth Sidious trains lightning to level 1','Darth Sidious trains lightning to level 2'] , sep="\t")
    print("sidious.fight(plagueis):", sidious.fight(plagueis) == 'Darth Sidious kills Darth Plagueis in battle' , sep="\t")
    print("sidious.take_apprentice(maul):", sidious.take_apprentice(maul) == 'Darth Sidious takes Darth Maul as an apprentice' , sep="\t")
    print("plagueis.train('choke'):", plagueis.train("choke") == 'Darth Plagueis is already dead' , sep="\t")
    print("sidious.impart():", sidious.impart() in ['Darth Sidious imparts choke to Darth Maul', 'Darth Sidious imparts lightning to Darth Maul', 'Darth Sidious imparts shadow to Darth Maul'] , sep="\t")
    print("maul.train(maul.get_powers()[0][0]):", maul.train(maul.get_powers()[0][0]) in ['Darth Maul trains choke to level 1', 'Darth Maul trains lightning to level 1', 'Darth Maul trains shadow to level 1'] , sep="\t")
    print("maul.train(maul.get_powers()[0][0]):", maul.train(maul.get_powers()[0][0]) in ['Darth Maul trains choke to level 2', 'Darth Maul trains lightning to level 2', 'Darth Maul trains shadow to level 2'] , sep="\t")
    print("maul.train(maul.get_powers()[0][0]):", maul.train(maul.get_powers()[0][0]) in ['Darth Maul trains choke to level 3', 'Darth Maul trains lightning to level 3', 'Darth Maul trains shadow to level 3'] , sep="\t")
    print("maul.impart():", maul.impart() == 'Darth Maul does not have an apprentice' , sep="\t")
    print("maul.take_apprentice(tyranus):", maul.take_apprentice(tyranus) == 'Darth Maul cannot take Darth Tyranus as an apprentice' , sep="\t")    
    print("maul.fight(sidious):", maul.fight(sidious) == 'Darth Sidious kills Darth Maul in battle' , sep="\t")
    print("sidious.take_apprentice(tyranus):", sidious.take_apprentice(tyranus) == 'Darth Sidious takes Darth Tyranus as an apprentice' , sep="\t")
    print("vader.train('hate'):", vader.train("hate") == 'Darth Vader trains hate to level 1' , sep="\t")    
    print("vader.fight(tyranus):", vader.fight(tyranus) == 'Darth Vader kills Darth Tyranus in battle' , sep="\t")
    print(sidious.take_apprentice(vader))
    print("sidious.take_apprentice(vader):", sidious.take_apprentice(vader) == 'Darth Sidious takes Darth Vader as an apprentice' , sep="\t")

def print3():
    plagueis = Sith("Plagueis", "lightning", "choke") 
    sidious = Sith("Sidious", "shadow")
    maul = Sith("Maul")
    tyranus = Sith("Tyranus")
    vader = Sith("Vader", "hate")
    
    print('plagueis.get_name():', plagueis.get_name())
    print('plagueis.get_powers():', plagueis.get_powers())
    print('plagueis.train("choke"):', plagueis.train("choke"))
    print('plagueis.train("lightning"):', plagueis.train("lightning"))
    print('plagueis.take_apprentice(sidious):', plagueis.take_apprentice(sidious))
    print('plagueis.get_apprentice():', plagueis.get_apprentice())
    print('sidious.get_master():', sidious.get_master())
    print('plagueis.impart():', plagueis.impart())
    print('sidious.train("lightning"):', sidious.train("lightning"))
    print('sidious.train("choke"):', sidious.train("choke"))
    print('sidious.get_powers():', sidious.get_powers())
    print('sidious.take_apprentice(maul):', sidious.take_apprentice(maul))
    print('sidious.fight(plagueis):', sidious.fight(plagueis))
    print('plagueis.impart():', plagueis.impart())
    print('plagueis.impart():', plagueis.impart())
    print('sidious.get_powers():', sidious.get_powers())
    print('sidious.fight(plagueis):', sidious.fight(plagueis))
    print('sidious.train("shadow"):', sidious.train("shadow"))
    print('sidious.fight(plagueis):', sidious.fight(plagueis))
    print('sidious.train("lightning"):', sidious.train("lightning"))
    print('sidious.fight(plagueis):', sidious.fight(plagueis))
    print('sidious.take_apprentice(maul):', sidious.take_apprentice(maul))
    print('plagueis.train("choke"):', plagueis.train("choke"))
    print('sidious.impart():', sidious.impart())
    print('maul.train(maul.get_powers()[0][0]):', maul.train(maul.get_powers()[0][0]))
    print('maul.train(maul.get_powers()[0][0]):', maul.train(maul.get_powers()[0][0]))
    print('maul.train(maul.get_powers()[0][0]):', maul.train(maul.get_powers()[0][0]))
    print('maul.impart():', maul.impart())
    print('maul.take_apprentice(tyranus):', maul.take_apprentice(tyranus))
    print('maul.fight(sidious):', maul.fight(sidious))
    print('sidious.take_apprentice(tyranus):', sidious.take_apprentice(tyranus))
    print('vader.train("hate"):', vader.train("hate"))
    print('vader.fight(tyranus):', vader.fight(tyranus))
    print('sidious.take_apprentice(vader):', sidious.take_apprentice(vader))

# Uncomment to show sample execution
# print3()

# Uncomment to test sample execution
test3()
