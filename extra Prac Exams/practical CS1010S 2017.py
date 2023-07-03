###
### Question 1
###

# Q1A
def num_cards(h):
    if h == 1:
        return 2
    else:
        return h*num_cards(1) + num_cards(h-1) + h - 1


# Q1B
def num_triangles(h):
    def triangle(n):
        result = 0
        for i in range(1, n):
            result += i
        return result

    upright = 0
    for i in range(1, h + 1):
        upright += triangle(i)
    inverted = 0
    for j in range(h, 0, -2):
        inverted += triangle(j)

    return upright + inverted 

        
    



# Tests
def test_q1a():
    print(num_cards(1))
    print(num_cards(2))
    print(num_cards(3))
    print(num_cards(4))


def test_q1b():
    for i in range(1, 10):
        print(i, num_triangles(i))


# Uncomment to test
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
# Q2A
def yearly_stats(fname, nric):
    data = read_csv(fname)[1:]
    first = None
    last = None
    smallest = None
    largest = None
    average = []
    for tax in data:
        if tax[0] == nric:
            if first == None or int(tax[1]) < first:
                first = int(tax[1])
            if last == None or int(tax[1]) > last:
                last = int(tax[1])
            if smallest == None or int(tax[3]) < smallest:
                smallest = int(tax[3])
            if largest == None or int(tax[3]) > largest:
                largest = int(tax[3])
            average.append(int(tax[3]))
    return (first, last, smallest, largest, round(sum(average)/len(average), 2))
            
        


# Q2B
def effective_tax(fname):
    data = read_csv(fname)[1:]
    by_year = {}
    for tax in data:
        if tax[1] not in by_year:
            by_year[tax[1]] = []
        total_rebate = 0
        for elem in tax[4:]:
            total_rebate += int(elem)
        etr = int(tax[3])*100/(int(tax[2]) - total_rebate)
        by_year[tax[1]].append(etr)
    for year in by_year:
        by_year[year] = round(sum(by_year[year])/ len(by_year[year]), 2)
    return by_year



# Tests
def test_q2a():
    print(yearly_stats("tax_data.csv", "G2407965J"))
    print(yearly_stats("tax_data.csv", "G2380503K"))


def test_q2b():
    print(effective_tax("tax_data.csv") == \
        {'2017': 1.95, '2016': 1.02, '2015': 1.02, '2014': 1.02})


#test_q2a()
#test_q2b()




###
### Question 3
###

### Your answer here.
class Kaiju(object):

    def __init__(self, name, category, attacks):
        self.name = name
        self.category = category
        self.health = 10**category
        self.attacks = attacks
        self.alive = True
        self.mega = False
        self.original = name

    def get_health(self):
        if self.mega != False:
            return self.mega.health
        return self.health

    def damage(self, amount):
        if self.mega != False:
            if self.mega.alive == False:
                return self.mega.name + " is already dead"
            elif self.mega.health <= amount:
                self.mega.health = 0
                self.mega.alive = False
                return self.mega.name + " takes " + str(amount) + " damage and dies"
            else:
                self.mega.health -= amount
                return self.mega.name + " takes " + str(amount) + " damage"
        elif self.alive == False:
            return self.name + " is already dead"
        elif self.health <= amount:
            self.health = 0
            self.alive = False
            return self.name + " takes " + str(amount) + " damage and dies"
        else:
            self.health -= amount
            return self.name + " takes " + str(amount) + " damage"

    def attack(self, move):
        if self.mega != False:
            if self.mega.alive == False:
                return self.mega.name + " is already dead"
            elif move not in self.mega.attacks:
                return self.mega.name + " does not know " + move
            else:
                return self.mega.name + " performs " + move + " attack"
            
        elif self.alive == False:
            return self.name + " is already dead"
        elif move not in self.attacks:
            return self.name + " does not know " + move
        else:
            return self.name + " performs " + move + " attack"

    def merge(self, *others):
        if self.mega != False:
            return self.mega.merge(*others)
        for other in others:
            if other.mega != False:
                return other.original + " is already a Mega-Kaiju"
        else:
            health = self.health
            attacks = self.attacks
            for other in others:
                health += other.health
                attacks += other.attacks
            m = MegaKaiju("MegaKaiju", health, attacks)
            for other in others:
                other.mega = m
            self.mega = m
            return m
            
            
        
            

class MegaKaiju(Kaiju):

    def __init__(self, name, health, attacks):
        super().__init__(name, 0, attacks)
        self.health = health
        self.mega = self

    def merge(self, *others):
        for other in others:
            if other.mega == True:
                return other.original + " is already a Mega-Kaiju"
        else:
            for other in others:
                self.health += other.health
                self.attacks += other.attacks
            for other in others:
                other.mega = self

        



# Tests
def test_q3():
    knifehead = Kaiju("Knifehead", 3, ("Headbutt", "Snapping jaws"))
    rajin = Kaiju("Rajin", 5, ("Electric jaw", "Morphic skull", "Shredding bite"))
    hajuka = Kaiju("Hajuka", 4, ("Molten blood",))
    shrikethorn = Kaiju("Shrikethorn", 4, ("Weaponized spines",))
    ripper = Kaiju("Ripper", 1, ())

    _=knifehead.attack('Headbutt'); print(_ == "Knifehead performs Headbutt attack", "\tknifehead.attack('Headbutt'):\t", _)
    _=knifehead.attack('Molten blood'); print(_ == "Knifehead does not know Molten blood", "\tknifehead.attack('Molten blood'):\t", _)
    _=knifehead.damage(500); print(_ == "Knifehead takes 500 damage", "\tknifehead.damage(500):\t", _)
    _=knifehead.get_health(); print(_ == 500, "\tknifehead.get_health():\t", _)
    _=knifehead.damage(500); print(_ == "Knifehead takes 500 damage and dies", "\tknifehead.damage(500):\t", _)
    _=knifehead.attack('Headbutt'); print(_ == "Knifehead is already dead", "\tknifehead.attack('Headbutt'):\t", _)
    _=knifehead.damage(500); print(_ == "Knifehead is already dead", "\tknifehead.damage(500):\t", _)
    _=rajin.attack('Electric jaw'); print(_ == "Rajin performs Electric jaw attack", "\trajin.attack('Electric jaw'):\t", _)
    _=rajin.damage(50000); print(_ == "Rajin takes 50000 damage", "\trajin.damage(50000):\t", _)
    _=rajin.get_health(); print(_ == 50000, "\trajin.get_health():\t", _)
    _=hajuka.get_health(); print(_ == 10000, "\thajuka.get_health():\t", _)
    _=shrikethorn.get_health(); print(_ == 10000, "\tshrikethorn.get_health():\t", _)
    _=rajin.attack('Molten blood'); print(_ == "Rajin does not know Molten blood", "\trajin.attack('Molten blood'):\t", _)
    mega = rajin.merge(hajuka, shrikethorn)
    _=mega.get_health(); print(_ == 70000, "\tmega.get_health():\t", _)
    _=rajin.get_health(); print(_ == 70000, "\trajin.get_health():\t", _)
    _=hajuka.get_health(); print(_ == 70000, "\thajuka.get_health():\t", _)
    _=shrikethorn.attack('Molten blood'); print(_ == "MegaKaiju performs Molten blood attack", "\tshrikethorn.attack('Molten blood'):\t", _)
    _=shrikethorn.attack('Headbutt'); print(_ == "MegaKaiju does not know Headbutt", "\tshrikethorn.attack('Headbutt'):\t", _)
    _=ripper.merge(rajin); print(_ == "Rajin is already a Mega-Kaiju", "\tripper.merge(rajin):\t", _)
    _=rajin.merge(ripper); print(_ == None, "\trajin.merge(ripper):\t", _)
    _=ripper.get_health(); print(_ == 70010, "\tripper.get_health():\t", _)
    _=mega.damage(50000); print(_ == "MegaKaiju takes 50000 damage", "\tmega.damage(50000):\t", _)
    print(mega.get_health())
    print(ripper.get_health())
    _=ripper.damage(3000); print(_ == "MegaKaiju takes 3000 damage", "\tripper.damage(3000):\t", _)
    _=rajin.attack('Weaponized spines'); print(_ == "MegaKaiju performs Weaponized spines attack", "\trajin.attack('Weaponized spines'):\t", _)
    print(shrikethorn.get_health())
    _=shrikethorn.damage(18000); print(_ == "MegaKaiju takes 18000 damage and dies", "\tshrikethorn.damage(18000):\t", _)
    _=mega.attack('Weaponized spines'); print(_ == "MegaKaiju is already dead", "\tmega.attack('Weaponized spines'):\t", _)


# Uncomment to test question 3
test_q3()


