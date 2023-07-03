##############
# Question 1 #
##############

def l33tify(string, code):
    result = ""
    for char in string:
        if char in code:
            result += code[char]
        else:
            result += char
    return result


l33t_dict = {
    'a': '4',
    'b': '8',
    'c': '(',
    'e': '3',
    'g': '[',
    'i': '1',
    'o': '0',
    's': '5',
    't': '7',
    'x': '%',
    'z': '2',
    }

# Uncomment to test
#print(l33tify("pheer my leet skills", l33t_dict))
#print(l33tify("python is cool", l33t_dict))

def rotate(lst):
    return lst[1:] + [lst[0]]

def advance_l33tify(string, code):
    result = ""
    copy = code.copy()
    for char in string:
        if char.isalpha():
            char = char.lower()
        if char in copy:
            result += copy[char][0]
            copy[char] = rotate(copy[char])
        else:
            result += char
    return result


adv_l33t_dict = {
    'a': ['4', '/-\\', '/_\\', '@', '/\\'],
    'b': ['8', '|3', '13', '|}', '|:', '|8', '18', '6', '|B'],
    'c': ['<', '{', '[', '('],
    'd': ['|)', '|}', '|]'],
    'e': ['3'],
    'f': ['|=', 'ph', '|#', '|"'],
    'g': ['[', '-', '[+', '6'],
    'h': ['|-|', '[-]', '{-}', '|=|', '[=]', '{=}'],
    'i': ['1', '|'],
    'j': ['_|', '_/', '_7', '_)'],
    'k': ['|<', '1<'],
    'l': ['|_', '|', '1'],
    'm': ['|\\/|', '^^', '/\\/\\'],
    'n': ['|\\|', '/\\/', '/V', '][\\\\]['],
    'o': ['0', '()', '[]', '{}'],
    'p': ['|o', '|O', '|>', '|*', '|°', '|D', '/o'],
    'q': ['O_', '9', '(', ')', ''],
    'r': ['|2', '12', '.-', '|^'],
    's': ['5', '$', '§'],
    't': ['7', '+', '7`', "'|'"],
    'u': ['|_|', '\\_\\', '/_/', '\\_/', '(_)'],
    'v': ['\\/'],
    'w': ['\\/\\/', '(/\\)', '\\^/', '|/\\|'],
    'x': ['%', '*', '><', '}{', ')('],
    'y': ['`/', '¥'],
    'z': ['2', '7_', '>_']
    }

# Uncomment to test
#print(advance_l33tify("Bow b4 me 4 I am root!!!", adv_l33t_dict))
#print(advance_l33tify("Mississippi", adv_l33t_dict))


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

def yearly_average(fname, year):
    data = read_csv(fname)[1:]
    result = {}
    for y, month, telco, service in data:
        if y == year:
            if telco not in result:
                result[telco] = []
            result[telco].append(float(service))
    for t in result:
        result[t] = round(sum(result[t])/len(result[t]), 4)
    return result
            
        
        


# Uncomment to test
#print(yearly_average("3g-coverage.csv", "2015"))
#print(yearly_average("3g-coverage.csv", "2013"))

def best_telco(fname, year):
    data = read_csv(fname)[1:]
    result = {}
    monthly = {}
    for y, month, telco, service in data:
        if y == year:
            if telco not in result:
                result[telco] = 0
            if month not in monthly:
                monthly[month] = {}
            if telco not in monthly[month]:
                monthly[month][telco] = float(service)
    for m in monthly:
        highest = None
        tel = None
        for telco in monthly[m]:
            if highest == None or monthly[m][telco] > highest:
                highest = monthly[m][telco]
                tel = telco
        result[tel] += 1
    return result
            

# Uncomment to test
#print(best_telco("3g-coverage.csv", "2015"))
#print(best_telco("3g-coverage.csv", "2013"))



##############
# Question 3 #
##############

class Villain:

    def __init__(self, name):
        self.name = name
        self.evilness = 0
        self.gadgets = {}
        self.own = []

    def get_evilness(self):
        return self.evilness

    def gadgets_owned(self):
        result = ()
        for gadget in self.own:
            result += (gadget.name, )
        return result

    def get_proficiency(self, gadget):
        if gadget in self.gadgets and self.gadgets[gadget] > 0:
            return self.name + "'s proficiency with " + gadget.name + " is " + str(self.gadgets[gadget])
        else:
            return self.name + " is not proficient with " + gadget.name

    def do_evil(self, action, gadget):
        if gadget not in self.own:
            return self.name + " does not have " + gadget.name
        else:
            self.evilness += gadget.value
            self.evilness += self.gadgets[gadget]
            gadget.decrease()
            self.gadgets[gadget] += 1
            return self.name + " " + action + " with " + gadget.name
            

    def steals(self, gadget):
        if gadget in self.own:
            return self.name + " already has " + gadget.name
        if gadget.owner == None:
            gadget.value = gadget.original
            gadget.owner = self
            if gadget not in self.gadgets:
                self.gadgets[gadget] = 0
            self.own.append(gadget)
            return self.name + " steals " + gadget.name
        else:
            other = gadget.owner
            other.evilness = other.evilness//2
            other.own.remove(gadget)
            gadget.value = gadget.original
            gadget.owner = self
            if gadget not in self.gadgets:
                self.gadgets[gadget] = 0
            self.own.append(gadget)
            return self.name + " steals " + gadget.name + " from " + other.name
            

    def envy(self, other):
        if isinstance(other, Gadget) and other.owner == None:
            return self.name + " envies " + other.name
        elif isinstance(other, Gadget) and other.owner != self:
            return self.name + " envies " + other.owner.name + "'s " + other.name
        elif isinstance(other, Gadget) and other.owner == self:
            return self.name + " already has " + other.name
        elif other == self:
            return self.name + " cannot envy himself"
        elif isinstance(other, Villain) and other.evilness == self.evilness:
            return "Nobody is envious"
        elif isinstance(other, Villain) and other.evilness > self.evilness:
            return self.name + " envies " + other.name
        elif isinstance(other, Villain) and other.evilness < self.evilness:
            return other.name + " envies " + self.name
          

class Gadget:

    def __init__(self, name, value):
        self.name = name
        self.original = value
        self.value = value
        self.owner = None

    def get_description(self):
        return self.name + " has level " + str(self.value) + " awesomeness"

    def owned_by(self):
        if self.owner != None:
            return self.name + " belongs to " + self.owner.name
        else:
            return self.name + " is unowned"
    def decrease(self):
        self.value = max(0, self.value - 1)

# Sample run test case
def test_q3():
    gru = Villain("Gru")
    vector = Villain("Vector")
    freeze_ray = Gadget("Freeze Ray", 5)
    lava_gun = Gadget("Lava Lamp Gun", 3)
    
    _=gru.get_evilness(); print(_ == 0, '\tgru.get_evilness():\t', _)
    _=gru.gadgets_owned(); print(tuple(sorted(_)) == (), '\tgru.gadgets_owned():\t', _)
    _=freeze_ray.get_description(); print(_ == "Freeze Ray has level 5 awesomeness", '\tfreeze_ray.get_description():\t', _)
    _=freeze_ray.owned_by(); print(_ == "Freeze Ray is unowned", '\tfreeze_ray.owned_by():\t', _)    
    _=gru.steals(freeze_ray); print(_ == "Gru steals Freeze Ray", '\tgru.steals(freeze_ray):\t', _)    
    _=gru.gadgets_owned(); print(tuple(sorted(_)) == ('Freeze Ray',), '\tgru.gadgets_owned():\t', _)
    _=freeze_ray.owned_by(); print(_ == "Freeze Ray belongs to Gru", '\tfreeze_ray.owned_by():\t', _)    
    _=gru.get_proficiency(freeze_ray); print(_ == "Gru is not proficient with Freeze Ray", '\tgru.get_proficiency(freeze_ray):\t', _)
    _=gru.do_evil("robs a bank", freeze_ray); print(_ == "Gru robs a bank with Freeze Ray", '\tgru.do_evil("robs a bank", freeze_ray):\t', _)
    _=gru.get_evilness(); print(_ == 5, '\tgru.get_evilness():\t', _)
    _=gru.get_proficiency(freeze_ray); print(_ == "Gru's proficiency with Freeze Ray is 1", '\tgru.get_proficiency(freeze_ray):\t', _)
    _=freeze_ray.get_description(); print(_ == "Freeze Ray has level 4 awesomeness", '\tfreeze_ray.get_description():\t', _)
    _=gru.do_evil("steals candy", freeze_ray); print(_ == "Gru steals candy with Freeze Ray", '\tgru.do_evil("steals candy", freeze_ray):\t', _)
    _=gru.get_proficiency(freeze_ray); print(_ == "Gru's proficiency with Freeze Ray is 2", '\tgru.get_proficiency(freeze_ray):\t', _)
    _=gru.get_evilness(); print(_ == 10, '\tgru.get_evilness():\t', _)
    _=freeze_ray.get_description(); print(_ == "Freeze Ray has level 3 awesomeness", '\tfreeze_ray.get_description():\t', _)
    _=gru.envy(freeze_ray); print(_ == "Gru already has Freeze Ray", '\tgru.envy(freeze_ray):\t', _)
    _=vector.envy(freeze_ray); print(_ == "Vector envies Gru's Freeze Ray", '\tvector.envy(freeze_ray):\t', _)
    _=gru.envy(vector); print(_ == "Vector envies Gru", '\tgru.envy(vector):\t', _)
    _=vector.steals(freeze_ray); print(_ == "Vector steals Freeze Ray from Gru", '\tvector.steals(freeze_ray):\t', _)
    _=gru.get_evilness(); print(_ == 5, '\tgru.get_evilness():\t', _)
    _=freeze_ray.get_description(); print(_ == "Freeze Ray has level 5 awesomeness", '\tfreeze_ray.get_description():\t', _)
    _=freeze_ray.owned_by(); print(_ == "Freeze Ray belongs to Vector", '\tfreeze_ray.owned_by():\t', _)
    _=gru.gadgets_owned(); print(tuple(sorted(_)) == (), '\tgru.gadgets_owned():\t', _)
    _=vector.do_evil("freezes Miami", freeze_ray); print(_ == "Vector freezes Miami with Freeze Ray", '\tvector.do_evil("freezes Miami", freeze_ray):\t', _)
    _=vector.get_evilness(); print(_ == 5, '\tvector.get_evilness():\t', _)
    _=gru.envy(vector); print(_ == "Nobody is envious", '\tgru.envy(vector):\t', _)
    _=gru.envy(lava_gun); print(_ == "Gru envies Lava Lamp Gun", '\tgru.envy(lava_gun):\t', _)
    _=gru.do_evil("steals Freeze Ray", lava_gun); print(_ == "Gru does not have Lava Lamp Gun", '\tgru.do_evil("steals Freeze Ray", lava_gun):\t', _)
    _=gru.envy(lava_gun); print(_ == "Gru envies Lava Lamp Gun", '\tgru.envy(lava_gun):\t', _)
    _=gru.steals(lava_gun); print(_ == "Gru steals Lava Lamp Gun", '\tgru.steals(lava_gun):\t', _)
    _=gru.do_evil("steals the Queen\'s crown", lava_gun); print(_ == "Gru steals the Queen's crown with Lava Lamp Gun", '\tgru.do_evil("steals the Queen\'s crown", lava_gun):\t', _)
    _=gru.get_evilness(); print(_ == 8, '\tgru.get_evilness():\t', _)
    _=gru.steals(freeze_ray); print(_ == "Gru steals Freeze Ray from Vector", '\tgru.steals(freeze_ray):\t', _)
    _=vector.get_evilness(); print(_ == 2, '\tvector.get_evilness():\t', _)
    _=gru.get_evilness(); print(_ == 8, '\tgru.get_evilness():\t', _)
    _=gru.envy(vector); print(_ == "Vector envies Gru", '\tgru.envy(vector):\t', _)
    _=gru.gadgets_owned(); print(tuple(sorted(_)) == ('Freeze Ray', 'Lava Lamp Gun'), '\tgru.gadgets_owned():\t', _)
    _=gru.do_evil("freezes Vector", freeze_ray); print(_ == "Gru freezes Vector with Freeze Ray", '\tgru.do_evil("freezes Vector", freeze_ray):\t', _)
    _=gru.get_evilness(); print(_ == 15, '\tgru.get_evilness():\t', _)

# Uncomment to test
test_q3()
